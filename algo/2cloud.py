import numpy as np
import paramiko
import ast
import time
import os
import operator
import socket


_tasks = {'t1': {'wcet': 3, 'period': 20},
          't2': {'wcet': 2, 'period': 5},
          't3': {'wcet': 2, 'period': 10},
          't4': {'wcet': 2, 'period': 6},
          't5': {'wcet': 3, 'period': 15}
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

mec_waiting_time = {}   # {ip : [moving (waiting time + rtt)]}

# offload_register = {}      # {task: host_ip}


# safe state or not
def isSafe(processes, avail, need, allot):
    # tasks to offload if exit
    offload = []

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

            a = list(set(processes) - set(safeSeq) - set(offload))
            _max = np.array([0, 0, 0])
            n = {}
            for i in a:
                n[i] = sum(allocation[i[:2]])
            _max = max(n, key=n.get)
            print('work: ', work, 'need: ', _need[_max[:2]])
            offload.append(_max)
            work = np.array(work) + np.array(allocation[_max[:2]])
            count += 1

            # Mark this p as finished
            finish[processes.index(_max)] = 1
            found = True

    # If system is in safe state then
    # safe sequence will be as below
    if 0 in safeSeq:
        safeSeq = safeSeq[:safeSeq.index(0)]
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    if len(offload) > 0:
        print('|======== Cannot Execute tasks: ', offload, '========|')

    return safeSeq


def get_safe_seq(pro):
    global P
    global R

    # Number of processes
    P = len(pro)

    # Number of resources
    R = 3
    processes = ['{}_{}'.format(pro[i], i) for i in range(P)]

    # Available instances of resources
    avail = [3, 5, 3]
    n_need = [_need[i[:2]] for i in pro]
    # print('need', n_need)
    # Resources allocated to processes
    allot = [allocation[i[:2]] for i in pro]
    # print('allocation', allot)

    # Maximum R that can be allocated
    # to processes
    # maxm = [np.array(allot[i]) + np.array(n_need[i]) for i in range(len(n_need))]
    # print('max_matrix:', maxm)

    # Check system is in safe state or not
    return isSafe(processes, avail, n_need, allot)


def calc_wait_time(list_seq):
    pre = 0
    time_dic = {}
    for i in list_seq:
        time_dic[i] = round(t_time[i[:2]][0] + pre, 3)
        pre += t_time[i[:2]][0]
    w_send = time_dic[list(time_dic.keys())[-1]]
    return time_dic


def compare_local_mec(list_seq):
    time_compare_dict = {i: t_time[i[:2]][1] > list_seq[i] for i in list_seq}
    print('local vs MEC comparison: ', time_compare_dict)
    miss_latency = []
    execute_locally = []
    for i in time_compare_dict:
        if time_compare_dict[i]:
            execute_locally.append(i)
        else:
            miss_latency.append(i)

    return miss_latency, execute_locally


def check_mec_offload():
    global offload_register
    global t_time

    offload_register = {}  # {task: host_ip}
    t_time = {}  # {t1: [execution, latency]}

    try:
        fr = open('/home/mec/temp/task_share.txt', 'r')
        t = fr.readlines()
        for i in t:
            ta = i[:-1].split()[1][:2] + '_' + str(t.index(i))
            offload_register[ta] = i[:-1].split()[0]
            t_time[ta] = ast.literal_eval(''.join(i[:-1].split()[2:]))
        fr.close()
        os.system('rm /home/mec/temp/task_share.txt')
        print('Tasks Offloaded to MEC: {}'.format(t_time.keys()))
    except Exception as e:
        return 0
    return 1


def edf_schedule(tasks_dic):
    t_d = {i: tasks_dic[i][1] for i in tasks_dic}     # {t1: [execution, latency]}

    edf = [i[0] for i in sorted(t_d.items(), key=operator.itemgetter(1))]

    return edf


def execute(local):
    print('\nExecuting :', local)
    send = []
    for i in local:
        i = '_'.join(i.split('_')[:-1])
        time.sleep(t_time[i][0])
        print('####### Executed: ', i)
        if len(i) > 2:
            send.append(i)
    print('============== EXECUTION DONE ===============')
    return send


def _execute(local):
    print('\nExecuting :', local)
    send = []
    for i in local:
        time.sleep(t_time[i][0])
        print('####### Executed: ', i)
        if len(i) > 2:
            send.append(i)
    print('============== EXECUTION DONE ===============')
    return send


def send_back_task(l_list):
    _host_ip = 'Cloud_Server'
    for i in l_list:
        try:
            c = paramiko.SSHClient()

            un = 'mec'
            pw = 'password'
            port = 22

            c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            c.connect(offload_register[i], port, un, pw)
            cmd = ('echo "{} {}" >> /home/mec/temp/executed.txt'.format(i, _host_ip))  # task share : host ip task

            stdin, stdout, stderr = c.exec_command(cmd)
        except Exception as e:
            print(e)


def ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def run_me():
    print('\n========== Deadlock Emulation Program: Cloud Server ===============')
    print('Cloud ip: ', ip_address())
    m = input('Start (Y/N): ').lower()
    if m == 'y':
        print('\n==========* Cloud Server Active *============\n')
        try:
            while True:
                if check_mec_offload() == 0:
                    time.sleep(4)
                elif len(t_time) <= 2:
                    local_ = _execute(list(t_time.keys()))
                    send_back_task(local_)
                    time.sleep(3)
                else:
                    edf_list = edf_schedule(t_time)
                    print('EDF List of Processes: ', edf_list, '\n')
                    print('\nRunning Bankers Algorithm')
                    list_seq = get_safe_seq(edf_list)
                    wait_list = calc_wait_time(list_seq)
                    print('\nWaiting Time List: ', wait_list)
                    compare_result = compare_local_mec(wait_list)
                    if len(compare_result[0]) > 0:
                        for i in compare_result[0]:
                            print(i, 'will miss execution latency deadline')

                    local_ = execute(compare_result[1]+compare_result[0])
                    send_back_task(local_)
                    time.sleep(3)
        except KeyboardInterrupt:
            print('\nProgramme Terminated')
    else:
        print('\nProgramme Terminated')


def main():
    run_me()


if __name__ == "__main__":
    main()