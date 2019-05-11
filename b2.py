# Python3 program to illustrate
# Banker's Algorithm
import numpy as np

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

    return True


# Driver code
if __name__ == "__main__":
    processes = ['p0', 'p1', 'p2', 'p3', 'p4']

    # Available instances of resources
    avail = [3, 3, 2]

    # Maximum R that can be allocated
    # to processes
    maxm = [np.array(allocation[i]) + np.array(_need[i]) for i in _need]

    # Resources allocated to processes
    allot = [allocation[i] for i in allocation]

    # Check system is in safe state or not
    isSafe(processes, avail, maxm, allot)
