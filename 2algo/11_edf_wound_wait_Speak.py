# Author Emeka Ugwuanyi Emmanuel

from functools import reduce
from sys import *
import numpy as np
import random as r
import ping_code as pc
import socket
import struct
import subprocess as sp
from threading import Thread
import threading
import ast
import time
import os
import psutil
import datetime as dt
import getpass as gp
import paho.mqtt.client as mqtt
from netifaces import interfaces, ifaddresses, AF_INET
import smtplib
import config


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

_cpu = []             # cpu plot list
prev_t = 0            # variable for cpu util
_off_mec = 0          # used to keep a count of tasks offloaded from local mec to another mec
_off_cloud = 0        # used to keep a count of tasks offloaded to cloud
_loc = 0              # used to keep a count of tasks executed locally
_inward_mec = 0       # used to keep a count of tasks offloaded from another mec to local mec
deadlock = [1]          # keeps count of how many deadlock is resolved
mec_waiting_time = {}   # {ip : [moving (waiting time + rtt)]}
memory = []
mec_rtt = {}               # {ip: [RTT]}

offload_register = {}      # {task: host_ip} to keep track of tasks sent to mec for offload
reoffload_list = [[], {}]   # [[task_list],{wait_time}] => records that’s re-offloaded to mec to execute.
discovering = 0            # if discovering == 0 update host
test = []
_time = []
_pos = 0
# received_task_queue = []   # [[(task_list,wait_time), host_ip], ....]
received_task_queue = []   # [(task_list,wait_time), ....]
thread_record = []
port = 65000
_port_ = 64000
cloud_register = {}   # ={client_id:client_ip} keeps address of task offloaded to cloud
cloud_port = 63000
stop = 0
t_track = 1
shared_resource_lock = threading.Lock()


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

    memory.append(round(algo.memory_percent(), 4))


def get_mec_rtts():
    for i in mec_rtt:
        mec_rtt[i].append(get_rtt(i))


def m_cpu():
    global prev_t

    # get cpu
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    _cpu.append(round(delta, 4))


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

    return round(rtt, 4)


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
    connect_client.subscribe('mec')


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    data = str(msg.payload, 'utf-8')
    if data[0] == 'c':       # receive from cloud
        data = data[2:]
        received_task = ast.literal_eval(data)
        # send_client({received_task: get_time()}, cloud_register[received_task.split('.')[2]])
        _client.publish(received_task.split('.')[2], str({received_task: get_time()}))

    elif data[0] == 't':     # receive from client
        received_task = ast.literal_eval(data[2:])
        received_task_queue.append(received_task)
    '''
    else:
        print('data: ', data)
    
    elif data[0] == 't':
        print('send: ', data[2:])
    '''


def connect_to_broker():
    global _client
    global broker_ip
    global topic

    username = 'mec'
    password = 'password'
    broker_ip = 'localhost'
    broker_port_no = 1883
    topic = 'mec'     # topic used to exchange mec details to clients

    _client = mqtt.Client()
    _client.on_connect = on_connect
    _client.on_message = on_message

    _client.username_pw_set(username, password)
    _client.connect(broker_ip, broker_port_no, 60)
    _client.loop_forever()


def edf():
    t_lcm = lcm([tasks[i]['period'] for i in tasks])

    t_dead = {i: tasks[i]['deadline'] for i in tasks}

    sorted_dead = sorted(t_dead.items(), key=lambda kv: (kv[1], kv[0]))
    # print(sorted_dead)

    ready_task = []
    for i in sorted_dead:
        period = tasks[i[0]]['period']
        # print('lcm: ', t_lcm, ' period: ', period)
        t_range = int(t_lcm/period)
        last_dead = 0
        for j in range(t_range):
            ready_task.append((i[0], last_dead+tasks[i[0]]['deadline']))
            last_dead += period

    ready_task = sorted(ready_task, key=lambda t: t[1])
    print(ready_task)

    t_time_ = 0
    schedule = []
    missed = []
    register = {i: 0 for i in tasks.keys()}   # {ti : amount executed}
    for i in ready_task:
        if (t_time_//tasks[i[0]]['period'])+1 <= register[i[0]]:
            while (t_time_//tasks[i[0]]['period'])+1 <= register[i[0]]:
                t_time_ += 1
                # schedule.append(('idle', t_time))
        if (t_time_//tasks[i[0]]['period'])+1 > register[i[0]]:
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

    return schedule


# generate execution sequence  using wound wait algorithm
def wound_wait(processes, avail, n_need, allocat):
    global deadlock

    offload = []

    # To store execution sequence
    exec_seq = []

    # Make a copy of available resources
    work = [0] * len(processes)

    # While all processes are not finished
    # or system is not in safe state.
    while 0 in work:
        ind = work.index(0)
        i = processes[ind]
        # print('comparing| process: ', i, n_need[i], 'work: ', avail)
        if not (False in list(np.greater_equal(avail, n_need[i]))):
            exec_seq.append(i)
            avail = np.add(avail, allocat[i])
            work[ind] = 1

        else:
            a = list(set(processes) - set(exec_seq) - set(offload))
            n = {}
            for j in a:
                n[j] = sum(allocat[j])
            _max = max(n, key=n.get)
            # print('work: ', work, 'need: ', _need[_max])
            if not (False in list(np.greater_equal(np.array(avail) + np.array(allocat[_max]), n_need[i]))):
                offload.append(_max)
                avail = np.array(avail) + np.array(allocat[_max])
                work[processes.index(_max)] = 1
            else:
                offload.append(i)
                avail = np.array(avail) + np.array(allocat[i])
                work[processes.index(i)] = 1

    if len(offload) > 0:
        print('offloading tasks: ', offload)
        cooperative_mec(offload)
        deadlock[0] += 1

    print('Execution seq: ', exec_seq)

    return exec_seq


def get_exec_seq(pro):

    # Number of processes
    p = len(pro)

    processes = ['{}_{}'.format(pro[i], i) for i in range(len(pro))]

    # Available instances of resources
    avail = [7, 5, 5]
    n_need = {i: _need[i[:2]] for i in processes}
    # print('need', n_need)
    # Resources allocated to processes
    allot = {i: allocation[i[:2]] for i in processes}

    # return execution sequence
    return wound_wait(processes, avail, n_need, allot)


def calc_wait_time(list_seq):
    pre = 0
    time_dic = {}
    for i in list_seq:
        j = i.split('_')[0]
        time_dic[i] = round(t_time[j][0] + pre, 3)
        pre += t_time[j][0]
    # waiting time = total waiting time ÷ 2 average waiting time might be too tight
    w_send = round(time_dic[list(time_dic.keys())[-1]]/2, 3)
    send_message('wt {} {}'.format(ip_address(), str(w_send)))   # multi-casting waiting time to cooperative MECs
    return time_dic


def compare_local_mec(list_seq):
    time_compare_dict = {i: t_time[i.split('_')[0]][1] > list_seq[i] for i in list_seq}
    print('local vs MEC comparison: ', time_compare_dict)
    execute_mec = []
    execute_locally = []
    for i in time_compare_dict:
        if time_compare_dict[i]:
            execute_locally.append(i)
        else:
            execute_mec.append(i)

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
            smg = mg + ' ' + str(['speaker', ip_address()])
            sock1.sendto(str.encode(smg), _multicast_group)
            print('\nHello message sent')
        elif mg == 'update':
            ho = hosts.copy()
            ho[message()] = host_ip
            smg = mg + ' ' + str(ho)
            sock1.sendto(str.encode(smg), _multicast_group)
            # print('\n===**====**==update message sent===**======**=========')
        elif mg == 'client':
            ho = hosts.copy()
            ho[message()] = host_ip
            smg = 'm {}'.format(ho)
            _client.publish(topic, smg, retain=True)
        else:
            sock1.sendto(str.encode(mg), _multicast_group)

    except Exception as e:
        print(e)


def message():
    cmd = ['cat /etc/hostname']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return hostname


def receive_message():
    global hosts

    while True:
        if stop == 1:
            print('Stopped : receive_message()')
            break
        else:
            data, address = sock1.recvfrom(1024)
            _d = data.decode()
            if _d[:5] == 'hello':
                _data = ast.literal_eval(_d[6:])
                hosts[_data[0]] = _data[1]
                # print('received: ', hosts)
                if _data[1] != host_ip:
                    mec_rtt[_data[1]] = []

            elif (_d[:6] == 'update') and (discovering == 0):
                hosts = ast.literal_eval(_d[7:])
                # print('received: ', hosts)

            elif _d[:2] == 'wt':
                split_data = _d.split()
                if split_data[1] != host_ip:
                    w_time = calculate_mov_avg(split_data[1], float(split_data[2]) + get_rtt(
                        address[0]))  # calcuate moving average of mec wait time => w_time = wait time + rtt

                    if split_data[1] in mec_waiting_time:
                        mec_waiting_time[split_data[1]].append(w_time)
                    else:
                        mec_waiting_time[split_data[1]] = [w_time]

            elif data.decode().strip() == 'user':
                send_message('update')


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

    for i in mec_list:
        _host = mec_comparison()
        if _host == 0:
            # send_cloud([i.split('_')[0], t_time[i.split('_')[0]][0]])  # [task_id,exec_time]
            _client.publish(cloud_ip, str([i.split('_')[0], t_time[i.split('_')[0]][0]]))
            _off_cloud += 1
            # cloud_register[i.split('_')[0].split('.')[2]] = send_back_host

            print('\n=========SENDING {} TO CLOUD==========='.format(i))

        else:
            j = i.split('_')[0]
            _max = np.array([7, 5, 5])
            send = 'false'
            if not (False in list(np.greater_equal(_max, _need[j[:2]]))):
                send = 'true'
            # CHECK IF THE MINIMUM MEC WAIT TIME IS LESS THAN LATENCY
            if mec_waiting_time[_host][-1] < t_time[j][1] and send == 'true':
                send_offloaded_task_mec('{} {} {}'.format('ex', mec_id(_host), [j, t_time[j][0]]))
                _off_mec += 1
                # SENDS TASK TO MEC FOR EXECUTION

                mec_waiting_time[_host].append(
                    round(mec_waiting_time[_host][-1] + (t_time[j][0]) / 2, 3))  # adds a new average waiting time
                print('\n======SENDING {} TO MEC {}========='.format(i, _host))
            else:
                _client.publish(cloud_ip, str([j, t_time[j][0]]))
                _off_cloud += 1
                # send_cloud([j, t_time[j][0]])    # # [task_id,exec_time]

                # cloud_register[j.split('.')[2]] = send_back_host

                print('\n=========SENDING {} TO CLOUD==========='.format(i))


def execute_re_offloaded_task(offloaded_task):
    exec_list = get_exec_seq(offloaded_task[0])
    for i in exec_list:
        j = i.split('_')[0]
        time.sleep(offloaded_task[1][j]/2)
        send_offloaded_task_mec('{} {}'.format(j.split('.')[1], i.split('*')[0]))


def execute(local):
    print('\nExecuting :', local)

    for i in local:
        j = i.split('_')[0]
        time.sleep(t_time[j][0]/2)
        print('#' * ((local.index(i) + 1) * 3), ' Executed: ', i)
        if j.split('.')[1] != node_id:
            send_offloaded_task_mec('{} {}'.format(j.split('.')[1], j))

        elif j.split('.')[1] == node_id:
            # send_client({j: get_time()}, send_back_host)
            _client.publish(j.split('.')[2], str({j: get_time()}))
    print('============== EXECUTION DONE ===============')


def receive_offloaded_task_mec():    # run as a thread
    global _inward_mec
    global t_track

    while True:
        if stop == 1:
            print('Stopped: receive_offloaded_task_mec()')
            break
        else:
            data, address = sock2.recvfrom(1024)
            if len(data.decode()) > 0:
                da = data.decode().split(' ')
                if (address[0] not in ip_set) and da[0] == node_id:               # send back to client
                    # send_client({da[1]: get_time()}, offload_register[da[1]])     # send back to client
                    _client.publish(da[1].split('.')[2], str({da[1]: get_time()}))
                elif (address[0] not in ip_set) and da[0] == 'ex' and da[1] == node_id:
                    _received = ast.literal_eval(da[2] + da[3])
                    shared_resource_lock.acquire()
                    task = _received[0] + '*{}'.format(t_track)
                    reoffload_list[0].append(task)
                    reoffload_list[1][task] = _received[1]
                    shared_resource_lock.release()
                    t_track += 1
                    _inward_mec += 1


def call_execute_re_offload():
    global reoffload_list

    while True:
        if stop == 1:
            print('Stopped: call_execute_re_offload()')
            break
        else:
            if len(reoffload_list[0]) == 1:
                t = reoffload_list[0][-1]
                time.sleep(reoffload_list[1][t]/2)
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

        time.sleep(1)


def send_email(msg):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(config.email_address, config.password)
        subject = 'Deadlock results edf+wound_wait {}'.format(message())
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


def run_me():
    global discovering

    initialization()
    while True:
        if len(hosts) == mec_no:
            print('MEC Details: ', hosts)
            del hosts['speaker']
            discovering = 1
            break
        time.sleep(2)
    speak = Thread(target=speaking_node)
    thread_record.append(speak)
    speak.daemon = True
    speak.start()
    start_loop()


def start_loop():
    global _loc
    global tasks
    global t_time
    global node_id
    global stop

    print('\n============* WELCOME TO THE DEADLOCK EMULATION PROGRAM *=============\n')

    node_id = mec_id(ip_address())
    # print('node id: ', node_id)
    _threads_ = [receive_offloaded_task_mec, call_execute_re_offload, connect_to_broker]
    for i in _threads_:
        Thread(target=i).daemon = True
        Thread(target=i).start()
    time.sleep(2)
    send_message('client')  # send mec details to clients
    x = gp.getpass('Press any key to Start...').lower()
    if x != 'exit':
        print('========= Waiting for tasks ==========')
        while True:
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

                        print('\nSending to cooperative platform')
                        if len(compare_result[0]) > 0:
                            cooperative_mec(compare_result[0])
                        execute(compare_result[1])
                        generate_results()
                else:
                    send_message(str('wt {} 0.0'.format(ip_address())))
                    time.sleep(1)

            except KeyboardInterrupt:
                print('\nProgramme Terminated')
                result = f"wt_12_{mec_no} = {mec_waiting_time} \nrtt_12_{mec_no} = {mec_rtt} " \
                         f"\ncpu_12_{mec_no} = {_cpu} \ninward_mec12_{mec_no} = {_inward_mec}" \
                         f"\noff_mec12_{mec_no} = {_off_mec} \noff_cloud12_{mec_no} = {_off_cloud} " \
                         f"\nloc12_{mec_no} = {_loc} \ndeadlock12_{mec_no} = {deadlock} \nmemory12_{mec_no} = {memory}"
                cmd = 'echo "{}" >> data.py'.format(result)
                os.system(cmd)
                send_email(result)
                stop += 1
                '''
                for i in thread_record:
                    i.join()
                '''
                _client.loop_stop()
                time.sleep(1)
                print('done')
                os.system('kill -9 {}'.format(os.getpid()))
                break


def speaking_node():
    global mec_no

    while True:
        if len(hosts) > (mec_no - 1):
            send_message('update')
            mec_no = len(hosts) + 1
        time.sleep(2)


def initialization():
    global mec_no
    global host_ip
    global cloud_ip

    host_ip = ip_address()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print('Broker IP: ', s.getsockname()[0])
    try:
        mec_no = int(input('Number of MECs: ').strip())
        cloud_ip = input('Cloud Server IP: ').strip()
        print('\nCompiling MEC Details')
        h1 = Thread(target=receive_message)
        h2 = Thread(target=receive_offloaded_task_mec)
        h1.daemon = True
        h2.daemon = True
        h1.start()
        h2.start()
        time.sleep(1.5)
        while True:
            b = input('Send Hello Message (Y/N): ').strip().lower()
            if b == 'y':
                send_message('hello')
                break
            else:
                print('\nPlease Type "y" to send Hello message\n')
    except KeyboardInterrupt:
        print('\nProgramme Terminated')
        exit(0)


def main():
    global algo

    os.system('clear')
    print('mec ip: ', ip_address())
    algo = psutil.Process()
    discovering_group()
    offloading_group()
    host_ip_set()
    run_me()


if __name__ == "__main__":
    main()
