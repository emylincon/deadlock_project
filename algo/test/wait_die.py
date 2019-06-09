# https://www.geeksforgeeks.org/program-bankers-algorithm-set-1-safety-algorithm/
# Python3 program to illustrate
# Banker's Algorithm
import numpy as np
# work = 3 3 2
_need = {
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

# Number of processes
P = len(allocation)

# Number of resources
R = 3


# safe state or not
def isSafe(processes, avail, maxm, allot):
    need = [_need[i] for i in _need]
    offload = []

    # Mark all processes as infinish
    finish = [0] * P

    # To store safe sequence
    exec_seq = []

    # Make a copy of available resources
    work = [0] * len(processes)

    # While all processes are not finished
    # or system is not in safe state.
    while 'w' or 0 in work:
        if 0 in work:
            ind = work.index(0)
            i = processes[ind]
        else:
            ind = work.index('w')
            i = processes[ind]
        print('comparing| process: ', i, _need[i], 'work: ', avail)
        if not (False in list(np.greater_equal(avail, _need[i]))):
            exec_seq.append(i)
            avail = np.add(avail, allocation[i])
            work[ind] = 1

        else:
            a = list(set(processes) - set(exec_seq) - set(offload))
            n = {}
            for j in a:
                n[j] = sum(allocation[j])
            _max = max(n, key=n.get)
            print('work: ', work, 'need: ', _need[_max])
            if processes.index(_max) > processes.index(i):   # if true, i is older
                # wait i
                work[processes.index(i)] = 'w'

            else:
                # abort i
                offload.append(i)
                avail = np.array(avail) + np.array(allocation[i])
                work[processes.index(i)] = 1

            '''
            if not (False in list(np.greater_equal(np.array(avail) + np.array(allocation[_max]), _need[i]))):
                offload.append(_max)
                avail = np.array(avail) + np.array(allocation[_max])
                work[processes.index(_max)] = 1
            else:
                offload.append(i)
                avail = np.array(avail) + np.array(allocation[i])
                work[processes.index(i)] = 1
            '''

    print('seq: ', exec_seq)
    print('offload: ', offload)


# Driver code
if __name__ == "__main__":
    processes = ['p0', 'p1', 'p2', 'p3', 'p4']

    # Available instances of resources
    avail = [3, 1, 2]

    # Maximum R that can be allocated
    # to processes
    maxm = [np.array(allocation[i]) + np.array(_need[i]) for i in _need]

    # Resources allocated to processes
    allot = [allocation[i] for i in allocation]

    # Check system is in safe state or not
    isSafe(processes, avail, maxm, allot)
