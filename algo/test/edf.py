from functools import reduce

# tasks = {ti: [capacity, deadline, period]}
tasks = {
    't1': [3, 7, 20],
    't2': [2, 4, 5],
    't3': [2, 8, 10],
}


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def _lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm(_list):
    return reduce(_lcm, _list)


def edf():
    t_lcm = lcm([tasks[i][-1] for i in tasks])

    t_dead = {i: tasks[i][1] for i in tasks}

    sorted_dead = sorted(t_dead.items(), key=lambda kv: (kv[1], kv[0]))
    # print(sorted_dead)

    ready_task = []
    for i in sorted_dead:
        period = tasks[i[0]][-1]
        # print('lcm: ', t_lcm, ' period: ', period)
        t_range = int(t_lcm/period)
        last_dead = 0
        for j in range(t_range):
            ready_task.append((i[0], last_dead+tasks[i[0]][1]))
            last_dead += period

    ready_task = sorted(ready_task, key=lambda t: t[1])
    # print(ready_task)

    t_time = 0
    schedule = []
    register = {i: 0 for i in tasks.keys()}   # {ti : amount executed}
    for i in ready_task:
        if (t_time//tasks[i[0]][-1])+1 <= register[i[0]]:
            while (t_time//tasks[i[0]][-1])+1 <= register[i[0]]:
                t_time += 1
                schedule.append(('idle', t_time))
        if (t_time//tasks[i[0]][-1])+1 > register[i[0]]:
            if t_time + tasks[i[0]][0] <= i[1]:
                register[i[0]] += 1
                t_time += tasks[i[0]][0]
                schedule.append((i[0], t_time))
            else:
                print('Deadline missed: ', i)

    print('s: ', schedule)
    print('r: ', register)


if __name__ == '__main__':
    edf()
