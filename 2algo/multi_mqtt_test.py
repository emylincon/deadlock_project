import paho.mqtt.client as mqtt
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Subscriber client')
print('-----------------------------------')

username = 'mec'
password = 'password'
broker_ip = 'localhost'
broker_port_no = 1883
topic1 = "test1"
topic2 = "test2"
print('-----------------------------------')


# Callback Function on Connection with MQTT Server
def on_connect(connect_client, userdata, flags, rc):
    print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic1)
    connect_client.subscribe(topic2)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    print('Publisher: ', str(msg.payload, 'utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)

client.loop_forever()