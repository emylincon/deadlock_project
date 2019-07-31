#!/usr/bin/env python3

import socket
import os
import ast
import struct
from threading import Thread
import random as r

port = 65000        # The port used by the server

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

        else:
            sock.sendto(str.encode(mg), _multicast_group)

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


def send_task(_task, _host):
    global port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((_host, port))
        s.sendall(str.encode(_task))
    port = 65000


def client():
    global port

    try:
        send_task()
    except ConnectionRefusedError:
        port += 10
        client()
    except KeyboardInterrupt:
        print('Programme Terminated')


def main():
    global host

    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    init = Thread(target=receive_message)
    init.start()
    client()


if __name__ == "__main__":
    main()

