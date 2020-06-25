import algorithms.graphical.algo_one as a1
import algorithms.graphical.algo_two as a2
import algorithms.graphical.algo_three as a3
import algorithms.graphical.algo_four as a4
import algorithms.graphical.algo_five as a5
import algorithms.graphical.algo_six as a6
import paho.mqtt.client as mqtt
import pickle
import subprocess as sp
import time
import random as r
import socket
import os
from threading import Thread
from drawnow import *
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)


style1 = [{'color': 'g', 'marker': '^'}, {'color': 'aqua', 'marker': '*'}, {'color': 'purple', 'marker': 'X'},
          {'color': 'r', 'marker': 'v'}, {'color': 'k', 'marker': '>'}, {'color': 'brown', 'marker': 'D'},
          {'color': 'b', 'marker': 's'}, {'color': 'c', 'marker': '1'}, {'color': 'olive', 'marker': 'p'},]


def percent(value, total):
    if value > 0:
        return round((value/total)*100, 2)
    else:
        return 0

# Plot me


def plot_offloaded_remote():
    keys = ['O-Out', 'Cloud', 'Local', 'O-In']
    total = running_algo._off_mec + running_algo._off_cloud + running_algo._loc + running_algo._inward_mec

    val = [percent(running_algo._off_mec, total),
           percent(running_algo._off_cloud, total),
           percent(running_algo._loc, total),
           percent(running_algo._inward_mec, total)]
    cols = ['r', 'g', 'b', 'm']
    ypos = ([0, 1, 2, 3])

    values = [running_algo._off_mec, running_algo._off_cloud, running_algo._loc, running_algo._inward_mec]
    for i in values:
        j = values.index(i)
        ax2.text(j-0.1, values[j], '{}%'.format(val[j]), rotation=0,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax2.set_xticks(ypos)
    ax2.set_xticklabels(keys)
    ax2.bar(ypos, values, align='center', color=cols, alpha=0.3)
    ax2.set_title('Local/Remote Execution Report')
    plt.subplot(ax2)

# color=color_code[list(hosts.values()).index(i)]


def plot_deadlock():
    # cols = ['r']
    text = str(running_algo.deadlock[-1] - 1) + " Deadlock Resolved"
    '''
    wedges, texts, autotexts = ax5.pie(deadlock, shadow=True, autopct=text,
                                       textprops=dict(rotation_mode='anchor', color="w", ha='left'), colors=cols)
    plt.setp(autotexts, size=9, weight="bold")
    '''
    ax5.text(0.5, 0.6, text, rotation=0, size=10,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.)))
    ax5.text(0.5, 0.45, '{} Tasks Received'.format(running_algo._loc+running_algo._inward_mec), rotation=0, size=10,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
    # ax5.set_title("Deadlock Resolved Counter")
    ax5.set_axis_off()
    plt.subplot(ax5)


def _mov_avg(a1):
    ma1 = []   # moving average list
    avg1 = 0   # moving average pointwise
    count = 0
    for i in range(len(a1)):
        count += 1
        avg1 = ((count-1)*avg1+a1[i])/count
        ma1.append(round(avg1, 4))    # cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def plot_memory():

    memory = running_algo.memory
    ax6.grid(True)
    ax6.plot(list(range(len(_mov_avg(memory)))), _mov_avg(memory), linewidth=2, label='Memory', color='m')
    # ax6.set_title('Moving Memory Utilization')
    ax6.set_ylabel('Moving Memory')
    ax6.set_xlabel('Time (seconds)')
    ax6.fill_between(list(range(len(_mov_avg(memory)))), _mov_avg(memory), 0, alpha=0.5, color='m')
    ax6.legend()
    plt.subplot(ax6)


def plot_wait_time():
    ax1.grid(True)

    for i in running_algo.mec_waiting_time:
        mv = _mov_avg(running_algo.mec_waiting_time[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        d = list(range(len(mv)))
        ptx = d[0:len(d):int((len(d) / 7)) + 1]
        if ptx[-1] != d[-1]:
            ptx.append(d[-1])
        if len(ptx) > len(pt):
            ptx=ptx[:-1]
        elif len(ptx) < len(pt):
            pt=pt[:-1]
        ax1.plot(ptx,
                 pt,
                 **style1[list(running_algo.hosts.values()).index(i)],
                 linestyle=(0, (3, 1, 1, 1, 1, 1)),
                 linewidth=2,
                 label=i)
    ax1.set_title('Waiting Time Queue')
    ax1.set_ylabel('Moving Wait + RTT')
    # ax2.set_xlabel('Time (seconds)')
    ax1.legend()
    plt.subplot(ax1)


def plot_rtts():
    ax3.grid(True)
    for i in running_algo.mec_rtt:
        mv = _mov_avg(running_algo.mec_rtt[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        d = list(range(len(mv)))
        ptx = d[0:len(d):int((len(d) / 7)) + 1]
        if ptx[-1] != d[-1]:
            ptx.append(d[-1])
        if len(ptx) > len(pt):
            ptx=ptx[:-1]
        elif len(ptx) < len(pt):
            pt=pt[:-1]
        ax3.plot(ptx,
                 pt,
                 **style1[list(running_algo.hosts.values()).index(i)],
                 linestyle=(0, (3, 1, 1, 1, 1, 1)),
                 linewidth=2,
                 label=i)
    ax3.set_title('RTT Utilization over Time')
    ax3.set_ylabel('Moving RTT')
    # ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


def plot_cpu():

    # plot graph
    ax4.grid(True)
    ax4.plot(list(range(len(_mov_avg(running_algo._cpu)))), _mov_avg(running_algo._cpu), linewidth=2, label='CPU')
    # ax4.set_title('Moving CPU Utilization')
    ax4.set_ylabel('Moving CPU')
    ax4.set_xlabel('Time (seconds)')
    ax4.fill_between(list(range(len(_mov_avg(running_algo._cpu)))), _mov_avg(running_algo._cpu), 0, alpha=0.5)
    ax4.legend()
    plt.subplot(ax4)


def plot_graphs():
    plot_offloaded_remote()
    plot_wait_time()
    plot_rtts()
    plot_cpu()
    plot_deadlock()
    plot_memory()
    fig.suptitle('MEC Performance During Deadlock Experiment')


def show_graphs():
    print('showing graphs')
    drawnow(plot_graphs)


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
    global plot

    algos = {1: a1, 2: a2, 3: a3, 4: a4, 5: a5, 6: a6}
    plot = 1
    running_algo = algos[algo_no]
    algos[algo_no].run_me(mec_no_=no_mec, hosts_=hosts, cloud_ip_=cloud_ip,  send_path=send_path, broker_ip_=ip)

    time.sleep(r.uniform(1, 10))
    plot = 0

    messenger.publish(control_topic, pickle.dumps(['stop', ip_address()]))   # publishes to control they stopped


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


plot = 0


def starter():
    global messenger
    global control_topic
    global msg_thread

    os.system('clear')
    control_topic = 'control/control'
    broker_dict = {'user': 'mec', 'pw': 'password', 'ip': '192.168.122.111',
                   'sub_topic': 'control/mec'}
    messenger = BrokerCom(**broker_dict)

    msg_thread = Thread(target=messenger.broker_loop)
    msg_thread.start()
    time.sleep(4)
    about = ['about', {host_id: ip_address()}]
    messenger.publish(control_topic, pickle.dumps(about))
    print(f'about sent: {about}')
    while True:
        try:
            if plot == 1:
                show_graphs()
                time.sleep(3)
            else:
                time.sleep(3)
        except KeyboardInterrupt:
            print('killed')
            break


if __name__ == '__main__':
    try:
        starter()
    except KeyboardInterrupt:
        messenger.run = 0
        msg_thread.join()