import numpy as np

# mat = {'p0': ['cpu', 'mem', 'storage']}
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


banker()
