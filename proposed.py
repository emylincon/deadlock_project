from functools import reduce
from sys import *
import numpy as np
import random as r
import psutil
import ping_code as pc

tasks = {'t1': {'wcet': 3, 'period': 20},
         't2': {'wcet': 2, 'period': 5},
         't3': {'wcet': 2, 'period': 10}
         }
# mat = {'p0': ['cpu', 'mem', 'storage']}
_need = {
    't1': [7, 4, 3],
    't2': [1, 2, 2],
    't3': [6, 0, 0],
    'p3': [0, 1, 1],
    'p4': [4, 3, 1]

}
allocation = {
    't1': [0, 1, 0],
    't2': [2, 0, 0],
    't3': [3, 0, 2],
    'p3': [2, 1, 1],
    'p4': [0, 0, 2]
}

t_time = {i:[round(r.uniform(0.4, 0.8), 3), round((tasks[i]['period'])/(tasks[i]['wcet']), 3)] for i in tasks}  # t_time = {'ti': [execution_time, latency], ..}

mec_waiting_time = {}   # {ip : [moving (waiting time + rtt)]}


def get_rtt(host):
    rtt = pc.verbose_ping(host)

    return rtt


def get_waiting_time():
    pass

    return waiting_time


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def LCM(list):
    return reduce(lcm, list)


def load_tasks():
    global tasks

    period_list = [tasks[i]['period'] for i in tasks]

    lcm_period = LCM(period_list)
    # insert idle task
    tasks['idle'] = {'wcet': lcm_period, 'period': lcm_period + 1}
    return lcm_period


def scheduler(D):
    queue = list(tasks.keys())  # initialize task queue
    schedule = []
    rms = []
    curr = ''  # current task
    prev = ''  # previous task
    tmp = {}
    for task in tasks.keys():
        tmp[task] = {}  # temporary data for each task
        tmp[task]['deadline'] = tasks[task]['period']
        tmp[task]['executed'] = 0

    # start scheduling...
    # proceed by one timestamp to handle preemption
    for time in range(D):
        # insert new tasks into the queue
        for t in tmp.keys():
            if time == tmp[t]['deadline']:
                if tasks[t]['wcet'] > tmp[t]['executed']:
                    # print('Scheduling Failed at %d' % time)
                    exit(1)
                else:
                    tmp[t]['deadline'] += tasks[t]['period']
                    tmp[t]['executed'] = 0
                    queue.append(t)
        # select next task to be scheduled
        min = D * 2
        for task in queue:
            if tmp[task]['deadline'] < min:
                min = tmp[task]['deadline']
                curr = task
        tmp[curr]['executed'] += 1
        # print(time, queue, curr)

        # dequeue the execution-completed task
        if tmp[curr]['executed'] == tasks[curr]['wcet']:
            for i in range(len(queue)):
                if curr == queue[i]:
                    del queue[i]
                    break

        # record to the schedule trace
        if prev != curr:
            if prev in queue and prev != 'idle':  # previous task is preempted..
                s = schedule.pop()
                schedule.append([s[0], s[1], '*'])
                rms.append(s[1])
            schedule.append([time, curr])
            if curr != 'idle': rms.append(curr)
        prev = curr

    return rms


def get_rms():
    a = load_tasks()
    return scheduler(a)


# safe state or not
def isSafe(processes, avail, need, allot):

    # Mark all processes as infinish
    finish = [0] * P

    # To store safe sequence
    safeSeq = [0] * P

    # Make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

        # While all processes are not finished
    # or system is not in safe state.
    count = 0
    while (count < P):

        # Find a process which is not finish
        # and whose needs can be satisfied
        # with current work[] resources.
        found = False
        for p in range(P):

            # First check if a process is finished,
            # if no, go for next condition
            if (finish[p] == 0):

                # Check if for all resources
                # of current P need is less
                # than work
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break

                # If all needs of p were satisfied.
                if (j == R - 1):

                    # Add the allocated resources of
                    # current P to the available/work
                    # resources i.e.free the resources
                    for k in range(R):
                        work[k] += allot[p][k]

                        # Add this process to safe sequence.
                    safeSeq[count] = processes[p]
                    count += 1

                    # Mark this p as finished
                    finish[p] = 1

                    found = True

        # If we could not find a next process
        # in safe sequence.
        if (found == False):
            print("System is not in safe state")
            return False

    # If system is in safe state then
    # safe sequence will be as below
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return safeSeq


def get_safe_seq(pro):
    global P
    global R

    # Number of processes
    P = len(pro)

    # Number of resources
    R = 3
    processes = [f'{pro[i]}_{i}' for i in range(len(pro))]

    # Available instances of resources
    avail = [3, 5, 3]
    n_need = [_need[i] for i in pro]
    # print('need', n_need)
    # Resources allocated to processes
    allot = [allocation[i] for i in pro]
    # print('allocation', allot)

    # Maximum R that can be allocated
    # to processes
    maxm = [np.array(allot[i]) + np.array(n_need[i]) for i in range(len(n_need))]
    # print('max_matrix:', maxm)


    # Check system is in safe state or not
    return isSafe(processes, avail, n_need, allot)


def calc_wait_time(list_seq):
    pre = 0
    time_dic = {}
    for i in list_seq:
        time_dic[i] = round(t_time[i[:2]][0] + pre, 3)
        pre += t_time[i[:2]][0]
    return time_dic


def compare_local_mec(list_seq):
    time_compare_dict = {i: t_time[i[:2]][1] > list_seq[i] for i in list_seq}
    print('local vs MEC comparison: ', time_compare_dict)
    execute_mec = []
    execute_locally = []
    for i in time_compare_dict:
        if time_compare_dict[i]:
            execute_locally.append(i)
        else:
            execute_mec.append(i)

    return execute_mec, execute_locally


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


def run_me():
    print('Running RMS on Tasks: ', tasks, '\n')
    rms_list = get_rms()
    print('RMS List of Processes: ', rms_list, '\n')
    print('\nRunning Bankers Algorithm')
    list_seq = get_safe_seq(rms_list)
    wait_list = calc_wait_time(list_seq)
    print('\nWaiting Time List: ', wait_list)
    compare_result = compare_local_mec(wait_list)
    print('\nExecute Locally: ', compare_result[1])
    print('\nExecute in MEC: ', compare_result[0])



run_me()