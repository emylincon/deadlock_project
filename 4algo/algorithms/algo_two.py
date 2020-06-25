from functools import reduce
from sys import *
import numpy as np
import random as r
import ping_code as pc
import socket
import struct
import subprocess as sp
import threading
from threading import Thread
import ast
import time
import datetime as dt
import os
import psutil
from netifaces import interfaces, ifaddresses, AF_INET
import paho.mqtt.client as mqtt
import smtplib
import config
import paramiko

hosts = {}  # {hostname: ip}

_tasks = {'t1': {'wcet': 3, 'period': 20, 'deadline': 15},
          't2': {'wcet': 1, 'period': 5, 'deadline': 4},
          't3': {'wcet': 2, 'period': 10, 'deadline': 8},
          't4': {'wcet': 1, 'period': 10, 'deadline': 9},
          't5': {'wcet': 3, 'period': 15, 'deadline': 12}
          }

# mat = {'p0': ['cpu', 'mem', 'storage']}
_need = {
    't1': [7, 4, 3],
    't2': [1, 2, 2],
    't3': [6, 0, 0],
    't4': [0, 1, 1],
    't5': [4, 3, 1]

}
allocation = {
    't1': [0, 1, 0],
    't2': [2, 0, 0],
    't3': [3, 0, 2],
    't4': [2, 1, 1],
    't5': [0, 0, 2]
}

_cpu = []  # cpu plot list
prev_t = 0  # variable for cpu util
_off_mec = 0  # used to keep a count of tasks offloaded from local mec to another mec
_off_cloud = 0  # used to keep a count of tasks offloaded to cloud
_loc = 0  # used to keep a count of tasks executed locally
_inward_mec = 0  # used to keep a count of tasks offloaded from another mec to local mec
deadlock = [1]  # keeps count of how many deadlock is resolved
memory = []
mec_waiting_time = {}  # {ip : [moving (waiting time + rtt)]}
mec_rtt = {}  # {ip: [RTT]}

offload_register = {}  # {task: host_ip} to keep track of tasks sent to mec for offload
reoffload_list = [[], {}]  # [[task_list],{wait_time}] => records that’s re-offloaded to mec to execute.
discovering = 0  # if discovering == 0 update host
test = []
_time = []
_pos = 0
received_task_queue = []  # [[(task_list,wait_time), host_ip], ....]
received_time = []
thread_record = []
_port_ = 64000
cloud_register = {}  # ={client_id:client_ip} keeps address of task offloaded to cloud
cloud_port = 63000
task_record = {}  # keeps record of task reoffloaded
task_id = 0  # id for each task reoffloaded
shared_resource_lock = threading.Lock()
t_track = 1


def discovering_group():
    global sock1

    multicast_group = '224.3.29.71'
    server_address = ('', 10000)

    # Create the socket
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to the server address
    sock1.bind(server_address)
    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def offloading_group():
    global sock2

    multicast_group = '224.5.5.55'
    server_address = ('', 20000)

    # Create the socket
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to the server address
    sock2.bind(server_address)
    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def ip_address():
    try:
        cmd = ['ifconfig eth1 | grep inet | cut -d ":" -f 2 | cut -d " " -f 1']
        address = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
        if len(address.strip().split('.')) == 4:
            return address.strip()
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


def _memory():
    global memory

    memory.append(round(my_algo.memory_percent(), 4))


def m_cpu():
    global prev_t

    # get cpu
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    _cpu.append(round(delta, 4))


def get_mec_rtts():
    for i in mec_rtt:
        mec_rtt[i].append(get_rtt(i))


def generate_results():
    _memory()
    m_cpu()
    get_mec_rtts()


def host_ip_set():
    global ip_set

    ip_set = set()
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        ip_set.add(', '.join(addresses))


def get_time():
    _time_ = []
    d = str(dt.datetime.utcnow()).split()
    _time_ += d[0].split('-')
    g = d[1].split('.')
    _time_ += g[0].split(':')
    _time_.append(g[1])
    return _time_


def get_rtt(host):
    rtt = pc.verbose_ping(host)
    if rtt:
        return round(rtt, 4)
    else:
        return get_rtt(host)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def _lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm(_list):
    return reduce(_lcm, _list)


def gosh_dist(_range):
    return ((23 ** r.randrange(1, 1331)) % r.randrange(1, 1777)) % _range


def on_connect(connect_client, userdata, flags, rc):
    # print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(node_id)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    data = str(msg.payload, 'utf-8')
    if data[0] == 'c':  # receive from cloud
        received_task = data[2:]
        # send_client({received_task: get_time()}, cloud_register[received_task.split('.')[2]])
        if received_task in task_record:
            del task_record[received_task]
            received_task = '.'.join(received_task.split('.')[:-1])
            _client.publish(topic=received_task.split('.')[2], payload=str({received_task: get_time() + ['cloud']}), )
            cooperate['cloud'] += 1
            count_task_sent(received_task)

    elif data[0] == 't':  # receive from client
        received_task = ast.literal_eval(data[2:])
        received_task_queue.append(received_task)
        received_time.append(time.time())

    # else:
    #     print('data: ', data)


def connect_to_broker(stop):
    global _client

    username = 'mec'
    password = 'password'
    broker_port_no = 1883

    _client = mqtt.Client()
    _client.on_connect = on_connect
    _client.on_message = on_message

    _client.username_pw_set(username, password)
    _client.connect(broker_ip, broker_port_no, 60)
    _client.loop_start()
    while True:
        if stop():
            _client.loop_stop()
            _client.disconnect()
            print('broker loop terminated')
            break


def task_time_map(seq, process):
    exe_seq = []
    capacity_sum = 0
    for job in process:
        capacity_sum += process[job]['wcet']
    while capacity_sum > 0:
        for job in seq:
            if process[job]['wcet'] > 0:
                exe_seq.append(job)
                process[job]['wcet'] -= 1
                capacity_sum -= 1

    return exe_seq


total_received_task = 0


def edf():
    global total_received_task
    t_lcm = lcm([tasks[i]['period'] for i in tasks])

    t_dead = {i: tasks[i]['deadline'] for i in tasks}

    sorted_dead = sorted(t_dead.items(), key=lambda kv: (kv[1], kv[0]))
    # print(sorted_dead)

    ready_task = []
    for i in sorted_dead:
        period = tasks[i[0]]['period']
        # print('lcm: ', t_lcm, ' period: ', period)
        t_range = int(t_lcm / period)
        last_dead = 0
        for j in range(t_range):
            ready_task.append((i[0], last_dead + tasks[i[0]]['deadline']))
            last_dead += period

    ready_task = sorted(ready_task, key=lambda t: t[1])
    print(ready_task)

    t_time_ = 0
    schedule = []
    missed = []
    register = {i: 0 for i in tasks.keys()}  # {ti : amount executed}
    for i in ready_task:
        if (t_time_ // tasks[i[0]]['period']) + 1 <= register[i[0]]:
            while (t_time_ // tasks[i[0]]['period']) + 1 <= register[i[0]]:
                t_time_ += 1
                # schedule.append(('idle', t_time))
        if (t_time_ // tasks[i[0]]['period']) + 1 > register[i[0]]:
            if t_time_ + tasks[i[0]]['wcet'] <= i[1]:
                register[i[0]] += 1
                t_time_ += tasks[i[0]]['wcet']
                schedule.append(i[0])
            else:
                print('Deadline missed: ', i)
                missed.append(i[0])

    # print('s : ', schedule)
    # print('r: ', register)
    if len(missed) > 0:
        # print('missed deadline: ', missed)
        cooperative_mec(missed)
    _edf_ = task_time_map(schedule, tasks)
    total_received_task += len(_edf_)
    return _edf_


# generate execution sequence
def is_safe(processes, avail, _need_, allot, p):  # bankers algorithm
    need = [_need_[i] for i in _need_]
    _allot_ = [allot[i] for i in allot]
    # tasks to offload if exit
    offload = []

    # Number of resources
    res = 3

    # Mark all processes as unfinished
    finish = [0] * p

    # To store safe sequence
    safe_seq = [0] * p

    # Make a copy of available resources
    work = [0] * res
    for i in range(res):
        work[i] = avail[i]

        # While all processes are not finished
    # or system is not in safe state.
    count = 0
    while count < p:

        # Find a process which is not finish
        # and whose needs can be satisfied
        # with current work[] resources.
        found = False
        for t in range(p):

            # First check if a process is finished,
            # if no, go for next condition
            if finish[t] == 0:

                # Check if for all resources
                # of current P need is less
                # than work
                for j in range(res):
                    if need[t][j] > work[j]:
                        break

                # If all needs of p were satisfied.
                if j == res - 1:

                    # Add the allocated resources of
                    # current P to the available/work
                    # resources i.e.free the resources
                    for k in range(res):
                        work[k] += _allot_[t][k]

                        # Add this process to safe sequence.
                    safe_seq[count] = processes[t]
                    count += 1

                    # Mark this p as finished
                    finish[t] = 1

                    found = True

        # If we could not find a next process
        # in safe sequence.
        if not found:
            print("System is not in safe state")

            a = list(set(processes) - set(safe_seq) - set(offload))
            _max = np.array([0, 0, 0])
            n = {}
            for i in a:
                n[i] = sum(allocation[i[:2]])
            _max = max(n, key=n.get)
            print('work: ', work, 'need: ', _need[_max[:2]])
            offload.append(_max)
            work = np.array(work) + np.array(allocation[_max[:2]])
            count += 1

            # Mark this p as finished
            finish[processes.index(_max)] = 1
            found = True

    # If system is in safe state then
    # safe sequence will be as below
    if len(offload) > 0:
        safe_seq = safe_seq[:safe_seq.index(0)]
        print('offloading tasks: ', offload)
        cooperative_mec(offload)
        deadlock[0] += 1
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print('safe seq: ', safe_seq)

    return safe_seq


def get_exec_seq(pro):
    # Number of processes
    p = len(pro)

    processes = ['{}_{}'.format(pro[i], i) for i in range(len(pro))]

    # Available instances of resources
    avail = [6, 5, 5]
    n_need = {i: _need[i[:2]] for i in processes}
    # print('need', n_need)
    # Resources allocated to processes
    allot = {i: allocation[i[:2]] for i in processes}

    # return execution sequence
    return is_safe(processes, avail, n_need, allot, p)


def calc_wait_time(list_seq):
    pre = 0
    time_dic = {}
    for i in list_seq:
        j = i.split('_')[0]
        time_dic[i] = round(t_time[j][0] + pre, 3)
        pre += t_time[j][0]
    # waiting time = total waiting time ÷ 2 average waiting time might be too tight
    w_send = round(time_dic[list(time_dic.keys())[-1]] / 2, 3)
    send_message('wt {} {}'.format(ip_address(), str(w_send)))  # Broadcasting waiting time to cooperative MECs
    return time_dic


timed_out_tasks = 0


def compare_local_mec(list_seq):
    global received_time, timed_out_tasks
    execute_mec = []
    execute_locally = []
    diff = time.time() - received_time.pop(0)
    checking_times = {}
    for i in list_seq:
        t_time[i.split('_')[0]][1] -= diff
        # if t_time[i.split('_')[0]][1] < 0:
        #     _client.publish(i.split('_')[0].split('.')[2], str({i.split('_')[0]: get_time() + ['local']}), )
        #     timed_out_tasks += 1
        if t_time[i.split('_')[0]][1] > list_seq[i]:
            execute_locally.append(i)
        else:
            execute_mec.append(i)
            checking_times[i] = {'Latency': t_time[i.split('_')[0]][1], 'Expected_exec_time': list_seq[i]}
    print('Execution time comparison:= ', checking_times)
    return execute_mec, execute_locally


def calculate_mov_avg(ma1, a1):
    if ma1 in mec_waiting_time:
        _count = len(mec_waiting_time[ma1])
        avg1 = mec_waiting_time[ma1][-1]
    else:
        _count = 0
        avg1 = 0
    _count += 1
    avg1 = ((_count - 1) * avg1 + a1) / _count
    # ma1.append(avg1) #cumulative average formula
    # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return round(avg1, 4)


def send_message(mg):
    _multicast_group = ('224.3.29.71', 10000)
    try:

        # Send data to the multicast group
        if mg == 'hello':
            smg = mg + ' ' + str([get_hostname(), ip_address()])
            sock1.sendto(str.encode(smg), _multicast_group)
            print('\nHello message sent')

        else:
            sock1.sendto(str.encode(mg), _multicast_group)

    except Exception as e:
        print(e)


def get_hostname():
    cmd = ['cat /etc/hostname']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return hostname


def receive_message(stop):  # used for multi-cast message exchange among MEC
    global hosts

    while True:
        if stop():
            print('Stopped: receive_message()')
            break
        else:
            data, address = sock1.recvfrom(1024)
            _d = data.decode()
            if _d[:5] == 'hello':
                _data = ast.literal_eval(_d[6:])
                hosts[_data[0]] = _data[1]

                if _data[1] != host_ip:
                    mec_rtt[_data[1]] = []

            elif (_d[:6] == 'update') and (discovering == 0):
                hosts = ast.literal_eval(_d[7:])
                # print('received: ', hosts)
                for i in hosts:
                    if i != host_ip:
                        mec_rtt[i] = []

            elif _d[:2] == 'wt':

                split_data = _d.split()

                if split_data[1] != host_ip:

                    w_time = calculate_mov_avg(split_data[1], float(split_data[2]) + get_rtt(
                        address[0]))  # calcuate moving average of mec wait time => w_time = wait time + rtt

                    if split_data[1] in mec_waiting_time:
                        mec_waiting_time[split_data[1]].append(w_time)
                    else:
                        mec_waiting_time[split_data[1]] = [w_time]


def mec_comparison():
    # returns min average waiting for all mecs
    if len(mec_waiting_time) == 0:
        return 0
    min_mec = {i: mec_waiting_time[i][-1] for i in mec_waiting_time}
    min_wt = min(min_mec, key=min_mec.get)
    return min_wt


def cooperative_mec(mec_list):
    global _off_cloud
    global _off_mec
    global task_id, task_record

    for i in mec_list:
        _host = mec_comparison()
        if _host == 0:
            # send_cloud([i.split('_')[0], t_time[i.split('_')[0]][0]])  # [task_id,exec_time]
            _send_task = f"{i.split('_')[0]}.{task_id}"
            _client.publish(cloud_ip, str([_send_task, t_time[i.split('_')[0]][0]]), )
            task_record[_send_task] = 'cloud'
            task_id += 1
            _off_cloud += 1
            # cloud_register[i.split('_')[0].split('.')[2]] = send_back_host

            print('\n=========SENDING {} TO CLOUD==========='.format(i))

        else:
            j = i.split('_')[0]
            _max = np.array([6, 5, 5])
            send = 'false'
            if not (False in list(np.greater_equal(_max, _need[j[:2]]))):
                send = 'true'
            # CHECK IF THE MINIMUM MEC WAIT TIME IS LESS THAN LATENCY
            if mec_waiting_time[_host][-1] < t_time[j][1] and send == 'true':
                _send_task = f"{j}.{task_id}"
                send_offloaded_task_mec('{} {} {}'.format('ex', mec_id(_host), [_send_task, t_time[j][0]]))
                task_record[_send_task] = 'mec'
                task_id += 1
                _off_mec += 1
                # SENDS TASK TO MEC FOR EXECUTION

                w_send = mec_waiting_time[_host][-1] + 0.001
                mec_waiting_time[_host].append(w_send)  # adds a new average waiting time
                print('\n======SENDING {} TO MEC {}========='.format(i, _host))
            elif send == 'true' and (get_rtt(_host) < get_rtt(cloud_ip)):
                _send_task = f"{j}.{task_id}"
                send_offloaded_task_mec('{} {} {}'.format('ex', mec_id(_host), [_send_task, t_time[j][0]]))
                task_record[_send_task] = 'mec'
                task_id += 1
                _off_mec += 1
                # SENDS TASK TO MEC FOR EXECUTION
                w_send = mec_waiting_time[_host][-1] + 0.001
                mec_waiting_time[_host].append(w_send)  # adds a new average waiting time
                print('\n======SENDING {} TO MEC {}========='.format(i, _host))

            else:
                _send_task = f"{j}.{task_id}"
                _client.publish(cloud_ip, str([_send_task, t_time[j][0]]), )
                task_record[_send_task] = 'cloud'
                task_id += 1
                _off_cloud += 1
                # send_cloud([j, t_time[j][0]])    # # [task_id,exec_time]

                # cloud_register[j.split('.')[2]] = send_back_host

                print('\n=========SENDING {} TO CLOUD==========='.format(i))


outward_mec = 0
offload_check = []


def execute_re_offloaded_task(offloaded_task):
    global outward_mec, offload_check
    exec_list = get_exec_seq(offloaded_task[0])
    if len(exec_list) != len(offloaded_task[0]):
        print('\n\n', '@ ' * 50)
        print('exec: ', exec_list, 'off: ', offloaded_task[0])
        print('\n\n', '@ ' * 50)
        offload_check.append((exec_list, offloaded_task[0]))
    outward_mec += len(exec_list)
    for i in exec_list:  # i = 't1.1.2.3*1_3'
        j = i.split('_')[0]
        time.sleep(offloaded_task[1][j] / 2)
        # print('j task: ', j)
        send_offloaded_task_mec('{} {}'.format(j.split('.')[1], i.split('*')[0]))


clients_record = {}


def count_task_sent(task):
    global clients_record
    c_id = task.split('.')[2]
    if c_id in clients_record:
        clients_record[c_id] += 1
    else:
        clients_record[c_id] = 1


def execute(local):
    print('\nExecuting :', local)

    for i in local:
        j = i.split('_')[0]
        _t = t_time[j][0] / 2
        time.sleep(_t)
        print('#{}'.format(local.index(i) + 1), ' Executed: ', i)
        _client.publish(j.split('.')[2], str({j: get_time() + ['local']}), )
        count_task_sent(j)
        # if j.split('.')[1] != node_id:
        #     send_offloaded_task_mec('{} {}'.format(j.split('.')[1], j))
        #     outward_mec += 1
        # elif j.split('.')[1] == node_id:
        #     # send_client({j: get_time()}, send_back_host)
        #     _client.publish(j.split('.')[2], str({j: get_time()+['local']}), )
        #     count_task_sent(j)
        # else:
        #     print('else execute: ', j)
    print('============== EXECUTION DONE ===============')


cooperate = {'mec': 0, 'cloud': 0}


def receive_offloaded_task_mec(stop):  # run as a thread
    global _inward_mec
    global t_track

    while True:
        if stop():
            print('Stopped: receive_offloaded_task_mec()')
            break
        else:
            data, address = sock2.recvfrom(1024)
            if len(data.decode()) > 0:
                da = data.decode().split(' ')
                if (address[0] not in ip_set) and (da[0] == node_id):  # send back to client
                    # send_client({da[1]: get_time()}, offload_register[da[1]])     # send back to client
                    if da[1] in task_record:
                        del task_record[da[1]]
                        task_new = '.'.join(da[1].split('.')[:-1])
                        _client.publish(da[1].split('.')[2], str({task_new: get_time() + ['mec']}), )
                        count_task_sent(da[1])
                        cooperate['mec'] += 1
                    else:
                        print('*' * 30 + f'\n{da[1]} Not in Task Record\n' + '*' * 30)
                elif (address[0] not in ip_set) and (da[0] == 'ex') and (da[1] == node_id):
                    _received = ast.literal_eval(da[2] + da[3])
                    shared_resource_lock.acquire()
                    task = _received[0] + '*{}'.format(t_track)
                    reoffload_list[0].append(task)
                    reoffload_list[1][task] = _received[1]
                    shared_resource_lock.release()
                    t_track += 1
                    _inward_mec += 1


def call_execute_re_offload(stop):
    global reoffload_list

    while True:
        if stop():
            print('Stopped: call_execute_re_offload()')
            break
        else:
            if len(reoffload_list[0]) == 1:
                t = reoffload_list[0][-1]
                time.sleep(reoffload_list[1][t] / 2)
                shared_resource_lock.acquire()
                reoffload_list[0].remove(t)
                del reoffload_list[1][t]
                shared_resource_lock.release()
                send_offloaded_task_mec('{} {}'.format(t.split('.')[1], t.split('*')[0]))
            elif len(reoffload_list[0]) > 1:
                o = reoffload_list.copy()
                execute_re_offloaded_task(o)
                for i in o[0]:
                    shared_resource_lock.acquire()
                    reoffload_list[0].remove(i)
                    del reoffload_list[1][i]
                    shared_resource_lock.release()


def send_email(msg, send_path):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(config.email_address, config.password)
        subject = 'Deadlock results edf+bankers {} {}'.format(get_hostname(), send_path)
        # msg = 'Attendance done for {}'.format(_timer)
        _message = 'Subject: {}\n\n{}\n\n SENT BY RIHANNA \n\n'.format(subject, msg)
        server.sendmail(config.email_address, config.send_email, _message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)


def send_offloaded_task_mec(msg):
    _multicast_group = ('224.5.5.55', 20000)
    try:
        sock2.sendto(str.encode(msg), _multicast_group)

    except Exception as e:
        print(e)


def mec_id(client_ip):
    _id = client_ip.split('.')[-1]
    if len(_id) == 1:
        return '00' + _id
    elif len(_id) == 2:
        return '0' + _id
    else:
        return _id


def send_result(host_, data):
    try:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(host_, port, un, pw)
        for i in data:
            cmd = ('echo "{}" >> /home/mec/result/data.py'.format(i))  # task share : host ip task
            stdin, stdout, stderr = c.exec_command(cmd)
        c.close()
    except Exception as e:
        print(e)


def save_and_send(send_path):
    _id_ = get_hostname()[-1]
    result = f"\nwt{_id_}_3_{mec_no} = {mec_waiting_time} " \
             f"\nrtt{_id_}_3_{mec_no} = {mec_rtt} \ncpu{_id_}_3_{mec_no} = {_cpu} " \
             f"\noff_mec{_id_}_3_{mec_no} = {_off_mec} " \
             f"\noff_cloud{_id_}_3_{mec_no} = {_off_cloud} " \
             f"\ninward_mec{_id_}_3_{mec_no} = {_inward_mec}" \
             f"\nloc{_id_}_3_{mec_no} = {_loc} " \
             f"\ndeadlock{_id_}_3_{mec_no} = {deadlock} \nmemory{_id_}_3_{mec_no} = {memory}" \
             f"\ntask_received{_id_}_3_{mec_no} = {total_received_task} \nsent_t{_id_}_3_{mec_no} = {clients_record}" \
             f"\ncooperate{_id_}_3_{mec_no} = {cooperate} \ntask_record{_id_}_3_{mec_no} = {task_record}" \
             f"\noutward_mec{_id_}_3_{mec_no} = {outward_mec}" \
             f"\noffload_check{_id_}_3_{mec_no} = {offload_check}" \
             f"\ntimed_out_tasks{_id_}_3_{mec_no} = {timed_out_tasks}\n"
    list_result = [
        f"\nwt{_id_}_3_{mec_no} = {mec_waiting_time} ",
        f"\nrtt{_id_}_3_{mec_no} = {mec_rtt} \ncpu{_id_}_3_{mec_no} = {_cpu} ",
        f"\noff_mec{_id_}_3_{mec_no} = {_off_mec} \noff_cloud{_id_}_3_{mec_no} = {_off_cloud} ",
        f"\ninward_mec{_id_}_3_{mec_no} = {_inward_mec}",
        f"\nloc{_id_}_3_{mec_no} = {_loc} ",
        f"\ndeadlock{_id_}_3_{mec_no} = {deadlock} \nmemory{_id_}_3_{mec_no} = {memory}",
        f"\ntask_received{_id_}_3_{mec_no} = {total_received_task} \nsent_t{_id_}_3_{mec_no} = {clients_record}",
        f"\ncooperate{_id_}_3_{mec_no} = {cooperate} \ntask_record{_id_}_3_{mec_no} = {task_record} ",
        f"\noutward_mec{_id_}_3_{mec_no} = {outward_mec}",
        f"\noffload_check{_id_}_3_{mec_no} = {offload_check}",
        f"\ntimed_out_tasks{_id_}_3_{mec_no} = {timed_out_tasks}"
    ]
    path_ = 'data/raw/'
    if os.path.exists(path_):
        cmd = f"echo '' > {path_}{_id_}_3_{mec_no}datal.py"
        os.system(cmd)
        cmd = f"echo '' > {path_}{_id_}_3_{mec_no}datap.py"
        os.system(cmd)
    else:
        os.mkdir(path_)
        cmd = f"echo '' > {path_}{_id_}_3_{mec_no}datal.py"
        os.system(cmd)
        cmd = f"echo '' > {path_}{_id_}_3_{mec_no}datap.py"
        os.system(cmd)

    file_ = open(f'{path_}{_id_}_3_{mec_no}datap.py', 'w')
    for i in list_result:
        cmd = f'echo "{i}" >> {path_}{_id_}_3_{mec_no}datal.py'
        file_.write(i)
        os.system(cmd)
    file_.close()
    sp.run(
        ["scp", f"{path_}{_id_}_3_{mec_no}datap.py", f"mec@{hosts['osboxes-0']}:{send_path}"])

    send_result(hosts['osboxes-0'], list_result)
    send_email(result, send_path)
    if len(task_record) > 0:
        for _task_ in task_record:
            task_new = '.'.join(_task_.split('.')[:-1])
            _client.publish(task_new.split('.')[2], str({task_new: get_time() + [task_record[_task_]]}), )


def terminate_process():
    global prev_t, _loc, _off_mec, _off_cloud, _inward_mec, outward_mec, deadlock, memory, mec_waiting_time, mec_rtt
    global offload_register, reoffload_list, discovering, test, _time, _pos, received_task_queue, received_time
    global cloud_register, t_track, task_record, task_id, cooperate, clients_record, offload_check
    global timed_out_tasks, total_received_task, _cpu

    # reinitialize  #
    _cpu = []  # cpu plot list
    prev_t = 0  # variable for cpu util
    _off_mec = 0  # used to keep a count of tasks offloaded from local mec to another mec
    _off_cloud = 0  # used to keep a count of tasks offloaded to cloud
    _loc = 0  # used to keep a count of tasks executed locally
    _inward_mec = 0  # used to keep a count of tasks offloaded from another mec to local mec
    outward_mec = 0  # keeps count of tasks sent back to another mec after executing
    deadlock = [1]  # keeps count of how many deadlock is resolved
    memory = []
    mec_waiting_time = {}  # {ip : [moving (waiting time + rtt)]}
    mec_rtt = {}  # {ip: [RTT]}
    offload_register = {}  # {task: host_ip} to keep track of tasks sent to mec for offload
    reoffload_list = [[], {}]  # [[task_list],{wait_time}] => records that’s re-offloaded to mec to execute.
    discovering = 0  # if discovering == 0 update host
    test = []
    _time = []
    _pos = 0
    received_task_queue = []  # [[(task_list,wait_time), host_ip], ....]
    received_time = []
    cloud_register = {}  # ={client_id:client_ip} keeps address of task offloaded to cloud
    t_track = 1
    task_record = {}  # keeps record of task reoffloaded
    task_id = 0  # id for each task reoffloaded

    cooperate = {'mec': 0, 'cloud': 0}
    clients_record = {}
    offload_check = [0, 0]
    timed_out_tasks = 0
    total_received_task = 0

    time.sleep(1)


run = 1  # tell agents child when to stop


def start_loop():
    global _loc
    global tasks
    global t_time
    global node_id
    global run

    print('\n============* WELCOME TO THE DEADLOCK EMULATION PROGRAM *=============\n')

    node_id = mec_id(ip_address())
    # print('node id: ', node_id)
    func_to_thread = [receive_message, receive_offloaded_task_mec, call_execute_re_offload, connect_to_broker]
    threads_ = []
    stop = False
    for i in func_to_thread:
        threads_.append(Thread(target=i, args=(lambda: stop,)))
        threads_[-1].daemon = True
        threads_[-1].start()

    print('algorithm is starting....')
    while run == 1:
        try:
            if len(received_task_queue) > 0:
                info = received_task_queue.pop(0)
                tasks, t_time = info

                print('EDF List of Processes: ', tasks, '\n')

                print('\n========= Running Deadlock Algorithm ===========')

                list_seq = get_exec_seq(edf())
                if len(list_seq) > 0:  # do only when there is a task in safe sequence
                    wait_list = calc_wait_time(list_seq)
                    print('\nWaiting Time List: ', wait_list)
                    compare_result = compare_local_mec(wait_list)
                    print('\nExecute Locally: ', compare_result[1])
                    _loc += len(compare_result[1])  # total number of tasks to be executed locally
                    print('\nExecute in MEC: ', compare_result[0])

                    if len(compare_result[0]) > 0:
                        print('\nSending to cooperative platform')
                        cooperative_mec(compare_result[0])
                    execute(compare_result[1])
                    generate_results()
            else:
                send_message(str('wt {} 0.0'.format(ip_address())))
                time.sleep(0.4)
        except KeyboardInterrupt:
            print('\nProgramme Terminated')
            stop = False
            for th in threads_:
                th.join()
            time.sleep(1)
            print('done')
            # os.system('kill -9 {}'.format(os.getpid()))
            break
    run = 1
    stop = False
    time.sleep(5)
    for th in threads_:
        th.join()


def run_me(hosts_, mec_no_, cloud_ip_, send_path, broker_ip_):  # call this from agent
    global discovering
    global hosts
    global mec_no
    global host_ip
    global cloud_ip
    global my_algo
    global broker_ip

    print('mec ip: ', ip_address())
    my_algo = psutil.Process()
    discovering_group()
    offloading_group()
    host_ip_set()

    hosts = hosts_
    mec_no = mec_no_
    cloud_ip = cloud_ip_
    broker_ip = broker_ip_

    host_ip = ip_address()
    print('MEC Details: ', hosts)
    discovering = 1
    time.sleep(2)
    for host in hosts:
        if host[1] != host_ip:
            mec_rtt[host[1]] = []
    start_loop()
    save_and_send(send_path)
    terminate_process()
