import pickle
import paho.mqtt.client as mqtt
from threading import Thread
import time
import os
import paramiko
import json

# algorithm imports

mec_nodes = {'mec-9': '192.168.122.119', 'mec-8': '192.168.122.118', 'mec-7': '192.168.122.117',
             'mec-6': '192.168.122.116', 'mec-5': '192.168.122.115', 'mec-4': '192.168.122.114',
             'mec-3': '192.168.122.113', 'mec-2': '192.168.122.112', 'mec-1': '192.168.122.111',
             'osboxes-0': '192.168.122.110'}


class BrokerCom:
    def __init__(self, user, pw, ip, sub_topic):
        self.user = user
        self.pw = pw
        self.ip = ip
        self.port = 1883
        self.topic = sub_topic
        self.client = mqtt.Client()
        self.finished = set()
        self.run = 1

    def on_connect(self, connect_client, userdata, flags, rc):
        print("Connected with Code :" + str(rc))
        # Subscribe Topic from here
        connect_client.subscribe(self.topic)

    def on_message(self, message_client, userdata, msg):
        data = pickle.loads(msg.payload)  # [hostname, ip]
        print(msg.topic, data)
        self.finished.add(data[1])

    def publish(self, topic, data):
        self.client.publish(topic, data)

    def broker_loop(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.username_pw_set(self.user, self.pw)
        self.client.connect(self.ip, self.port, 60)
        self.client.loop_start()
        while True:
            if self.run == 0:
                self.client.loop_stop()
                self.client.disconnect()
                print('broker loop stopped!')
                break

    def __del__(self):
        print('Broker Communication Object Deleted!')


def mec_id(client_ip):
    _id = client_ip.split('.')[-1]
    if len(_id) == 1:
        return '00' + _id
    elif len(_id) == 2:
        return '0' + _id
    else:
        return _id


"""
{'mec-9': '192.168.122.119', 'mec-8': '192.168.122.118', 'mec-7': '192.168.122.117', 'mec-6': '192.168.122.116', 'mec-5': '192.168.122.115', 'mec-4': '192.168.122.114', 'mec-3': '192.168.122.113', 'mec-2': '192.168.122.112', 'mec-1': '192.168.122.111', 'osboxes-0': '192.168.122.110'}
"""


def send_command(host_, no_mec, algo_no, send_path):
    try:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(host_, port, un, pw)

        algos = {1: 'algo_one', 2: 'algo_two', 3: 'algo_three', 4: 'algo_four', 5: 'algo_five', 6: 'algo_six'}

        if host_ == mec_nodes['osboxes-0']:
            p = '/home/mec/deadlock_project/4algo/manual/gui'
        else:
            p = '/home/mec/deadlock_project/4algo/manual/'
        cmd = f"python3 {p}/{algos[algo_no]}.py --n={no_mec} --p={send_path}"

        c.exec_command(cmd)
    except Exception as e:
        print(e)


def send_client(host_, no_mec, algo_no, send_path):
    try:
        c = paramiko.SSHClient()

        un = 'osboxes'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(host_, port, un, pw)

        algo_nos = {1: 2, 2: 3, 3: 7, 4: 10, 5: 12, 6: 16}

        p = '/home/osboxes/deadlock_project/4algo/manual/'
        cmd = f"python3 {p}/1client.py --n={no_mec} --a={algo_nos[algo_no]} --p={send_path}"

        c.exec_command(cmd)
    except Exception as e:
        print(e)


# python3 algo_three.py --n=10 --p=homo_4


def exp_control():
    global messenger

    broker_dict = {'user': 'mec', 'pw': 'password', 'sub_topic': 'control', 'ip': '192.168.122.111'}
    algos = [i for i in range(1, 7)]

    exp_no = [4, 7, 10]
    exp_type = ['homo', 'hetero']
    client_ips = ['192.168.122.124', '192.168.122.125', '192.168.122.126']
    counter = range(5, 16)
    messenger = BrokerCom(**broker_dict)
    h1 = Thread(target=messenger.broker_loop)
    h1.start()
    input('start: ')

    s_hosts = sorted({i: mec_nodes[i] for i in mec_nodes if i != 'osboxes-0'})
    for count in counter:
        for kind in exp_type:
            for algo_no in algos:
                for mec_no in exp_no:
                    hosts = {i: mec_nodes[i] for i in s_hosts[:mec_no - 1]}
                    hosts['osboxes-0'] = mec_nodes['osboxes-0']
                    # h_list = list(hosts)
                    send_path = f'{kind}_{count}'

                    print('initializing Edge nodes')
                    for hostname, ip in hosts.items():
                        print(hostname, ip)
                        send_command(host_=ip, no_mec=len(hosts), algo_no=algo_no, send_path=send_path)
                        #print(f'send_command(host_={ip}, no_mec={len(hosts)}, algo_no={algo_no}, send_path={send_path})')

                    time.sleep(20)
                    print('initializing Client Nodes')
                    print('\n\n')
                    for ip in client_ips:
                        send_client(host_=ip, no_mec=len(hosts), algo_no=algo_no, send_path=send_path)
                        # print(
                        #     f'send_client(host_={ip}, no_mec={len(hosts)}, algo_no={algo_no}, send_path={send_path})')

                    t_total = mec_no+3
                    print(f'Experiment {mec_no} for {kind} has commenced!')
                    while len(messenger.finished) != t_total:
                        time.sleep(60)

                    print('All is finished!')
                    messenger.finished = set()
                    time.sleep(3 * 60)
                    print(f'Experiment {mec_no} for {kind} is concluded!')
                    print('Waiting for 60 seconds Time Lapse!')
                    print('\n\n\n\n\n\n')
                    time.sleep(60)

    print('All Experiments has been Concluded!')


if __name__ == '__main__':
    os.system('clear')
    try:
        exp_control()
    except KeyboardInterrupt:
        print('killed')
        messenger.run = 0
