import matplotlib.pyplot as plt
import numpy as np
from data_het.client_data import *
from textwrap import wrap

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

width = 0.35
title = {2}
_timely = {
    24: timely4_2_4 + timely5_2_4 + timely6_2_4,
    27: timely4_2_7 + timely5_2_7 + timely6_2_7,
    210: timely4_2_10 + timely5_2_10 + timely6_2_10,

    34: timely4_3_4 + timely5_3_4 + timely6_3_4,
    37: timely4_3_7 + timely5_3_7 + timely6_3_7,
    310: timely4_3_10 + timely5_3_10 + timely6_3_10,

    74: timely4_7_4 + timely5_7_4 + timely6_7_4,
    77: timely4_7_7 + timely5_7_7 + timely6_7_7,
    710: timely4_7_10 + timely5_7_10 + timely6_7_10,

    104: timely4_10_4 + timely5_10_4 + timely6_10_4,
    107: timely4_10_7 + timely5_10_7 + timely6_10_7,
    1010: timely4_10_10 + timely5_10_10 + timely6_10_10,

    124: timely4_12_4 + timely5_12_4 + timely6_12_4,
    127: timely4_12_7 + timely5_12_7 + timely6_12_7,
    1210: timely4_12_10 + timely5_12_10 + timely6_12_10,

    164: timely4_16_4 + timely5_16_4 + timely6_16_4,
    167: timely4_16_7 + timely5_16_7 + timely6_16_7,
    1610: timely4_16_10 + timely5_16_10 + timely6_16_10,

}
_untimely = {
    24: untimely4_2_4 + untimely5_2_4 + untimely6_2_4,
    27: untimely4_2_7 + untimely5_2_7 + untimely6_2_7,
    210: untimely4_2_10 + untimely5_2_10 + untimely6_2_10,

    34: untimely4_3_4 + untimely5_3_4 + untimely6_3_4,
    37: untimely4_3_7 + untimely5_3_7 + untimely6_3_7,
    310: untimely4_3_10 + untimely5_3_10 + untimely6_3_10,

    74: untimely4_7_4 + untimely5_7_4 + untimely6_7_4,
    77: untimely4_7_7 + untimely5_7_7 + untimely6_7_7,
    710: untimely4_7_10 + untimely5_7_10 + untimely6_7_10,

    104: untimely4_10_4 + untimely5_10_4 + untimely6_10_4,
    107: untimely4_10_7 + untimely5_10_7 + untimely6_10_7,
    1010: untimely4_10_10 + untimely5_10_10 + untimely6_10_10,

    124: untimely4_12_4 + untimely5_12_4 + untimely6_12_4,
    127: untimely4_12_7 + untimely5_12_7 + untimely6_12_7,
    1210: untimely4_12_10 + untimely5_12_10 + untimely6_12_10,

    164: untimely4_16_4 + untimely5_16_4 + untimely6_16_4,
    167: untimely4_16_7 + untimely5_16_7 + untimely6_16_7,
    1610: untimely4_16_10 + untimely5_16_10 + untimely6_16_10,

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


def format_data(time_av_t, time_av_u ):
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
            if 7 in t_data:
                t_data[7].append(time_av_t[j])
                u_data[7].append(time_av_u[j])
                s5 += 3
            else:
                t_data[7] = [time_av_t[j]]
                u_data[7] = [time_av_u[j]]
                s5 += 3
        elif i == s6:
            if 10 in t_data:
                t_data[10].append(time_av_t[j])
                u_data[10].append(time_av_u[j])
                s6 += 3
            else:
                t_data[10] = [time_av_t[j]]
                u_data[10] = [time_av_u[j]]
                s6 += 3

    return t_data, u_data


def plot_av_times():
    axes = {ax1: 4, ax2: 7, ax3: 10}
    _data = format_data(_timely, _untimely)
    # print(_data)
    for i in axes:
        histogram(_data[0][axes[i]], _data[1][axes[i]], i, axes[i])
    fig.suptitle('Execution Time Comparison During Deadlock Experiment')
    plt.show()


plot_av_times()

