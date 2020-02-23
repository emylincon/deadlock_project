from data import timely as t
from data import diff as d
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
timely_dict = {2: {4: [d.timely4_2_4, d.timely5_2_4, d.timely6_2_4],
                   5: [d.timely4_2_5, d.timely5_2_5, d.timely6_2_5],
                   6: [d.timely4_2_6, d.timely5_2_6, d.timely6_2_6],
                   7: [d.timely4_2_7, d.timely5_2_7, d.timely6_2_7]},
               3: {4: [t.timely4_3_4, t.timely5_3_4, t.timely6_3_4],
                   5: [t.timely4_3_5, t.timely5_3_5, t.timely6_3_5],
                   6: [t.timely4_3_6, t.timely5_3_6, t.timely6_3_6],
                   7: [t.timely4_3_7, t.timely5_3_7, t.timely6_3_7]},
               7: {4: [t.timely4_7_4, t.timely5_7_4, t.timely6_7_4],
                   5: [t.timely4_7_5, t.timely5_7_5, t.timely6_7_5],
                   6: [t.timely4_7_6, t.timely5_7_6, t.timely6_7_6],
                   7: [t.timely4_7_7, t.timely5_7_7, t.timely6_7_7]},
               10: {4: [t.timely4_10_4, t.timely5_10_4, t.timely6_10_4],
                    5: [t.timely4_10_5, t.timely5_10_5, t.timely6_10_5],
                    6: [t.timely4_10_6, t.timely5_10_6, t.timely6_10_6],
                    7: [t.timely4_10_7, t.timely5_10_7, t.timely6_10_7]},
               12: {4: [t.timely4_12_4, t.timely5_12_4, t.timely6_12_4],
                    5: [t.timely4_12_5, t.timely5_12_5, t.timely6_12_5],
                    6: [t.timely4_12_6, t.timely5_12_6, t.timely6_12_6],
                    7: [t.timely4_12_7, t.timely5_12_7, t.timely6_12_7]},
               16: {4: [t.timely4_16_4, t.timely5_16_4, t.timely6_16_4],
                    5: [t.timely4_16_5, t.timely5_16_5, t.timely6_16_5],
                    6: [t.timely4_16_6, t.timely5_16_6, t.timely6_16_6],
                    7: [t.timely4_16_7, t.timely5_16_7, t.timely6_16_7]}
               }

untimely_dict = {2: {4: [d.untimely4_2_4, d.untimely5_2_4, d.untimely6_2_4],
                     5: [d.untimely4_2_5, d.untimely5_2_5, d.untimely6_2_5],
                     6: [d.untimely4_2_6, d.untimely5_2_6, d.untimely6_2_6],
                     7: [d.untimely4_2_7, d.untimely5_2_7, d.untimely6_2_7]},
                 3: {4: [t.untimely4_3_4, t.untimely5_3_4, t.untimely6_3_4],
                     5: [t.untimely4_3_5, t.untimely5_3_5, t.untimely6_3_5],
                     6: [t.untimely4_3_6, t.untimely5_3_6, t.untimely6_3_6],
                     7: [t.untimely4_3_7, t.untimely5_3_7, t.untimely6_3_7]},
                 7: {4: [t.untimely4_7_4, t.untimely5_7_4, t.untimely6_7_4],
                     5: [t.untimely4_7_5, t.untimely5_7_5, t.untimely6_7_5],
                     6: [t.untimely4_7_6, t.untimely5_7_6, t.untimely6_7_6],
                     7: [t.untimely4_7_7, t.untimely5_7_7, t.untimely6_7_7]},
                 10: {4: [t.untimely4_10_4, t.untimely5_10_4, t.untimely6_10_4],
                      5: [t.untimely4_10_5, t.untimely5_10_5, t.untimely6_10_5],
                      6: [t.untimely4_10_6, t.untimely5_10_6, t.untimely6_10_6],
                      7: [t.untimely4_10_7, t.untimely5_10_7, t.untimely6_10_7]},
                 12: {4: [t.untimely4_12_4, t.untimely5_12_4, t.untimely6_12_4],
                      5: [t.untimely4_12_5, t.untimely5_12_5, t.untimely6_12_5],
                      6: [t.untimely4_12_6, t.untimely5_12_6, t.untimely6_12_6],
                      7: [t.untimely4_12_7, t.untimely5_12_7, t.untimely6_12_7]},
                 16: {4: [t.untimely4_16_4, t.untimely5_16_4, t.untimely6_16_4],
                      5: [t.untimely4_16_5, t.untimely5_16_5, t.untimely6_16_5],
                      6: [t.untimely4_16_6, t.untimely5_16_6, t.untimely6_16_6],
                      7: [t.untimely4_16_7, t.untimely5_16_7, t.untimely6_16_7]}
                 }


def sum_data(data):
    result = {}
    for algo in data:
        for no in data[algo]:
            if no in result:
                result[no].append(sum(data[algo][no]))
            else:
                result[no] = [sum(data[algo][no])]

    return result


def total_data():
    data_tuple = format_data()
    result = {}
    for no in data_tuple[0]:
        for item_id in range(len(data_tuple[0][no])):
            if no in result:
                result[no].append(data_tuple[0][no][item_id] + data_tuple[1][no][item_id])
            else:
                result[no] = [data_tuple[0][no][item_id] + data_tuple[1][no][item_id]]

    print(result)


def format_data():
    return sum_data(timely_dict), sum_data(untimely_dict)


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


def plot_av_times():
    axes = {ax1: 4, ax2: 5, ax3: 6, ax4: 7}
    _data = format_data()
    # print(_data)
    for i in axes:
        histogram(_data[0][axes[i]], _data[1][axes[i]], i, axes[i])
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.show()

total_data()
plot_av_times()
