import numpy as np

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
_available = [10, 5, 7]
safe_sequence = []  # [p1,p3,p4,p0,p2]


def main():
    processes = len(work)
    resources = len(_available)
    max_resources = _available

    "-- allocated resources for each process --"
    currently_allocated = [allocation[i] for i in allocation]

    "-- maximum resources for each process --"
    max_need = [np.array(allocation[i]) + np.array(need[i]) for i in need]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\ntotal allocated resources : {allocated}")

    available = np.array(max_resources) - np.array(allocated)
    print(f"total available resources : {available}\n")

    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} is executing")
                    safe_sequence.append(work[i])
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("the processes are in an unsafe state.")
            break

        print(f"the process is in a safe state.\navailable resources : {available}\n")


if __name__ == '__main__':
    main()
    print(f'safe_seq = {safe_sequence}')