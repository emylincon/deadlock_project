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
import paramiko
import ast
import time
import os
import datetime as dt
import getpass as gp
import data

hosts = {}  # {hostname: ip}
multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

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

mec_waiting_time = {}   # {ip : [moving (waiting time + rtt)]}

offload_register = {}      # {task: host_ip}

discovering = 0            # if discovering == 0 update host
test = []
_time = []
_pos = 0
received_task_queue = []   # [(task_list,wait_time), ...]
thread_record = []


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_time():
    _time_ = dt.datetime.utcnow()
    return _time_


def get_rtt(host):
    rtt = pc.verbose_ping(host)

    return rtt


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def _lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm(_list):
    return reduce(_lcm, _list)


def gosh_dist(_range):
    return ((23 ** r.randrange(1, 1331)) % r.randrange(1, 1777)) % _range


def receive_tasks_client(_con, _addr):
    with _con:
        print('Connected: ', _addr)
        while True:
            data = _con.recv(1024)
            # print(_addr[0], ': ', data.decode())
            received_task = ast.literal_eval(data.decode())
            received_task_queue.append([received_task, _addr[0]])


def receive_connection():
    host = ip_address()
    port = 65000        # Port to listen on (non-privileged ports are > 1023)

    print('Server IP: {}'.format(host))

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()

                thread_record.append(Thread(target=receive_tasks_client, args=(conn, addr)))
                thread_record[-1].start()
                port += 10

        except KeyboardInterrupt:
            print('\nProgramme Forcefully Terminated')
            break


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

    print('s (task, execution_time): ', schedule)
    print('r: ', register)
    if len(missed) > 0:
        print('missed deadline: ', missed)
        cooperative_mec(missed, 0)

    return offloaded + schedule


# generate execution sequence
def wait_die(processes, avail, n_need, allocat):
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
        cooperative_mec(offload, 0)

    print('Execution seq: ', exec_seq)

    return exec_seq


def get_exec_seq(pro):

    processes = ['{}_{}'.format(pro[i], i) for i in range(len(pro))]

    # Available instances of resources
    avail = [5, 5, 5]
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
        j = '_'.join(i.split('_')[:-1])            # i = 't5_3_3', j = 't5_3'
        time_dic[i] = round(t_time[j][0] + pre, 3)
        pre += t_time[j][0]
    w_send = round(time_dic[list(time_dic.keys())[-1]]/2, 3)            # waiting time = total waiting time ÷ 2 average waiting time might be too tight
    send_message(str(w_send))   # Broadcasting waiting time to cooperative MECs
    return time_dic


def compare_local_mec(list_seq):
    time_compare_dict = {i: t_time['_'.join(i.split('_')[:-1])][1] > list_seq[i] for i in list_seq}
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
    return avg1


def send_message(mg):
    _multicast_group = ('224.3.29.71', 10000)
    try:

        # Send data to the multicast group
        if mg == 'hello':
            smg = mg + ' ' + message()
            sock.sendto(str.encode(smg), _multicast_group)
            print('\nHello message sent')
        elif mg == 'update':
            ho = hosts.copy()
            ho[message()] = host_ip
            smg = mg + ' ' + str(ho)
            sock.sendto(str.encode(smg), _multicast_group)
            # print('\n===**====**==update message sent===**======**=========')
        else:
            sock.sendto(str.encode(mg), _multicast_group)

    except Exception as e:
        print(e)


def message():
    cmd = ['cat /etc/hostname']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return hostname


def receive_message():
    global hosts

    while True:
        data, address = sock.recvfrom(1024)

        if data.decode()[:5] == 'hello':
            hosts[data.decode()[6:]] = address[0]

        elif (data.decode()[:6] == 'update') and (discovering == 0):
            hosts = ast.literal_eval(data.decode()[7:])
            # print('received: ', hosts)

        elif (data.decode()[:6] != 'update') and (address[0] != host_ip):
            w_time = calculate_mov_avg(address[0], float(data.decode()) + get_rtt(address[0]))      # calcuate moving average of mec wait time => w_time = wait time + rtt
            if address[0] in mec_waiting_time:
                mec_waiting_time[address[0]].append(w_time)
            else:
                mec_waiting_time[address[0]] = [w_time]
        elif data.decode().strip() == 'user':
            send_message('update')


def mec_comparison():
    # returns min average waiting for all mecs
    if len(mec_waiting_time) == 0:
        return 0
    min_mec = {i: mec_waiting_time[i][-1] for i in mec_waiting_time}
    min_wt = min(min_mec, key=min_mec.get)
    return min_wt


def mec_task_unicast(task, host_):
    try:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(host_, port, un, pw)
        cmd = ('echo "{} {} {}" >> /home/mec/deadlock_project/temp/task_share.txt'.format(host_ip, task, t_time[task[:2]]))  # task share : host ip task

        stdin, stdout, stderr = c.exec_command(cmd)
    except Exception as e:
        print(e)


def cooperative_mec(mec_list, n):
    for i in mec_list:
        _host = mec_comparison()
        if _host == 0:
            mec_task_unicast(i, cloud_ip)

            print('\n=========SENDING {} TO CLOUD==========='.format(i))

        elif n == 0:
            j = '_'.join(i.split('_')[:-1])
            if mec_waiting_time[_host][-1] < t_time[j][1]:     # CHECK IF THE MINIMUM MEC WAIT TIME IS LESS THAN TASK LATENCY

                mec_task_unicast(i, _host)                 # SENDS TASK TO MEC FOR EXECUTION

                mec_waiting_time[_host].append(mec_waiting_time[_host][-1] + t_time[j][0])      # adds a new average waiting time
                print('\n======SENDING {} TO MEC {}========='.format(i, _host))
            else:
                mec_task_unicast(i, cloud_ip)

                print('\n=========SENDING {} TO CLOUD==========='.format(i))
        else:
            j = '_'.join(i.split('_')[:-1])
            if mec_waiting_time[_host][-1] < t_time[j][1]:  # CHECK IF THE MINIMUM MEC WAIT TIME IS LESS THAN TASK LATENCY

                mec_task_unicast(i, _host)  # SENDS TASK TO MEC FOR EXECUTION

                mec_waiting_time[_host].append(mec_waiting_time[_host][-1] + t_time[j][0])  # adds a new average waiting time
                print('\n======SENDING {} TO MEC {}========='.format(i, _host))
            else:
                mec_task_unicast(i, cloud_ip)

                print('\n=========SENDING {} TO CLOUD==========='.format(i))


def check_mec_offload():
    global offloaded

    offloaded = []
    t_mec = {}                # {t1: [execution, latency}
    try:
        fr = open('/home/mec/deadlock_project/temp/task_share.txt', 'r')
        t = fr.readlines()
        for i in t:
            ta = i[:-1].split()[1][:2] + '_' + str(t.index(i))
            offloaded.append(ta)
            offload_register[ta] = i[:-1].split()[0]
            t_mec[ta] = ast.literal_eval(''.join(i[:-1].split()[2:]))
        fr.close()
        os.system('rm /home/mec/deadlock_project/temp/task_share.txt')
        print('Tasks Offloaded to MEC: {}'.format(offloaded))
    except Exception as e:
        print('no offloaded Task!')
    return t_mec


def execute(local):
    print('\nExecuting :', local)
    send = []
    for i in local:
        j = '_'.join(i.split('_')[:-1])
        time.sleep(t_time[j][0])
        print('#' *((local.index(i) + 1) * 3), ' Executed: ', i)
        if len(j) > 2:
            send_back_task(j)
            send.append(j)
    print('============== EXECUTION DONE ===============')
    return send


def send_back_task(o_task):
    _host_ip = ip_address()

    try:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(offload_register[o_task], port, un, pw)
        cmd = ('echo "{} {} {}" >> '
               '/home/mec/deadlock_project/temp/executed.txt'.format(o_task, _host_ip, get_time()))
        # task share, host ip task, execution_time

        stdin, stdout, stderr = c.exec_command(cmd)
    except Exception as e:
        print(e)


def receive_executed_task():
    try:
        fr = open('/home/mec/deadlock_project/temp/executed.txt', 'r')
        t = fr.readlines()
        for i in t:
            i = i[:-1].split()
            print('Received Executed task {} from {}'.format(i[0], i[1]))
        fr.close()
        os.system('rm /home/mec/deadlock_project/temp/executed.txt')
    except Exception as e:
        print('No Executed Tasks from MEC Received')


def send_task_client(_task, _host):
    global _port_
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((_host, _port_))
        s.sendall(str.encode(_task))
    _port_ = 64000


def send_client(t, h):    # t = tasks, h = host ip
    global _port_

    try:
        send_task_client(t, h)
    except ConnectionRefusedError:
        _port_ += 10
        send_client(t, h)
    except KeyboardInterrupt:
        print('Programme Terminated')


def run_me():
    global discovering

    initialization()
    while True:
        if len(hosts) == mec_no:
            print('MEC Details: ', hosts)
            del hosts[message()]
            discovering = 1
            break
        time.sleep(2)
    speak = Thread(target=speaking_node)
    thread_record.append(speak)
    speak.start()
    start_loop()


def start_loop():
    global _loc
    global tasks
    global t_time
    global send_back_host

    print('\n============* WELCOME TO THE DEADLOCK EMULATION PROGRAM *=============\n')

    x = gp.getpass('Press any key to Start...').lower()
    if x != 'exit':
        while True:
            try:
                if len(received_task_queue) > 0:
                    info = received_task_queue.pop(0)
                    tasks, t_time = info[0]
                    send_back_host = info[1]

                    print('EDF List of Processes: ', tasks, '\n')
                    print('\nDeadlock Algorithm')
                    list_seq = get_exec_seq(tasks)
                    if len(list_seq) > 0:  # do only when there is a task in safe sequence
                        wait_list = calc_wait_time(list_seq)
                        print('\nWaiting Time List: ', wait_list)
                        compare_result = compare_local_mec(wait_list)
                        print('\nExecute Locally: ', compare_result[1])
                        t_loc = len(compare_result[1])  # total number of tasks to be executed locally
                        print('\nExecute in MEC: ', compare_result[0])

                        print('\nSending to cooperative platform')
                        if len(compare_result[0]) > 0:
                            cooperative_mec(compare_result[0], 1)
                        _send_back = execute(compare_result[1])
                        _loc = t_loc
                        if len(_send_back) > 0:  # do only when there is a task to send back
                            _loc = t_loc - len(_send_back)
                    receive_executed_task()
                else:
                    print('========= Waiting for tasks ==========')
                    os.system('clear')
            except KeyboardInterrupt:
                print('\nProgramme Terminated')
                for i in thread_record:
                    i.stop()
                    break
            print('\nEnter "Exit" to stop Programme!')


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
    try:
        mec_no = int(input('Number of MECs: ').strip())
        cloud_ip = input('Cloud Server IP: ').strip()
        print('\nCompiling MEC Details')
        h1 = Thread(target=receive_message)
        h1.start()
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
    os.system('clear')
    run_me()


if __name__ == "__main__":
    main()

