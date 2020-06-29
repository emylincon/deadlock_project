import paho.mqtt.client as mqtt
import pickle
import subprocess as sp
import socket
import os
import json


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
        print(f'data received: {data}')
        if (data[0] == 'start') and (host_id in data[1]):
            no_of_mec = len(data[1])
            del data[1][host_id]
            hosts = data[1]
            c_ip = data[3][host_id]
            run_me(no_mec=no_of_mec, hosts=hosts, algo_no=int(data[2]), cloud_ip=c_ip, send_path=data[4], ip=self.ip)

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


class BrokerSend:
    def __init__(self, user, pw, ip, sub_topic, data):
        self.user = user
        self.pw = pw
        self.ip = ip
        self.port = 1883
        self.topic = sub_topic
        self.client = mqtt.Client()
        self.client.username_pw_set(self.user, self.pw)
        self.client.connect(self.ip, self.port, 60)
        self.data = data

    def publish(self):
        self.client.publish(self.topic, self.data)

    def __del__(self):
        print('BrokerSend Object Deleted!')


def run_me(no_mec, hosts, algo_no, cloud_ip, send_path, ip):
    try:
        algos = {1: 'algo_one', 2: 'algo_two', 3: 'algo_three', 4: 'algo_four', 5: 'algo_five', 6: 'algo_six'}
        # (--hosts, --mec_no_, --cloud_ip, --s_path, --b_ip)
        cmd = f"python3 algorithms/gui/{algos[algo_no]}.py --hosts='{json.dumps(hosts)}' " \
              f"--mec_no={no_mec} --cloud_ip='{cloud_ip}'" \
              f"--s_path='{send_path}' --b_ip='{ip}'"
        os.system(cmd)
    except KeyboardInterrupt:
        print('killed run me')
        os.system('kill -9 {}'.format(os.getpid()))


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


def starter():
    global messenger
    global control_topic

    os.system('clear')
    control_topic = 'control/control'
    b_ip = '192.168.122.111'
    broker_dict = {'user': 'mec', 'pw': 'password', 'ip': b_ip,
                   'sub_topic': 'control/mec'}
    about = ['about', {host_id: ip_address()}]
    BrokerSend(user='mec', pw='password', ip=b_ip, sub_topic='control/control', data=pickle.dumps(about)).publish()

    messenger = BrokerCom(**broker_dict)

    try:
        messenger.broker_loop()
    except KeyboardInterrupt:
        messenger.run = 0
        cmd = 'kill -9 {}'.format(os.getpid())
        os.system(cmd)


if __name__ == '__main__':
    starter()


