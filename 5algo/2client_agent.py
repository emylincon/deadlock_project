#!/usr/bin/env python3
import os
import paho.mqtt.client as mqtt
import pickle
import json


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
        global run
        print(f'Topic received: {msg.topic}')

        data = pickle.loads(msg.payload)  #
        if data[0] == 'start':  # ['start', {hostname: ip}, algo_id, homo/hetero, send_path]
            # --hosts= --al_id= --kind= --s_path=
            # run_me(mec_dict=data[1], algo_id_=data[2], exp_kind=data[3], send_path=data[4])
            cmd = f"python3 algorithms/client.py --hosts='{json.dumps(data[1])}' --al_id={data[2]} --kind='{data[3]}' " \
                  f"--s_path='{data[4]}'"
            os.system(cmd)

        elif data[0] == 'stop':  # ['stop']
            run = 0

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


def starter():
    global broker_ip
    global messenger
    global control_topic

    control_topic = 'control/control'
    broker_ip = '192.168.122.111'
    broker_dict = {'user': 'mec', 'pw': 'password', 'ip': broker_ip,
                   'sub_topic': 'control/client'}
    messenger = BrokerCom(**broker_dict)
    messenger.broker_loop()


if __name__ == "__main__":
    os.system('clear')
    starter()
