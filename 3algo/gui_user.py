#!/usr/bin/env python3
import matplotlib
matplotlib.use('TkAgg')
import socket
import os
import ast
import struct
from threading import Thread
import random as r
import time
import datetime as dt
import subprocess as sp
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from drawnow import *
import smtplib
import config
import paramiko
import homo_dist as dst

port = 65000  # The port used by the server

# hosts = {}  # {hostname: ip}
multicast_group = '224.3.29.71'
server_address = ('', 10000)
record = []  # [({tasks}, {waiting time}), hostname] records the task list and execution and waiting time and host sent

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multi-cast group
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
task_record = {}  # records tasks start time and finish time {seq_no:{task:[duration, start_time,finish_time]}}
# idea for task naming # client-id_task-no_task-id  client id = 11, task no=> sequence no, task id => t1
tasks_executed_on_time = 0
tasks_not_executed_on_time = 0
timely_ = {'local':0, 'mec':0, 'cloud':0}
untimely_ = {'local':0, 'mec':0, 'cloud':0}
filename = {2: 'rms+bankers',
            3: 'edf+bankers',
            7: 'rms+wound_wait',
            10: 'rms+wait_die',
            12: 'edf+wound_wait',
            16: 'edf+wait_die'}
plt.ion()
fig = plt.figure(frameon=True)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)


def auto_value(no):
    if no < 5:
        return no
    elif no < 10:
        return no - 3
    elif no < 50:
        return no - 6
    elif no < 150:
        return no - 30
    elif no < 800:
        return no - 70
    elif no < 2000:
        return no - 200
    else:
        return no - 400


def plot_performance():
    name = ['Timely', 'Untimely']
    ypos = ([0, 1])
    total = tasks_executed_on_time + tasks_not_executed_on_time
    if tasks_executed_on_time > 0:
        timely = round((tasks_executed_on_time / total) * 100, 2)
    else:
        timely = 0

    if tasks_not_executed_on_time > 0:
        untimely = round((tasks_not_executed_on_time / total) * 100, 2)
    else:
        untimely = 0

    values = [tasks_executed_on_time, tasks_not_executed_on_time]
    ax1.set_xticks(ypos)
    ax1.set_xticklabels(name)
    ax1.bar(ypos, values, align='center', color=['g', 'm'], alpha=0.5)
    ax1.set_title('Task execution Time record')
    dis = 'Seq: {}\nTotal Tasks: {}\ntotal: {}'.format(seq, total, total_split_task)
    # ax1.annotate(dis, xy=(2, 1), xytext=(3, 1.5))

    ax1.text(1, auto_value(tasks_executed_on_time), dis, size=10, rotation=0,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.7, 0.7), fc=(1., 0.8, 0.8), ))
    ax1.text(-0.1, tasks_executed_on_time, '{}, {}%'.format(tasks_executed_on_time, timely), size=10, rotation=0,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax1.text(0.99, tasks_not_executed_on_time, '{}, {}%'.format(tasks_not_executed_on_time, untimely),
             size=10, rotation=0,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    plt.subplot(ax1)
    d = [[timely_, ax2, 'Timely Details'], [untimely_, ax3, 'UnTimely Details']]
    for info in d:
        plot_details(ax=info[1], data=info[0], title=info[2])
    fig.suptitle('MEC Performance During Deadlock Experiment')


def plot_details(ax, data, title):
    name = ['Local', 'MEC', 'Cloud']
    ypos = ([0, 1, 2])
    data_per = {}
    total = 0
    for i in data:
        total += data[i]
    for i in data:
        if data[i] == 0:
            data_per[i] = 0
        else:
            data_per[i] = round((data[i] / total) * 100, 2)

    values = list(data.values())
    ax.set_xticks(ypos)
    ax.set_xticklabels(name)
    ax.bar(ypos, values, align='center', color=['g', 'b', 'r'], alpha=0.5)
    ax.set_title(title)
    g = -0.1
    for i in data:
        ax.text(g, data[i], '{}, {}%'.format(data[i], data_per[i]), size=10, rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
        g += 1

    plt.subplot(ax)


def get_time():
    _time_ = dt.datetime.utcnow()
    return _time_


def gosh_dist(_range):
    return ((23 ** r.randrange(1, 1331)) % r.randrange(1, 1777)) % _range


def get_tasks():
    global tasks

    tasks = {}
    _t = r.randrange(2, 4)
    while len(tasks) < _t:
        a = list(_tasks.keys())[gosh_dist(5)]
        tasks[a] = _tasks[a]

    _t_time = waiting_time_init()
    return tasks, _t_time


def waiting_time_init():
    t_time = {i: [round(r.uniform(0.4, 0.8), 3), round((tasks[i]['period']) / (tasks[i]['wcet']*2), 3)] for i in
              tasks}  # t_time = {'ti': [execution_time, latency], ..} 0.4 0.8, 1.5, 4 | 1.3, 3.5 |1.25, 3.5| 1.2,3.4
    # .9, 2.1 | 0.8, 1.9 | 1.1, 2.3 | 1.5, 2.8
    # t_time = {i: [round(r.uniform(0.1, 0.4), 3), round(r.uniform(1.3, 2.5), 3)] for i in
    #           tasks}
    return t_time


# Callback Function on Connection with MQTT Server
def on_connect(connect_client, userdata, flags, rc):
    print("Connected with Code :" + str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic, qos=0)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    global hosts
    global host_dict
    global algo_id
    global ho

    # print the message received from the subscribed topic
    details = str(msg.payload, 'utf-8')[2:].split('_')
    ho = ast.literal_eval(details[0])  # {hostname: ip}
    algo_id = int(details[1])
    hosts = sorted(list(ho.values()))  # list of Ips
    host_dict = dict(zip(list(ho.values()), list(ho.keys())))  # {ip: hostname}
    # print('hosts: ', hosts)
    _client.loop_stop()


def get_mec_details():
    global topic
    global _client
    global broker_ip

    username = 'mec'
    password = 'password'
    broker_ip = input("Broker's IP: ").strip()
    broker_port_no = 1883
    topic = 'mec'

    _client = mqtt.Client()
    _client.on_connect = on_connect
    _client.on_message = on_message

    _client.username_pw_set(username, password)
    _client.connect(broker_ip, broker_port_no, 60)

    _client.loop_start()


def on_connect_task(connect_client, userdata, flags, rc):
    # print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(task_topic, qos=0)


# Callback Function on Receiving the Subscribed Topic/Message
def on_receive_task(message_client, userdata, msg):
    global tasks_executed_on_time
    global tasks_not_executed_on_time
    # print the message received from the subscribed topic
    data = str(msg.payload, 'utf-8')
    received_task = ast.literal_eval(data)      # {task_id: ['2020', '04', '09', '14', '38', '39', '627060', '<mec>']}

    for i in received_task:
        tk = '.'.join(i.split('.')[:4])
        # print('tk: {}'.format(tk))
        seq_no = int(tk.split('.')[3])   # naming tasks = task_id.node_id.client_id.sequence_no  =>t2.110.170.10
        k = task_record[seq_no][tk]     # task_record= {seq_no:{task:[duration,start_time,finish_time]}}
        if len(k) < 3:                 # check if i have received a task with the same id
            a = received_task[i]
            k.append(dt.datetime(int(a[0]), int(a[1]),
                                 int(a[2]), int(a[3]),
                                 int(a[4]), int(a[5]),
                                 int(a[6])))
            p = float(str(k[2] - k[1]).split(':')[-1])
            if p < k[0]:
                tasks_executed_on_time += 1
                timely_[a[7]] += 1
            else:
                tasks_not_executed_on_time += 1
                untimely_[a[7]] += 1
        elif len(k) == 3:
            a = received_task[i]
            t = dt.datetime(int(a[0]), int(a[1]),
                            int(a[2]), int(a[3]),
                            int(a[4]), int(a[5]),
                            int(a[6]))
            p = float(str(t - k[1]).split(':')[-1])
            if p < k[0]:
                tasks_executed_on_time += 1
                timely_[a[7]] += 1
            else:
                tasks_not_executed_on_time += 1
                untimely_[a[7]] += 1


def receive_mec_start():
    global task_topic
    global task_client

    username = 'mec'
    password = 'password'
    broker_port_no = 1883
    task_topic = client_id(ip_address())

    task_client = mqtt.Client()
    task_client.on_connect = on_connect_task
    task_client.on_message = on_receive_task

    task_client.username_pw_set(username, password)
    task_client.connect(broker_ip, broker_port_no, 60)

    task_client.loop_forever()


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_hostname():
    cmd = ['cat /etc/hostname']
    hostname = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return hostname


def send_email(msg):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(config.email_address, config.password)
        subject = 'Deadlock results {} {}'.format(filename[algo_id], get_hostname())
        # msg = 'Attendance done for {}'.format(_timer)
        _message = 'Subject: {}\n\n{}\n\n SENT BY RIHANNA \n\n'.format(subject, msg)
        server.sendmail(config.email_address, config.send_email, _message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)


def send_result(host_, data):
    try:
        c = paramiko.SSHClient()

        un = 'mec'
        pw = 'password'
        port = 22

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(host_, port, un, pw)
        for i in data:
            cmd = ('echo "{}" >> /home/mec/result/client_data.py'.format(data))  # task share : host ip task

            stdin, stdout, stderr = c.exec_command(cmd)
        c.close()
    except Exception as e:
        print(e)


def client_id(client_ip):
    _id = client_ip.split('.')[-1]
    if len(_id) == 1:
        return '00' + _id
    elif len(_id) == 2:
        return '0' + _id
    else:
        return _id


total_task_sent = 0
total_split_task = 0
task_dist = {1: 0, 2: 0, 3: 0}


def task_details(tasks):
    global task_dist, total_task_sent, total_split_task
    total_task_sent += len(tasks)
    for task in tasks:
        total_split_task += tasks[task]['wcet']
        task_dist[tasks[task]['wcet']] += 1


def name_task(task_list, node_id, seq_no):
    # naming nomenclature of tasks = task_id.node_id.client_id.sequence_no  =>t2.110.170.10
    # returns task list and waiting_time with proper identification
    return {i + '.' + str(node_id) + '.' + client_id_ + '.' + str(seq_no): task_list[0][i] for i in task_list[0]}, \
           {k + '.' + str(node_id) + '.' + client_id_ + '.' + str(seq_no): task_list[1][k] for k in task_list[1]}


def namestr(obj):
    namespace = globals()
    return [name for name in namespace if namespace[name] is obj]


def split_list(data, _id_):
    # host_sp = {3: 1, 4: 2, 5: 3}
    if _id_ == 4:
        return data[:600]
    if _id_ == 5:
        return data[600:1200]
    if _id_ == 6:
        return data[1200:]


def save_data():
    result = f"\ntimely{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {tasks_executed_on_time} " \
             f"\nuntimely{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {tasks_not_executed_on_time}" \
             f"\nrecord{len(hosts)} = {record} \nhost_names{len(hosts)} = {host_dict}" \
             f"\n{namestr(total_task_sent)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {total_task_sent}" \
             f"\n{namestr(total_split_task)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = " \
             f"{total_split_task} " \
             f"\n{namestr(task_dist)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {task_dist}\n" \
             f"\n{namestr(untimely_)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {untimely_}" \
             f"\n{namestr(timely_)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {timely_}"
    list_result = [
        f"\ntimely{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {tasks_executed_on_time} ",
        f"\nuntimely{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {tasks_not_executed_on_time}",
        f"\nrecord{len(hosts)} = {record} ",
        f"\nhost_names{len(hosts)} = {host_dict}",
        f"\n{namestr(total_task_sent)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {total_task_sent}"
        f"\n{namestr(total_split_task)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = "
        f"{total_split_task} "
        f"\n{namestr(task_dist)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {task_dist}\n",
        f"\n{namestr(timely_)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {timely_}",
        f"\n{namestr(untimely_)[0]}{get_hostname()[-1]}_{algo_id}_{len(hosts)} = {untimely_}"
    ]
    path_ = 'data/raw/'
    if os.path.exists(path_):
        cmd = f"echo '' > {path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datal.py"
        os.system(cmd)
        cmd = f"echo '' > {path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datap.py"
        os.system(cmd)

    else:
        os.mkdir(path_)
        cmd = f"echo '' > {path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datal.py"
        os.system(cmd)
        cmd = f"echo '' > {path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datap.py"
        os.system(cmd)
    file_ = open(f'{path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datap.py', 'w')
    for i in list_result:
        cmd = f'echo "{i}" >> {path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datal.py'
        os.system(cmd)
        file_.write(i)
    file_.close()
    sp.run(
        ["scp", f"{path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datap.py",
         f"mec@{ho['osboxes-0']}:/home/mec/result/python"])
    sp.run(
        ["scp", f"{path_}c{get_hostname()[-1]}_{algo_id}_{len(hosts)}datal.py",
         f"mec@{ho['osboxes-0']}:/home/mec/result/linux"])
    # send_result(ho['osboxes-0'], result)
    send_email(result)


def main():
    global record
    global client_id_
    global seq

    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    get_mec_details()
    client_id_ = client_id(ip_address())
    '''
    thread_record.append(Thread(target=receive_tasks))
    thread_record[-1].daemon = True
    thread_record[-1].start()
    '''
    redeem_task = Thread(target=receive_mec_start)
    redeem_task.daemon = True
    redeem_task.start()
    while True:
        time.sleep(1)
        if len(hosts) > 0:
            break
    print('Client is connected to servers: {}'.format(hosts))
    data = {4: dst.mec4, 5: dst.mec5, 6: dst.mec6, 7: dst.mec7}
    cmd = ['hostname']
    host_id = str(sp.check_output(cmd, shell=True), 'utf-8')[-2]
    while True:
        try:
            x = input('Enter "y" to start and "stop" to exit: ').strip().lower()
            _data_ = split_list(data[len(hosts)], int(host_id))
            if x == 'y':
                for i in range(len(_data_)):
                    seq = i
                    rand_host = hosts[int(_data_[i]) - 1]  # host selection using generated gausian distribution
                    _task_ = get_tasks()  # tasks, waiting time
                    _tasks_list = name_task(_task_, client_id(rand_host), i)  # id's tasks => ({tasks}, {waiting time})
                    task_details(_tasks_list[0])
                    record.append([_tasks_list, host_dict[rand_host]])
                    for task in _tasks_list[0]:
                        if i not in task_record:  # task_record= {seq_no:{task:[duration,start_time,finish_time]}}
                            task_record[i] = {task: [_task_[1][task[:2]][1], get_time()]}
                        else:
                            task_record[i][task] = [_task_[1][task[:2]][1], get_time()]
                    # client(_tasks_list, rand_host)
                    task_client.publish(client_id(rand_host), "t {}".format(_tasks_list))
                    print("Sent {} to {} node_id {} \n\n".format(_tasks_list, rand_host, client_id(rand_host)))
                    drawnow(plot_performance)
                    time.sleep(3)
            elif x == 'stop':
                print('\nProgramme terminated')
                print('MEC: ', ho['osboxes-0'])
                save_data()

                task_client.loop_stop()
                print('done')
                time.sleep(1)
                break

        except KeyboardInterrupt:
            print('\nProgramme terminated')
            task_client.loop_stop()
            break


if __name__ == "__main__":
    main()
