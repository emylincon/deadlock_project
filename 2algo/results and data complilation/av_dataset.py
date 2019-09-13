import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
width = 0.35
title = {2}
time_av_t = {'_4_2': 10374,
             '_5_2': 10861,
             '_6_2': 11052,

             '_4_3': 6465,
             '_5_3': 8200,
             '_6_3': 10791,

             '_4_7': 10329,
             '_5_7': 10951,
             '_6_7': 10136,

             '_4_10': 6721,
             '_5_10': 7418,
             '_6_10': 10913,

             '_4_12': 9172,
             '_5_12': 10441,
             '_6_12': 9618,

             '_4_16': 8364,
             '_5_16': 9225,
             '_6_16': 8536,

             }
time_av_u = {
    '_4_2': 544,
    '_5_2': 211,
    '_6_2': 111,

    '_4_3': 4479,
    '_5_3': 2898,
    '_6_3': 165,

    '_4_7': 580,
    '_5_7': 218,
    '_6_7': 919,

    '_4_10': 4193,
    '_5_10': 3743,
    '_6_10': 170,

    '_4_12': 1717,
    '_5_12': 651,
    '_6_12': 1337,

    '_4_16': 2527,
    '_5_16': 1855,
    '_6_16': 2396

}


def percent(value, total):
    if value > 0:
        return round((value/total)*100, 2)
    else:
        return 0


def histogram(timely, untimely, ax):
    ind = np.arange(len(timely))
    p1 = ax.bar(ind, untimely , width)
    p2 = ax.bar(ind, timely , width, bottom=untimely)
    ax.set_xticks(ind)
    ax.set_xticklabels(('RMS + Bankers',
                        'EDF + Bankers',
                        'RMS + wound wait',
                        'RMS + wait die',
                        'EDF + wound wait',
                        'EDF + wait die'))
    for i in timely:
        j = timely.index(i)
        total = i + untimely[j]
        ax.text(j, timely[j]+untimely[j], '{}%'.format(percent(i, total)), rotation=0,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
        ax.text(j, untimely[j], '{}%'.format(percent(untimely[j], total)), rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax.legend((p1[0], p2[0]), ('Untimely', 'Timely'))


def format_data():
    t_data = {}
    u_data = {}
    _keys = list(time_av_t.keys())
    s4 = 0
    s5 = 1
    s6 = 2
    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(time_av_t[j])
                u_data[4].append(time_av_u[j])
                s4 += 3
            else:
                t_data[4] = [time_av_t[j]]
                u_data[4] = [time_av_u[j]]
                s4 += 3
        elif i == s5:
            if 5 in t_data:
                t_data[5].append(time_av_t[j])
                u_data[5].append(time_av_u[j])
                s5 += 3
            else:
                t_data[5] = [time_av_t[j]]
                u_data[5] = [time_av_u[j]]
                s5 += 3
        elif i == s6:
            if 6 in t_data:
                t_data[6].append(time_av_t[j])
                u_data[6].append(time_av_u[j])
                s6 += 3
            else:
                t_data[6] = [time_av_t[j]]
                u_data[6] = [time_av_u[j]]
                s6 += 3

    return t_data, u_data

            
def plot_av_times():
    axes = {ax1: 4, ax2: 5, ax3: 6}
    _data = format_data()
    for i in axes:
        histogram(_data[0][axes[i]], _data[1][axes[i]], i)
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.show()


plot_av_times()