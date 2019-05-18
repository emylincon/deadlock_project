import numpy as np
import psutil
import time
import subprocess as sp
from threading import Thread
import matplotlib.pyplot as plt

# mat = {'p0': ['cpu', 'mem', 'storage']}
cpu = []
store = []
mem = []

need = {
    'p0': [0, 1, 0, 0],
    'p1': [0, 4, 2, 1],
    'p2': [1, 0, 0, 1],
    'p3': [0, 0, 2, 0],
    'p4': [0, 6, 4, 2]

}
allocation = {
    'p0': [0, 1, 1, 0],
    'p1': [1, 2, 3, 1],
    'p2': [1, 3, 6, 5],
    'p3': [0, 6, 3, 2],
    'p4': [0, 0, 1, 4]
}
work = ['p0', 'p1', 'p2', 'p3', 'p4']
available = [1, 5, 2, 0]
safe_sequence = []  # [p1,p3,p4,p0,p2]


def banker():
    global available
    global need
    global safe_sequence
    j = 0  # keeping index
    while len(work) > 0:
        i = work[j]  # process of jth index
        # if np.array_equal(np.maximum(available, need[i]), available) == True:
        if not (False in list(np.greater_equal(available, need[i]))):
            available = np.add(available, allocation[i])
            safe_sequence.append(i)
            work.remove(i)
            if j == len(work):  # if last element is removed, index decreases
                j = 0
        else:
            j = (j + 1) % len(work)

    # safe seq
    s_seq = ''
    for i in range(len(safe_sequence)):
        if i != (len(safe_sequence) - 1):
            s_seq += f'{safe_sequence[i]}->'
        else:
            s_seq += f'{safe_sequence[i]}'
    print(s_seq)
    print(need)
    print(list(available))


def get_cpu():
    prev_t = 0
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    #return delta     # Returns CPU util in percentage
    cpu.append(delta)


def get_mem():
    cmd = ['cat /proc/meminfo | grep MemFree |cut -d ":" -f 2 | cut -d "k" -f 1']
    free_mem = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    cmd = [' cat /proc/meminfo | grep MemAva |cut -d ":" -f 2 | cut -d "k" -f 1']
    total_mem = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    mem_util = (int(free_mem.strip())/int(total_mem.strip()))*100
    #return mem_util  # Returns memory util in percentage
    mem.append(mem_util)


def get_storage():
    cmd = ['df -t ext4 | tail -n 2 | head -n 1 | cut -d " " -f 14 | cut -c 1-2']
    storage = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    #return int(storage.strip())  # Returns storage in percentage
    store.append(int(storage.strip()))


def get_resource_util():
    h1 = Thread(target=get_mem)
    h2 = Thread(target=get_cpu)
    h3 = Thread(target=get_storage)

    h1.start()
    h2.start()
    h3.start()


def calculate_mov_avg(a1):
    ma1=[] # moving average list
    avg1=0 # movinf average pointwise
    count=0
    for i in range(len(a1)):
        count+=1
        avg1=((count-1)*avg1+a1[i])/count
        ma1.append(avg1) #cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def plot_resource_util():
    global mem
    global store
    global cpu

    plt.ion()
    plt.grid(True, color='k')
    plt.plot(calculate_mov_avg(cpu), linewidth=5, label='CPU')
    plt.plot(calculate_mov_avg(mem), linewidth=5, label='Memory')
    plt.plot(calculate_mov_avg(store), linewidth=5, label='Storage')
    plt.title('Resource Utilization')
    plt.ylabel('Utilization in percentage')
    plt.xlabel('Time (scale of 2 seconds)')
    plt.legend()
    plt.pause(2)


banker()
