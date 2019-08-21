import paho.mqtt.client as mqtt
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Publisher client')
print('-----------------------------------')
client = mqtt.Client()
username = 'mec'
password = 'password'
broker_ip = input("Broker's IP: ").strip()
broker_port_no = 1883
# topic = input("Topic: ").strip()
print('-----------------------------------')


client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)

while True:
    try:
        message = input('Input Message: ').strip().lower().split()
        client.publish(message[0], message[1])
        print("Message Sent")
    except KeyboardInterrupt:
        print('\nProgramme Terminated')
        break
