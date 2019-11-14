import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)
width = 0.35
title = {2}
time_av_t = {'_4_2': 6760,
             '_5_2': 10565,
             '_6_2': 10722,
             '_7_2': 10940,

             '_4_3': 9510,
             '_5_3': 10456,
             '_6_3': 10577,
             '_7_3': 10616,

             '_4_7': 7494,
             '_5_7': 8928,
             '_6_7': 10991,
             '_7_7': 11118,

             '_4_10': 9843,
             '_5_10': 10829,
             '_6_10': 10714,
             '_7_10': 11099,

             '_4_12': 9626,
             '_5_12': 10506,
             '_6_12': 10579,
             '_7_12': 10542,

             '_4_16': 8264,
             '_5_16': 9110,
             '_6_16': 9758,
             '_7_16': 9710, }

time_av_u = {
    '_4_2': 3708,
    '_5_2': 190,
    '_6_2': 181,
    '_7_2': 116,

    '_4_3': 965,
    '_5_3': 576,
    '_6_3': 299,
    '_7_3': 168,

    '_4_7': 2998,
    '_5_7': 1910,
    '_6_7': 153,
    '_7_7': 41,

    '_4_10': 665,
    '_5_10': 176,
    '_6_10': 128,
    '_7_10': 73,

    '_4_12': 839,
    '_5_12': 572,
    '_6_12': 291,
    '_7_12': 217,

    '_4_16': 2209,
    '_5_16': 1747,
    '_6_16': 1298,
    '_7_16': 1053
}


def percent(value, total):
    if value > 0:
        return round((value / total) * 100, 2)
    else:
        return 0


def histogram(timely, untimely, ax, no):
    ind = np.arange(len(timely))
    p1 = ax.bar(ind, untimely, width, color='r', alpha=0.4)
    p2 = ax.bar(ind, timely, width, color='g', bottom=untimely, alpha=0.4)
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
        ax.text(j, timely[j] + untimely[j], '{}%'.format(percent(i, total)), rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
        ax.text(j, untimely[j], '{}%'.format(percent(untimely[j], total)), rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax.legend((p1[0], p2[0]), ('Untimely', 'Timely'))
    # ax.set_ylabel('\n'.join(wrap(f'Plot for {no} MECs', 8))).set_rotation(0)
    ax.set_ylabel('\n'.join(wrap(f'{no} MECs', 8)), rotation=0, fontsize=15, labelpad=30)


def format_data():
    t_data = {}
    u_data = {}
    _keys = list(time_av_t.keys())
    s4 = 0
    s5 = 1
    s6 = 2
    s7 = 3
    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(time_av_t[j])
                u_data[4].append(time_av_u[j])
                s4 += 4
            else:
                t_data[4] = [time_av_t[j]]
                u_data[4] = [time_av_u[j]]
                s4 += 4
        elif i == s5:
            if 5 in t_data:
                t_data[5].append(time_av_t[j])
                u_data[5].append(time_av_u[j])
                s5 += 4
            else:
                t_data[5] = [time_av_t[j]]
                u_data[5] = [time_av_u[j]]
                s5 += 4
        elif i == s6:
            if 6 in t_data:
                t_data[6].append(time_av_t[j])
                u_data[6].append(time_av_u[j])
                s6 += 4
            else:
                t_data[6] = [time_av_t[j]]
                u_data[6] = [time_av_u[j]]
                s6 += 4
        elif i == s7:
            if 7 in t_data:
                t_data[7].append(time_av_t[j])
                u_data[7].append(time_av_u[j])
                s7 += 4
            else:
                t_data[7] = [time_av_t[j]]
                u_data[7] = [time_av_u[j]]
                s7 += 4

    return t_data, u_data


def plot_av_times():
    axes = {ax1: 4, ax2: 5, ax3: 6, ax4: 7}
    _data = format_data()
    # print(_data)
    for i in axes:
        histogram(_data[0][axes[i]], _data[1][axes[i]], i, axes[i])
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.show()


plot_av_times()

