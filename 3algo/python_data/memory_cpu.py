from data_het.mec_data import *
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

style1 = [{'color': 'g', 'marker': '^'}, {'color': 'aqua', 'marker': '*'}, {'color': 'purple', 'marker': 'X'},
          {'color': 'r', 'marker': 'v'}, {'color': 'k', 'marker': '>'}, {'color': 'brown', 'marker': 'D'},
          {'color': 'b', 'marker': 's'}, {'color': 'c', 'marker': '1'}, {'color': 'olive', 'marker': 'p'}, ]
style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>', 'c-.s']
names = ('RMS+Bankers',
         'EDF+Bankers',
         'RMS+wound wait',
         'RMS+wait die',
         'EDF+wound wait',
         'EDF+wait die')
algo_dict = {'RMS+Bankers': r'$ALG_1$',
             'EDF+Bankers': r'$ALG_2$',
             'RMS+wound wait': r'$ALG_3$',
             'RMS+wait die': r'$ALG_4$',
             'EDF+wound wait': r'$ALG_5$',
             'EDF+wait die': r'$ALG_6$'}
font = {
        'weight': 'medium',
        'size': 14,
        }

_memory = {
    24: memory2_2_4,
    27: memory2_2_7,
    210: memory2_2_10,

    34: memory2_3_4,
    37: memory2_3_7,
    310: memory2_3_10,

    74: memory2_7_4,
    77: memory2_7_7,
    710: memory2_7_10,

    104: memory2_10_4,
    107: memory2_10_7,
    1010: memory2_10_10,

    124: memory2_12_4,
    127: memory2_12_7,
    1210: memory2_12_10,

    164: memory2_16_4,
    167: memory2_16_7,
    1610: memory2_16_10,

}


def format_data(d_dict):
    t_data = {}
    _keys = list(d_dict.keys())
    s4 = 0
    s7 = 1
    s10 = 2

    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(d_dict[j])

                s4 += 3
            else:
                t_data[4] = [d_dict[j]]

                s4 += 3
        elif i == s7:
            if 7 in t_data:
                t_data[7].append(d_dict[j])

                s7 += 3
            else:
                t_data[7] = [d_dict[j]]

                s7 += 3
        elif i == s10:
            if 10 in t_data:
                t_data[10].append(d_dict[j])

                s10 += 3
            else:
                t_data[10] = [d_dict[j]]

                s10 += 3

    return t_data


def _mov_avg(a1):
    ma1 = []  # moving average list
    avg1 = 0  # moving average pointwise
    count = 0
    for i in range(len(a1)):
        count += 1
        avg1 = ((count - 1) * avg1 + a1[i]) / count
        ma1.append(round(avg1, 4))  # cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def plot_memory(plot_data, ax, no):
    global ax1, ax2, ax3, ax4

    for i in plot_data:
        style_id = plot_data.index(i)
        if (style_id == 2) and (no == 6):
            mv = _mov_avg(i)
            pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
            if pt[-1] != mv[-1]:
                pt.append(mv[-1])

            a = list(range(len(i)))
            ptx = a[0:len(a):int((len(a) / 10)) + 1]
            if ptx[-1] != a[-1]:
                ptx.append(a[-1])
        else:
            mv = _mov_avg(i)
            pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
            if pt[-1] != mv[-1]:
                pt.append(mv[-1])

            a = list(range(0, len(mv)))
            ptx = a[0:len(a):int((len(a) / 10)) + 1]
            if ptx[-1] != a[-1]:
                ptx.append(a[-1])

        ax.grid(True)
        ax.plot(ptx,
                pt,
                **style1[style_id],
                linestyle=(0, (3, 1, 1, 1, 1, 1)),
                linewidth=2,
                label=f'{algo_dict[names[style_id]]} (Avg) : {mv[-1]}')
    ax.set_title(f'Moving Utilization for {no} MEC Set-up', fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font)
    ax.set_ylabel('memory Utilization in Percentage', fontdict=font)
    # ax.set_ylim(top=8.1)
    # ax.set_ylim(bottom=1.5)
    #ax.xaxis.set_tick_params(labelsize=16)
    ax.legend(prop={"size":14})
    plt.subplot(ax)


def call_plot():
    axis = {4:ax1, 7:ax2, 10:ax3}
    k = format_data(_memory)

    for i in k:
        plot_memory(k[i], axis[i], i)
    #fig.suptitle('MEC memory Utilization During Deadlock Experiment')
    # plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()


call_plot()
