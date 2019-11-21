from drawnow import *
from matplotlib import pyplot as plt
import data
import cpu_redo as cp
import cpu6_redo as cp6
import data_for_1cpu as d1cpu

fig = plt.figure()
ax1 = fig.add_subplot(141)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(144)

style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>', 'c--+']


def _mov_avg(a1):
    ma1 = []  # moving average list
    avg1 = 0  # movinf average pointwise
    count = 0
    for i in range(len(a1)):
        count += 1
        avg1 = ((count - 1) * avg1 + a1[i]) / count
        ma1.append(avg1)  # cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def x_index(full_list, sel_list):
    r_list = []
    r_set = set()
    for i in sel_list:
        if i in r_set:
            start = full_list.index(i) + 1
            r_list.append(full_list.index(i, start, 499))
        else:
            r_list.append(full_list.index(i))
            r_set.add(i)
    return r_list


def get_x_y(data, ax, _id, name):
    mv = _mov_avg(data)
    pt = mv[0:len(mv):int((len(mv) / 20)) + 1]
    if pt[-1] != mv[-1]:
        pt.append(mv[-1])
    # ptx = [mv.index(i) for i in pt]
    ptx = x_index(full_list=mv, sel_list=pt)

    return ax.plot(ptx,
                   pt,
                   style[_id],
                   linewidth=2,
                   label=name)


def four_mec():
    ax1.grid(True)
    _list = [data.cpu_1, data.cpu_3, data.cpu_5, data.cpu_8, data.cpu_11, data.cpu_16]
    labels = ('RMS + Bankers',
              'EDF + Bankers',
              'RMS + wound wait',
              'RMS + wait die',
              'EDF + wound wait',
              'EDF + wait die')
    for i in _list:
        get_x_y(data=i, ax=ax1, _id=_list.index(i), name=labels[_list.index(i)])

    '''
    ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_3), linewidth=2, label='EDF + Bankers')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_5), linewidth=2, label='RMS + wound wait')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_8), linewidth=2, label='RMS + wait die')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_11), linewidth=2, label='EDF + wound wait')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_16), linewidth=2, label='EDF + wait die')
    '''

    ax1.set_title('Moving CPU Utilization for 4 MEC Set-up')
    ax1.set_ylabel('Moving CPU')
    ax1.set_ylim(top=30)
    ax1.set_xlabel('Time (seconds)')
    ax1.legend()
    plt.subplot(ax1)


def five_mec():
    ax2.grid(True)

    _list = [d1cpu.cpu_1_5, data.cpu_3_5, data.cpu_5_5, data.cpu_8_5, data.cpu_11_5, data.cpu_16_5]
    labels = ('RMS + Bankers',
              'EDF + Bankers',
              'RMS + wound wait',
              'RMS + wait die',
              'EDF + wound wait',
              'EDF + wait die')
    for i in _list:
        get_x_y(data=i, ax=ax2, _id=_list.index(i), name=labels[_list.index(i)])

    '''
    ax2.plot(list(range(500)), _mov_avg(d1cpu.cpu_1_5), linewidth=2, label='RMS + Bankers')
    # ax2.plot(list(range(500)), _mov_avg(cp.cpu_1_5), linewidth=2, label='RMS + Bankers')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_3_5), linewidth=2, label='EDF + Bankers')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_5_5), linewidth=2, label='RMS + wound wait')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_8_5), linewidth=2, label='RMS + wait die')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_11_5), linewidth=2, label='EDF + wound wait')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_16_5), linewidth=2, label='EDF + wait die')
    '''

    ax2.set_title('Moving CPU Utilization for 5 MEC Set-up')
    ax2.set_ylabel('Moving CPU')
    ax2.set_ylim(top=30)
    ax2.set_xlabel('Time (seconds)')
    ax2.legend()
    plt.subplot(ax2)


def six_mec():
    ax3.grid(True)

    _list = [d1cpu.cpu_1_6, data.cpu_3_6, data.cpu_5_6, data.cpu_8_6, data.cpu_11_6, data.cpu_16_6]
    labels = ('RMS + Bankers',
              'EDF + Bankers',
              'RMS + wound wait',
              'RMS + wait die',
              'EDF + wound wait',
              'EDF + wait die')
    for i in _list:
        get_x_y(data=i, ax=ax3, _id=_list.index(i), name=labels[_list.index(i)])
    '''
    ax3.plot(list(range(500)), _mov_avg(d1cpu.cpu_1_6), linewidth=2, label='RMS + Bankers')
    # ax3.plot(list(range(500)), _mov_avg(cp6.cpu_1_6), linewidth=2, label='RMS + Bankers')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_3_6), linewidth=2, label='EDF + Bankers')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_5_6), linewidth=2, label='RMS + wound wait')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_8_6), linewidth=2, label='RMS + wait die')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_11_6), linewidth=2, label='EDF + wound wait')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_16_6), linewidth=2, label='EDF + wait die')
    '''
    ax3.set_title('Moving CPU Utilization for 6 MEC Set-up')
    ax3.set_ylabel('Moving CPU')
    ax3.set_ylim(top=30)
    ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


def seven_mec():
    ax4.grid(True)

    _list = [d1cpu.cpu_1_7, d1cpu.cpu_3_7, d1cpu.cpu_5_7, d1cpu.cpu_8_7, d1cpu.cpu_11_7, d1cpu.cpu_16_7]
    labels = ('RMS + Bankers',
              'EDF + Bankers',
              'RMS + wound wait',
              'RMS + wait die',
              'EDF + wound wait',
              'EDF + wait die')
    for i in _list:
        get_x_y(data=i, ax=ax4, _id=_list.index(i), name=labels[_list.index(i)])
    '''
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_1_7), linewidth=2, label='RMS + Bankers')
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_3_7), linewidth=2, label='EDF + Bankers')
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_5_7), linewidth=2, label='RMS + wound wait')
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_8_7), linewidth=2, label='RMS + wait die')
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_11_7), linewidth=2, label='EDF + wound wait')
    ax4.plot(list(range(500)), _mov_avg(d1cpu.cpu_16_7), linewidth=2, label='EDF + wait die')
    '''
    ax4.set_title('Moving CPU Utilization for 7 MEC Set-up')
    ax4.set_ylabel('Moving CPU')
    ax4.set_ylim(top=30)
    ax4.set_xlabel('Time (seconds)')
    ax4.legend()
    plt.subplot(ax4)


def plot_graphs():
    four_mec()
    five_mec()
    six_mec()
    seven_mec()
    fig.suptitle('MEC CPU Utilization During Homogeneous Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()
