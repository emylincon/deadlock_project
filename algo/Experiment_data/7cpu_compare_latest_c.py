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
algo_dict = {'RMS+Bankers': r'$ALG_1$',
                 'EDF+Bankers': r'$ALG_2$',
                 'RMS+wound wait': r'$ALG_3$',
                 'RMS+wait die': r'$ALG_4$',
                 'EDF+wound wait': r'$ALG_5$',
                 'EDF+wait die': r'$ALG_6$'}


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
                   label=f'{name} (Avg) : {round(mv[-1], 3)}')


def four_mec():
    ax1.grid(True)
    _list = [data.cpu_1, data.cpu_3, data.cpu_5, data.cpu_8, data.cpu_11, data.cpu_16]
    labels = list(algo_dict.values())
    for i in _list:
        get_x_y(data=i, ax=ax1, _id=_list.index(i), name=labels[_list.index(i)])

    ax1.set_title('Moving CPU Utilization for 4 MEC Set-up', fontdict={'weight': 'medium', "size":14})
    ax1.set_ylabel('Moving CPU %', fontdict={'weight': 'medium', 'size': 13})
    ax1.set_ylim(top=30)
    ax1.set_xlabel('Time Period', fontdict={'weight': 'medium', 'size': 13})
    ax1.legend(prop={"size":14})
    plt.subplot(ax1)


def five_mec():
    ax3.grid(True)

    _list = [d1cpu.cpu_1_5, data.cpu_3_5, data.cpu_5_5, data.cpu_8_5, data.cpu_11_5, data.cpu_16_5]
    labels = list(algo_dict.values())
    for i in _list:
        get_x_y(data=i, ax=ax3, _id=_list.index(i), name=labels[_list.index(i)])

    ax3.set_title('Moving CPU Utilization for 6 MEC Set-up', fontdict={'weight': 'medium', "size":14})
    ax3.set_ylabel('Moving CPU %', fontdict={'weight': 'medium', 'size': 13})
    ax3.set_ylim(top=30)
    ax3.set_xlabel('Time Period', fontdict={'weight': 'medium', 'size': 13})
    ax3.legend(prop={"size":14})
    plt.subplot(ax3)


def six_mec():
    ax2.grid(True)

    _list = [d1cpu.cpu_1_6, data.cpu_3_6, data.cpu_5_6, data.cpu_8_6, data.cpu_11_6, data.cpu_16_6]
    labels = list(algo_dict.values())
    for i in _list:
        get_x_y(data=i, ax=ax2, _id=_list.index(i), name=labels[_list.index(i)])

    ax2.set_title('Moving CPU Utilization for 5 MEC Set-up', fontdict={'weight': 'medium', "size":14})
    ax2.set_ylabel('Moving CPU %', fontdict={'weight': 'medium', 'size': 13})
    ax2.set_ylim(top=30)
    ax2.set_xlabel('Time Period', fontdict={'weight': 'medium', 'size': 13})
    ax2.legend(prop={"size":14})
    plt.subplot(ax2)


def seven_mec():
    ax4.grid(True)

    _list = [d1cpu.cpu_1_7, d1cpu.cpu_3_7, d1cpu.cpu_5_7, d1cpu.cpu_8_7, d1cpu.cpu_11_7, d1cpu.cpu_16_7]
    labels = list(algo_dict.values())
    for i in _list:
        get_x_y(data=i, ax=ax4, _id=_list.index(i), name=labels[_list.index(i)])

    ax4.set_title('Moving CPU Utilization for 7 MEC Set-up',  fontdict={'weight': 'medium', "size":14})
    ax4.set_ylabel('Moving CPU %', fontdict={'weight': 'medium', 'size': 13})
    ax4.set_ylim(top=30)
    ax4.set_xlabel('Time Period', fontdict={'weight': 'medium', 'size': 13})
    ax4.legend(prop={"size":14})
    plt.subplot(ax4)


def plot_graphs():
    four_mec()
    five_mec()
    six_mec()
    seven_mec()
    #fig.suptitle('MEC CPU Utilization During Homogeneous Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()
