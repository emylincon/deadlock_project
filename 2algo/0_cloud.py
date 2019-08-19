import numpy as np
import ast
import time
import os
import socket
from threading import Thread
import paho.mqtt.client as mqtt

# deadlock project
_tasks = {'t1': {'wcet': 1, 'period': 3, 'deadline': 3},
          't2': {'wcet': 1, 'period': 5, 'deadline': 4},
          't3': {'wcet': 1, 'period': 5, 'deadline': 5},
          't4': {'wcet': 1, 'period': 10, 'deadline': 9},
          't5': {'wcet': 1, 'period': 5, 'deadline': 4}
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

received_task_queue = [[], {}]      # = [[task_list],{wait_time}]
# offload_register = {}      # {task: host_ip}
thread_record = []
_port_ = 62000
port = 63000
cloud_register = {}   # ={node_id:mec_ip} keeps address of task offloaded to cloud
cannot = []


def receive_tasks_client(_con, _addr):   # run as thread
    # unicast socket
    with _con:
        print('Connected: ', _addr)
        while True:
            try:
                data = _con.recv(1024)
                # print(_addr[0], ': ', data.decode())
                d = str(data.decode())
                if len(d) > 0:
                    received_task = ast.literal_eval(d)
                    received_task_queue[0].append(received_task[0])
                    received_task_queue[1][received_task[0]] = received_task[1]
                    cloud_register[received_task[0].split('.')[1]] = _addr[0]
            except Exception as e:
                print('Error Encountered')


def receive_connection():
    # unicast socket
    host = ip_address()
    port = 63000        # Port to listen on (non-privileged ports are > 1023)

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()

                thread_record.append(Thread(target=receive_tasks_client, args=(conn, addr)))
                thread_record[-1].daemon = True
                thread_record[-1].start()
                port += 10

        except KeyboardInterrupt:
            print('\nProgramme Forcefully Terminated')
            break


def on_connect(connect_client, userdata, flags, rc):
    # print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    data = str(msg.payload, 'utf-8')
    received_task = ast.literal_eval(data)
    received_task_queue[0].append(received_task[0])
    received_task_queue[1][received_task[0]] = received_task[1]
    # cloud_register[received_task[0].split('.')[2]] = _addr[0]


def connect_to_broker():
    global _client
    global broker_ip
    global topic

    username = 'mec'
    password = 'password'
    broker_ip = input('Broker Ip: ').strip()
    broker_port_no = 1883
    topic = ip_address()

    _client = mqtt.Client()
    _client.on_connect = on_connect
    _client.on_message = on_message

    _client.username_pw_set(username, password)
    _client.connect(broker_ip, broker_port_no, 60)


# safe state or not
def isSafe(processes, avail, need, allot):
    global cannot
    # tasks to offload if exit
    offload = []

    # Mark all processes as infinish
    finish = [0] * P

    # To store safe sequence
    safeSeq = [0] * P

    # Make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

        # While all processes are not finished
    # or system is not in safe state.
    count = 0
    while (count < P):

        # Find a process which is not finish
        # and whose needs can be satisfied
        # with current work[] resources.
        found = False
        for p in range(P):

            # First check if a process is finished,
            # if no, go for next condition
            if (finish[p] == 0):

                # Check if for all resources
                # of current P need is less
                # than work
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break

                # If all needs of p were satisfied.
                if (j == R - 1):

                    # Add the allocated resources of
                    # current P to the available/work
                    # resources i.e.free the resources
                    for k in range(R):
                        work[k] += allot[p][k]

                        # Add this process to safe sequence.
                    safeSeq[count] = processes[p]
                    count += 1

                    # Mark this p as finished
                    finish[p] = 1

                    found = True

        # If we could not find a next process
        # in safe sequence.
        if (found == False):
            print("System is not in safe state")

            a = list(set(processes) - set(safeSeq) - set(offload))
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
    if 0 in safeSeq:
        safeSeq = safeSeq[:safeSeq.index(0)]
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    if len(offload) > 0:
        print('|======== Cannot Execute tasks: ', offload, '========|')
        cannot += offload

    return safeSeq


def get_safe_seq(pro):
    global P
    global R

    # Number of processes
    P = len(pro)

    # Number of resources
    R = 3
    processes = ['{}_{}'.format(pro[i], i) for i in range(P)]

    # Available instances of resources
    avail = [15, 15, 15]
    n_need = [_need[i[:2]] for i in pro]
    # print('need', n_need)
    # Resources allocated to processes
    allot = [allocation[i[:2]] for i in pro]
    # print('allocation', allot)

    # Maximum R that can be allocated
    # to processes
    # maxm = [np.array(allot[i]) + np.array(n_need[i]) for i in range(len(n_need))]
    # print('max_matrix:', maxm)

    # Check system is in safe state or not
    return isSafe(processes, avail, n_need, allot)


def execute(local):
    print('\nExecuting :', local)
    for i in local:
        time.sleep((t_time[i]) / 2)  # cloud executes tasks in less time than MEC
        print('####### Executed: ', i)
        _client.publish()
        send_client(i, cloud_register[i.split('.')[1]])
    print('============== EXECUTION DONE ===============')


def send_task_client(_task, _host):
    global _port_
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((_host, _port_))
        s.sendall(str.encode(str(_task)))
    _port_ = 62000


def send_client(t, h):    # t = tasks, h = host ip
    global _port_

    try:
        send_task_client(t, h)
    except ConnectionRefusedError:
        _port_ += 10
        send_client(t, h)
    except KeyboardInterrupt:
        print('Programme Terminated')


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def run_me():
    global tasks
    global t_time

    print('\n========== Deadlock Emulation Program: Cloud Server ===============')
    print('Cloud ip: ', ip_address())
    receive = Thread(target=receive_connection)
    receive.daemon = True
    receive.start()
    m = input('Start (Y/N): ').lower()
    if m == 'y':
        print('\n============* Cloud Server Active *==============\n')
        while True:
            try:
                if len(received_task_queue[0]) == 0:
                    time.sleep(2)
                elif len(received_task_queue[0]) <= 2:
                    tasks, t_time = received_task_queue
                    execute(received_task_queue[0])
                    for t in tasks:
                        received_task_queue[0].remove(t)
                        del received_task_queue[1][t]

                    time.sleep(2)
                else:
                    tasks, t_time = received_task_queue
                    print('\nRunning Bankers Algorithm')
                    list_seq = get_safe_seq(tasks)
                    execute(list_seq)
                    for t in tasks:
                        received_task_queue[0].remove(t)
                        del received_task_queue[1][t]
                    time.sleep(2)
            except KeyboardInterrupt:
                print('\nProgramme Terminated')
                os.system('echo "cannot = {}" >> cannot.py')
                break
    else:
        print('\nProgramme Terminated')


def main():
    os.system('clear')
    run_me()


if __name__ == "__main__":
    main()