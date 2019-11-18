from drawnow import *
from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import data
import redo_data as rd

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)


width = 0.30


def percent(value, total):
    if value > 0:
        return round((value / total) * 100, 2)
    else:
        return 0


def histogram(local, offload, ax, no):
    ind = np.arange(len(local))
    p1 = ax.bar(ind, offload, width, color='r', alpha=0.4)
    p2 = ax.bar(ind, local, width, color='g', bottom=offload, alpha=0.4)
    ax.set_xticks(ind)
    ax.set_xticklabels(('RMS + Bankers',
                        'EDF + Bankers',
                        'RMS + wound wait',
                        'RMS + wait die',
                        'EDF + wound wait',
                        'EDF + wait die'))
    a = []
    for i in local:
        if i in a:
            start = local.index(i) + 1
            j = local.index(i, start, -1)
            total = i + offload[j]
            ax.text(j, local[j] + offload[j], '{}%'.format(percent(i, total)), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
            ax.text(j, offload[j], '{}%'.format(percent(offload[j], total)), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
        else:
            j = local.index(i)
            total = i + offload[j]
            ax.text(j, local[j] + offload[j], '{}%'.format(percent(i, total)), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
            ax.text(j, offload[j], '{}%'.format(percent(offload[j], total)), rotation=0,
                    ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
            a.append(i)
    ax.legend((p1[0], p2[0]), ('Offload', 'Local'))
    # ax.set_ylabel('\n'.join(wrap(f'Plot for {no} MECs', 8))).set_rotation(0)
    ax.set_ylabel('\n'.join(wrap(f'{no} MECs', 8)), rotation=0, fontsize=15, labelpad=30)


def plot_av_times():
    axes = {ax1: 4, ax2: 5, ax3: 6, ax4: 7}
    _data_ = {
        4: [[data.off_mec1 + data.off_cloud1, data.loc1],
            [data.off_mec3 + data.off_cloud3, data.loc3],
            [data.off_mec5 + data.off_cloud3, data.loc5],
            [data.off_mec8 + data.off_cloud8, data.loc8],
            [data.off_mec11 + data.off_cloud11, data.loc11],
            [data.off_mec16 + data.off_cloud16, data.loc16]],
        5: [[data.off_mec1_5 + data.off_cloud1_5, data.loc1_5],
            [data.off_mec3_6 + data.off_cloud3_6, data.loc3_6],
            [data.off_mec5_5 + data.off_cloud5_5, data.loc5_5],
            [data.off_mec8_6 + data.off_cloud8_6, data.loc8_6],
            [data.off_mec11_6 + data.off_cloud11_6, data.loc11_6],
            [rd.off_mec16_7 + rd.off_cloud16_7, rd.loc16_7],
            ],
        6: [
            [rd.off_mec1_7 + rd.off_cloud1_7, rd.loc1_7],
            [rd.off_mec3_7 + rd.off_cloud3_7, rd.loc3_7],
            [rd.off_mec5_7 + rd.off_cloud5_7, rd.loc5_7],
            [data.off_mec8_5 + data.off_cloud8_5, data.loc8_5],
            [rd.off_mec11_7 + rd.off_cloud11_7, rd.loc11_7],
            [data.off_mec16_6 + data.off_cloud16_6, data.loc16_6],
        ],
        7: [
            [data.off_mec1_6 + data.off_cloud1_6, data.loc1_6],
            [data.off_mec3_5 + data.off_cloud3_5, data.loc3_5],
            [data.off_mec5_5 + data.off_cloud5_5, data.loc5_5],
            [rd.off_mec8_7 + rd.off_cloud8_7, rd.loc8_7],
            [data.off_mec11_5 + data.off_cloud11_5, data.loc11_5],
            [data.off_mec16_5 + data.off_cloud16_5, data.loc16_5]
        ]
    }
    _data_l = {}
    _data_o = {}
    for i in _data_:
        for j in _data_[i]:
            if i in _data_l:
                _data_l[i].append(j[1])
                _data_o[i].append(j[0])
            else:
                _data_l[i] = [j[1]]
                _data_o[i] = [j[0]]

    for i in axes:
        histogram(_data_l[axes[i]], _data_o[axes[i]], i, axes[i])
    fig.suptitle('MEC Offload Vs Local Comparison for Homogeneous Setup During Deadlock Experiment')
    plt.show()


plot_av_times()
