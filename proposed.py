from functools import reduce
from sys import *
import numpy as np


# mat = {'p0': ['cpu', 'mem', 'storage']}
need = {
    'p0': [7, 4, 3],
    'p1': [1, 2, 2],
    'p2': [6, 0, 0],
    'p3': [0, 1, 1],
    'p4': [4, 3, 1]

}
allocation = {
    'p0': [0, 1, 0],
    'p1': [2, 0, 0],
    'p2': [3, 0, 2],
    'p3': [2, 1, 1],
    'p4': [0, 0, 2]
}
work = ['p0', 'p1', 'p2', 'p3', 'p4']
available = [3, 3, 2]
safe_sequence = []


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
                    print('Scheduling Failed at %d' % time)
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
        print(time, queue, curr)

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
    s = scheduler(a, b)

