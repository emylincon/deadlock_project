from functools import reduce
from sys import *
import numpy as np


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


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def LCM(list):
    return reduce(lcm, list)


def load_tasks():

    tasks = {'t1': {'wcet': 3, 'period': 20},
             't2': {'wcet': 2, 'period': 5},
             't3': {'wcet': 2, 'period': 10}
             }
    period_list = [tasks[i]['period'] for i in tasks]

    lcm_period = LCM(period_list)
    # insert idle task
    tasks['idle'] = {'wcet': lcm_period, 'period': lcm_period + 1}
    return tasks, lcm_period


def scheduler(tasks, D):
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
    a, b = load_tasks()
    return scheduler(a, b)


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
    print('n_p: ', P)
    print('p: ', pro)

    # Number of resources
    R = 3
    processes = [f'{pro[i]}_{i}' for i in range(len(pro))]

    # Available instances of resources
    avail = [5, 5, 5]
    n_need = [_need[i] for i in pro]
    print('need', n_need)
    # Resources allocated to processes
    allot = [allocation[i] for i in pro]
    print('allocation', allot)

    # Maximum R that can be allocated
    # to processes
    maxm = [np.array(allot[i]) + np.array(n_need[i]) for i in range(len(n_need))]
    print('max_matrix:', maxm)


    # Check system is in safe state or not
    return isSafe(processes, avail, n_need, allot)


def run_me():
    rms_list = get_rms()
    print(rms_list)
    print(get_safe_seq(rms_list))


run_me()