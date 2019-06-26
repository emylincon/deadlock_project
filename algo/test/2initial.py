# random => sample of deadline and capacity
# random put task in queue
# from queue choose period

import random as ra
import matplotlib.pyplot as plt
import numpy as np
import time

task_list = []
task_queue = []
d_task = {} # task_id: period


def ghosh_dist(a,b):
    if a == b:
        return a
    else:
        return int(a+int(np.random.lognormal(ra.randint(0,100),ra.randint(1,100)))%(b-a))


def plot_me():
    temp=[]
    for i in d_task:
        plt.plot(d_task[i],':o' ,label='task_'+str(i)+ \
                                       'period : '+str(round(sum(d_task[i])/len(d_task[i]),3))+ \
                                       ' | Variance : '  + str(round(np.var(d_task[i]),3)))
    plt.legend()
    plt.show()


def gen_task(c_lim, d_lim):
    c=ghosh_dist(1, c_lim)
    return (int(len(task_list)), c,
            c + ra.randint(int((d_lim-c_lim) / 2), d_lim - c_lim))


def sel_task():
    if ra.randint(0,133331)%2 == 0:
        return task_list[ghosh_dist(0,len(task_list)-1)]
    else:
        return task_list[ra.randint(0, len(task_list) - 1)]


def main():
    for i in range(10):
        while True:
            c=ra.randint(2,6)
            d=ra.randint(6,30)
            if c!=d:
                break

        if d > c:
            print(f'c={c}, d={d} req ')
            r=gen_task(c,d)
            task_list.append(r)
            print(f'\t id={r[0]}, c={r[1]}, d={r[2]}\n')

    select_task()

    '''
    for i in task_queue:
        print(i)
    '''
    print('Tasks: \t', task_list)
    print(task_queue)
    plot_me()


def task_buffer():
    t_buffer = []
    for i in range(6):
        t = ra.randrange(len(task_list))
        t_buffer.append(task_list[t])
    return t_buffer


def cal_period(tim, ca, freq):
    return round((tim+ca)/freq, 3)


def select_task():
    i = 0
    _time = 1
    fre = {}  # task: freq
    while i < 1000:
        tas = task_buffer()
        for j in range(ra.randrange(57)):

            t = tas[ra.randint(0, len(tas) - 1)]
            if t[0] not in d_task.keys():
                d_task[t[0]]=[cal_period(_time, t[1], 1)]
                i += 1
                _time += t[1]
                fre[t[0]] = 2
            else:
                d_task[t[0]].append(cal_period(_time, t[1], fre[t[0]]))
                i += 1
                _time += t[1]
                fre[t[0]] += 1
            task_queue.append((t[0], t[1], d_task[t[0]][-1], t[2]))
            if i == 1000:
                break


def fetching_task():
    global task_queue

    while len(task_queue) > 0:
        u = ra.randrange(2, 5)
        t = task_queue[:u]
        task_queue = task_queue[u:]
        task = {}
        for i in t:
            task['t' + str(i[0]) + '_{}'.format(t.index(i))] = {'wcet': i[1], 'period': i[2], 'deadline': i[3]}
        print('task: ', task)
        _t = ra.randrange(2, 5)
        time.sleep(_t)


main()

fetching_task()

# finish this