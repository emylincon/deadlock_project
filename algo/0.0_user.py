#!/usr/bin/env python3

import socket
import os
import ast
import struct
from threading import Thread
import random as r
import time

port = 65000        # The port used by the server

hosts = {}  # {hostname: ip}
multicast_group = '224.3.29.71'
server_address = ('', 10000)
record = []  # records the task list and execution and waiting time and host sent

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
'''
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
'''
thread_record = []


def gosh_dist(_range):
    return ((23 ** r.randrange(1, 1331)) % r.randrange(1, 1777)) % _range


def get_tasks():
    global tasks
    global _pos

    tasks = {}
    _t = r.randrange(2, 4)
    while len(tasks) < _t:
        a = list(_tasks.keys())[gosh_dist(5)]
        tasks[a] = _tasks[a]

    _t_time = waiting_time_init()
    return tasks, _t_time


def waiting_time_init():
    t_time = {i: [round(r.uniform(0.4, 0.8), 3), round((tasks[i]['period']) / (tasks[i]['wcet']), 3)] for i in
              tasks}  # t_time = {'ti': [execution_time, latency], ..}

    return t_time


def send_message(mg):
    _multicast_group = ('224.3.29.71', 10000)
    try:

        # Send data to the multicast group
        if mg == 'hello':
            smg = 'user'
            sock.sendto(str.encode(smg), _multicast_group)
            print('\nHello message sent')

    except Exception as e:
        print(e)


def receive_message():
    global hosts

    while True:
        data, address = sock.recvfrom(1024)

        if data.decode()[:6] == 'update':
            ho = ast.literal_eval(data.decode()[7:])
            hosts = list(ho.keys())
            # print('received: ', hosts)
            break


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def receive_data(_con, _addr):
    with _con:
        while True:
            try:
                data = _con.recv(1024)
                print(_addr[0], ': ', data.decode())
            except KeyboardInterrupt:
                print('Receive Tasks Terminated')
                break


def receive_tasks():
    _host_ = ip_address()
    _port_ = 64000        # Port to listen on (non-privileged ports are > 1023)

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((_host_, _port_))
                s.listen()
                conn, addr = s.accept()

                th = Thread(target=receive_data, args=(conn, addr))
                thread_record.append(th)
                th.start()
                _port_ += 10

        except KeyboardInterrupt:
            print('\nProgramme Forcefully Terminated')
            break


def send_task(_task, _host):
    global port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((_host, port))
        s.sendall(str.encode(_task))
    port = 65000


def client(t, h):    # t = tasks, h = host ip
    global port

    try:
        send_task(t, h)
    except ConnectionRefusedError:
        port += 10
        client(t, h)
    except KeyboardInterrupt:
        print('Programme Terminated')


def main():
    global record

    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    init = Thread(target=receive_message)
    thread_record.append(init)
    init.start()
    send_message('hello')
    while True:
        time.sleep(1)
        if len(hosts) > 0:
            break
    print('Client is connected to servers: {}'.format(hosts))
    while True:
        try:
            x = input('Enter "y" to start and "stop" to exit: ').strip().lower()
            if x == 'y':
                for i in range(500):
                    rand_host = hosts[gosh_dist(5)]      # randomly selecting a host to send task to
                    _task_ = get_tasks()
                    record.append([_task_, rand_host])
                    client(_task_, rand_host)
                    time.sleep(2)
            elif x == 'stop':
                cmd = "echo '{}' >> record.py".format(record)
                os.system(cmd)
                for i in thread_record:
                    i.stop()
                break
        except KeyboardInterrupt:
            print('Programme terminated')
            for i in thread_record:
                i.stop()
            break


if __name__ == "__main__":
    main()

