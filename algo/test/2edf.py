from functools import reduce

# tasks = {ti: [capacity, deadline, period]}
tasks = {
    't1': {'wcet': 3, 'period': 20, 'deadline': 7},
    't2': {'wcet': 2, 'period': 5, 'deadline': 4},
    't3': {'wcet': 2, 'period': 10, 'deadline': 8},
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
    t_lcm = lcm([tasks[i]['period'] for i in tasks])

    t_dead = {i: tasks[i]['deadline'] for i in tasks}

    sorted_dead = sorted(t_dead.items(), key=lambda kv: (kv[1], kv[0]))
    # print(sorted_dead)

    ready_task = []
    for i in sorted_dead:
        period = tasks[i[0]]['period']
        # print('lcm: ', t_lcm, ' period: ', period)
        t_range = int(t_lcm/period)
        last_dead = 0
        for j in range(t_range):
            ready_task.append((i[0], last_dead+tasks[i[0]]['deadline']))
            last_dead += period

    ready_task = sorted(ready_task, key=lambda t: t[1])
    print(ready_task)

    t_time = 0
    schedule = []
    missed = []
    register = {i: 0 for i in tasks.keys()}   # {ti : amount executed}
    for i in ready_task:
        if (t_time//tasks[i[0]]['period'])+1 <= register[i[0]]:
            while (t_time//tasks[i[0]]['period'])+1 <= register[i[0]]:
                t_time += 1
                schedule.append(('idle', t_time))
        if (t_time//tasks[i[0]]['period'])+1 > register[i[0]]:
            if t_time + tasks[i[0]]['wcet'] <= i[1]:
                register[i[0]] += 1
                t_time += tasks[i[0]]['wcet']
                schedule.append((i[0], t_time))
            else:
                print('Deadline missed: ', i)
                missed.append(i[0])

    print('s (task, execution_time): ', schedule)
    print('r: ', register)
    if len(missed) > 0:
        print('missed deadline: ', missed)
    print(t_time)


if __name__ == '__main__':
    edf()

