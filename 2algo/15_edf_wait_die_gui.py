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
import getpass as gp
import psutil
from drawnow import *
from matplotlib import pyplot as plt
from netifaces import interfaces, ifaddresses, AF_INET
import paho.mqtt.client as mqtt


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

test = []
_time = []
color_code = ['orange', 'brown', 'purple', 'pink', 'blue']
style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>']
mec_waiting_time = {}   # {ip : [moving (waiting time + rtt)]}

offload_register = {}      # {task: host_ip} to keep track of tasks sent to mec for offload
reoffload_list = [[], {}]
discovering = 0
mec_rtt = {}               # {ip: [RTT]}
thread_record = []   # keeps track of threads
prev_t = 0            # variable for cpu util
_cpu = []             # cpu plot list

_off_mec = 0          # used to keep a count of tasks offloaded from local mec to another mec
_off_cloud = 0        # used to keep a count of tasks offloaded to cloud
_loc = 0              # used to keep a count of tasks executed locally
_inward_mec = 0       # used to keep a count of tasks offloaded from another mec to local mec
deadlock = [1]          # keeps count of how many deadlock is resolved
_pos = 0

received_task_queue = []   # [[(task_list,wait_time), host_ip], ....]
_port_ = 64000
cloud_register = {}   # ={client_id:client_ip} keeps address of task offloaded to cloud
cloud_port = 63000
memory = []
stop = 0
t_track = 1
shared_resource_lock = threading.Lock()

fig = plt.figure()
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)


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


def _mov_avg(a1):
    ma1 = []   # moving average list
    avg1 = 0   # moving average pointwise
    count = 0
    for i in range(len(a1)):
        count += 1
        avg1 = ((count-1)*avg1+a1[i])/count
        ma1.append(round(avg1, 4))    # cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def percent(value, total):
    if value > 0:
        return round((value/total)*100, 2)
    else:
        return 0


def plot_offloaded_remote():
    keys = ['O-Out', 'Cloud', 'Local', 'O-In']
    total = _off_mec + _off_cloud + _loc + _inward_mec

    val = [percent(_off_mec, total),
           percent(_off_cloud, total),
           percent(_loc, total),
           percent(_inward_mec, total)]
    cols = ['r', 'g', 'b', 'm']
    ypos = ([0, 1, 2, 3])
    '''
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax2.pie(val, labels=keys, autopct='%.3f%%', wedgeprops=dict(width=0.5), 
    startangle=-40, shadow=True, explode=explode, colors=cols)
    '''
    values = [_off_mec, _off_cloud, _loc, _inward_mec]
    for i in values:
        j = values.index(i)
        ax2.text(j-0.1, values[j], '{}%'.format(val[j]), rotation=0,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax2.set_xticks(ypos)
    ax2.set_xticklabels(keys)
    ax2.bar(ypos, values, align='center', color=cols, alpha=0.3)
    ax2.set_title('Local/Remote Execution Report')
    plt.subplot(ax2)

# color=color_code[list(hosts.values()).index(i)]


def plot_deadlock():
    # cols = ['r']
    text = str(deadlock[-1] - 1) + " Deadlock Resolved"
    '''
    wedges, texts, autotexts = ax5.pie(deadlock, shadow=True, autopct=text,
                                       textprops=dict(rotation_mode='anchor', color="w", ha='left'), colors=cols)

    plt.setp(autotexts, size=9, weight="bold")
    '''
    ax5.text(0.5, 0.6, text, rotation=0, size=10,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.)))
    ax5.text(0.5, 0.45, '{} Tasks Received'.format(_loc+_inward_mec), rotation=0, size=10,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
    # ax5.set_title("Deadlock Resolved Counter")
    ax5.set_axis_off()
    plt.subplot(ax5)


def plot_memory():
    global memory

    memory.append(round(algo.memory_percent(), 4))

    ax6.grid(True)
    ax6.plot(list(range(len(_mov_avg(memory)))), _mov_avg(memory), linewidth=2, label='Memory', color='m')
    # ax6.set_title('Moving Memory Utilization')
    ax6.set_ylabel('Moving Memory')
    ax6.set_xlabel('Time (seconds)')
    ax6.fill_between(list(range(len(_mov_avg(memory)))), _mov_avg(memory), 0, alpha=0.5, color='m')
    ax6.legend()
    plt.subplot(ax6)


def plot_wait_time():
    ax1.grid(True)

    for i in mec_waiting_time:
        mv = _mov_avg(mec_waiting_time[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax1.plot(ptx,
                 pt,
                 style[list(hosts.values()).index(i)],
                 linewidth=2,
                 label=i)
    ax1.set_title('Waiting Time Queue')
    ax1.set_ylabel('Moving Wait + RTT')
    # ax2.set_xlabel('Time (seconds)')
    ax1.legend()
    plt.subplot(ax1)


def get_mec_rtts():
    for i in mec_rtt:
        mec_rtt[i].append(get_rtt(i))


def plot_rtts():
    get_mec_rtts()
    ax3.grid(True)
    for i in mec_rtt:
        mv = _mov_avg(mec_rtt[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax3.plot(ptx,
                 pt,
                 style[list(hosts.values()).index(i)],
                 linewidth=2,
                 label=i)
    ax3.set_title('RTT Utilization over Time')
    # ax3.set_ylabel('Moving RTT')
    # ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


def plot_cpu():
    global prev_t

    # get cpu
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    _cpu.append(round(delta, 4))

    # plot graph
    ax4.grid(True)
    ax4.plot(list(range(len(_mov_avg(_cpu)))), _mov_avg(_cpu), linewidth=2, label='CPU')
    # ax4.set_title('Moving CPU Utilization')
    ax4.set_ylabel('Moving CPU')
    ax4.set_xlabel('Time (seconds)')
    ax4.fill_between(list(range(len(_mov_avg(_cpu)))), _mov_avg(_cpu), 0, alpha=0.5)
    ax4.legend()
    plt.subplot(ax4)


def plot_graphs():
    plot_offloaded_remote()
    plot_wait_time()
    plot_rtts()
    plot_cpu()
    plot_deadlock()
    plot_memory()
    fig.suptitle('MEC Performance During Deadlock Experiment')


def show_graphs():
    drawnow(plot_graphs)


def ip_address():
    try:
        # cmd = ['ifconfig eth1 | grep inet | cut -d ":" -f 2 | cut -d " " -f 1']
        cmd = ['ifconfig ens4 | grep inet | head -n 1 | cut -d "t" -f 2 | cut -d " " -f 2']
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


def host_ip_set():
    global ip_set

    ip_set = set()
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        ip_set.add(', '.join(addresses))


def get_rtt(host):
    rtt = pc.verbose_ping(host)

    return round(rtt, 4)


def get_time():
    _time_ = []
    d = str(dt.datetime.utcnow()).split()
    _time_ += d[0].split('-')
    g = d[1].split('.')
    _time_ += g[0].split(':')
    _time_.append(g[1])
    return _time_


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
    if data[0] == 'c':
        data = data[2:]
        received_task = ast.literal_eval(data)
        # send_client({received_task: get_time()}, cloud_register[received_task.split('.')[2]])
        _client.publish(received_task.split('.')[2], str({received_task: get_time()}))

    elif data[0] == 't':  # receive from client
        received_task = ast.literal_eval(data[2:])
        received_task_queue.append(received_task)

    else:
        print('data: ', data)


def connect_to_broker():
    global _client
    global broker_ip

    username = 'mec'
    password = 'password'
    broker_ip = hosts['speaker']
    broker_port_no = 1883

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


# generate execution sequence
def wait_die(processes, avail, n_need, allocat):
    global deadlock

    offload = []

    # To store execution sequence
    exec_seq = []

    # Make a copy of available resources
    work = [0] * len(processes)

    # While all processes are not finished
    # or system is not in safe state.
    while 'w' or 0 in work:
        if 0 in work:
            ind = work.index(0)
            i = processes[ind]
        elif 'w' in work:
            # print('wk: ', work)
            ind = work.index('w')
            i = processes[ind]
        else:
            break

        # print('comparing| process: ', i, _need[i], 'work: ', avail)
        if not (False in list(np.greater_equal(avail, n_need[i]))):
            exec_seq.append(i)
            avail = np.add(avail, allocat[i])
            work[ind] = 1
            # print('added: ', exec_seq)

        else:
            a = list(set(processes) - set(exec_seq) - set(offload))
            n = {}
            for j in a:
                n[j] = sum(allocat[j])
            _max = max(n, key=n.get)
            # print('work: ', work, 'need: ', _need[_max])
            if processes.index(_max) > processes.index(i):   # if true, i is older
                # if process is already waiting then offload process
                if work[ind] == 'w':
                    offload.append(i)
                    avail = np.array(avail) + np.array(allocat[i])
                    work[processes.index(i)] = 1
                    # print('offload reentry: ', i, offload)
                else:
                    # wait put process to waiting
                    work[processes.index(i)] = 'w'
                    # print('waiting: ', i)

            else:
                # abort i
                offload.append(i)
                avail = np.array(avail) + np.array(allocat[i])
                work[processes.index(i)] = 1
                # print('offload: ', i)

    if len(offload) > 0:
        print('offloading tasks: ', offload)
        cooperative_mec(offload)
        deadlock[0] += 1

    print('Execution seq: ', exec_seq)

    return exec_seq


def get_exec_seq(pro):

    # Number of processes
    p = len(pro)

    processes = ['{}_{}'.format(pro[i], i) for i in range(p)]

    # Available instances of resources
    avail = [7, 5, 5]
    n_need = {i: _need[i[:2]] for i in processes}
    # print('need', n_need)
    # Resources allocated to processes
    allot = {i: allocation[i[:2]] for i in processes}

    # return execution sequence
    return wait_die(processes, avail, n_need, allot)


def calc_wait_time(list_seq):
    pre = 0
    time_dic = {}
    for i in list_seq:
        j = i.split('_')[0]           # i = 't5_3_3', j = 't5_3'
        time_dic[i] = round(t_time[j][0] + pre, 3)
        pre += t_time[j][0]
    # waiting time = total waiting time ÷ 2 average waiting time might be too tight
    w_send = round(time_dic[list(time_dic.keys())[-1]]/2, 3)

    send_message('wt {} {}'.format(ip_address(), str(w_send)))  # Broadcasting waiting time to cooperative MECs
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
            smg = mg + ' ' + str([message(), ip_address()])
            sock1.sendto(str.encode(smg), _multicast_group)
            print('\nHello message sent')
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
            print('Stopped : receive_message')
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

            elif (data.decode()[:6] == 'update') and (discovering == 0):
                hosts = ast.literal_eval(data.decode()[7:])

            elif _d[:2] == 'wt':
                split_data = _d.split()
                if split_data[1] != host_ip:
                    # calcuate moving average of mec wait time => w_time = wait time + rtt
                    w_time = calculate_mov_avg(split_data[1], float(split_data[2]) + get_rtt(address[0]))
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
        # print('j task: ', j)
        send_offloaded_task_mec('{} {}'.format(j.split('.')[1], i.split('*')[0]))


def execute(local):
    print('\nExecuting :', local)

    # send = []
    for i in local:
        j = i.split('_')[0]
        time.sleep(t_time[j][0]/2)
        print('#' * ((local.index(i) + 1) * 3), ' Executed: ', i)
        if j.split('.')[1] != node_id:
            send_offloaded_task_mec('{} {}'.format(j.split('.')[1], j))
            # send.append(j)
        elif j.split('.')[1] == node_id:
            # send_client({j: get_time()}, send_back_host)
            _client.publish(j.split('.')[2], str({j: get_time()}))
    print('============== EXECUTION DONE ===============')
    # return send


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
                if (address[0] not in ip_set) and da[0] == node_id:  # send back to client
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
            print('Stopped: call_executed_re_offload()')
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
    global hosts

    initialization()
    while True:
        if len(hosts) == mec_no:
            print('MEC Details: ', hosts)
            del hosts[message()]
            discovering = 1
            break
        time.sleep(2)
    start_loop()


def start_loop():
    global _loc
    global tasks
    global t_time
    global stop
    global node_id

    print('\n============* WELCOME TO THE DEADLOCK EMULATION PROGRAM *=============\n')

    node_id = mec_id(ip_address())
    # print('node id: ', node_id)
    _threads_ = [receive_offloaded_task_mec, call_execute_re_offload, connect_to_broker]
    for i in _threads_:
        thread_record.append(Thread(target=i))
        Thread(target=i).daemon = True
        Thread(target=i).start()

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

                        if len(compare_result[0]) > 0:
                            print('\nSending to cooperative platform')
                            cooperative_mec(compare_result[0])
                        execute(compare_result[1])
                        show_graphs()
                else:
                    send_message(str('wt {} 0.0'.format(ip_address())))
                    # show_graphs()
                    time.sleep(.5)
            except KeyboardInterrupt:
                print('\nProgramme Terminated')
                cmd = 'echo "wt_16_4 = {} \nrtt_16_4 = {} \ncpu_16_4 = {} \noff_mec16_4 = {}' \
                      '\noff_cloud16_4 = {} \nloc16_4 = {} \ndeadlock16_4 = {}' \
                      '\nmemory16_4 = {} " >> data.py'.format(mec_waiting_time, mec_rtt, _cpu, _off_mec, _off_cloud,
                                                              _loc,
                                                              deadlock, memory)
                os.system(cmd)
                stop += 1
                for i in thread_record:
                    i.join()

                _client.loop_stop()
                print('done')

                break


def initialization():
    global mec_no
    global host_ip
    global cloud_ip

    host_ip = ip_address()
    try:
        mec_no = int(input('Number of MECs: ').strip())
        cloud_ip = input('Cloud Server IP: ').strip()
        print('\nCompiling MEC Details')
        h1 = Thread(target=receive_message)
        h2 = Thread(target=receive_offloaded_task_mec)
        thread_record.append(h1)
        thread_record.append(h2)
        h1.daemon = True
        h2.daemon = True
        h1.start()
        h2.start()
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
