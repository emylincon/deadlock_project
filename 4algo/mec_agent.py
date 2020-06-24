import algorithms.algo_one as a1
import algorithms.algo_two as a2
import algorithms.algo_three as a3
import algorithms.algo_four as a4
import algorithms.algo_five as a5
import algorithms.algo_six as a6
import paho.mqtt.client as mqtt
import pickle
import subprocess as sp
import time
import random as r
import socket
import os
from threading import Thread


def get_hostname():
    cmd = ['cat /etc/hostname']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return hostname


host_id = get_hostname()


class BrokerCom:
    def __init__(self, user, pw, ip, sub_topic):
        self.user = user
        self.pw = pw
        self.ip = ip
        self.port = 1883
        self.topic = sub_topic
        self.client = mqtt.Client()
        self.run = 1

    def on_connect(self, connect_client, userdata, flags, rc):
        print("Connected with Code :" + str(rc))
        # Subscribe Topic from here
        connect_client.subscribe(self.topic)

    def on_message(self, message_client, userdata, msg):
        print(f'Topic received: {msg.topic}')

        data = pickle.loads(msg.payload)      # ['start', {hostname: ip}, algo_no, cloud_ip, send_path ]
        if (data[0] == 'start') and (host_id in data[1]):
            no_of_mec = len(data[1])
            del data[1][host_id]
            hosts = data[1]
            c_ip = data[3][host_id]
            run_me(no_mec=no_of_mec, hosts=hosts, algo_no=int(data[2]), cloud_ip=c_ip, send_path=data[4], ip=self.ip)
        elif (data[0] == 'stop') and (host_id in data[1]):     # ['stop', {hostname: ip}]
            running_algo.run = 0       # receives message to stop

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
                break

    def __del__(self):
        print('Broker Communication Object Deleted!')


def run_me(no_mec, hosts, algo_no, cloud_ip, send_path, ip):
    global running_algo

    algos = {1: a1, 2: a2, 3: a3, 4: a4, 5: a5, 6: a6}

    running_algo = algos[algo_no]
    algos[algo_no].run_me(mec_no_=no_mec, hosts_=hosts, cloud_ip_=cloud_ip,  send_path=send_path, broker_ip_=ip)

    time.sleep(r.uniform(10))

    messenger.publish(control_topic, pickle.dumps(['stop', ip_address()]))   # publishes to control they stopped


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def starter():
    global messenger
    global control_topic

    os.system('clear')
    control_topic = 'control/control'
    broker_dict = {'user': 'mec', 'pw': 'password', 'ip': input('Enter broker ip: '),
                   'sub_topic': 'control/mec'}
    messenger = BrokerCom(**broker_dict)

    h1 = Thread(target=messenger.broker_loop)
    h1.daemon = True
    h1.start()
    about = ['about', {host_id: ip_address()}]
    messenger.publish(control_topic, pickle.dumps(about))
    print(f'about sent: {about}')


if __name__ == '__main__':
    try:
        starter()
    except KeyboardInterrupt:
        messenger.run = 0
