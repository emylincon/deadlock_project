import matplotlib.pyplot as plt
from data import cpu as rd

fig = plt.figure()
ax1 = fig.add_subplot(141)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(144)


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

_cpu = {
    24: rd.cpu2_2_4,
    25: rd.cpu2_2_5,
    26: rd.cpu2_2_6,
    27: rd.cpu2_2_7,

    34: rd.cpu2_3_4,
    35: rd.cpu2_3_5,
    36: rd.cpu2_3_6,
    37: rd.cpu2_3_7,

    74: rd.cpu2_7_4,
    75: rd.cpu2_7_5,
    76: rd.cpu2_7_6,
    77: rd.cpu2_7_7,

    104: rd.cpu2_10_4,
    105: rd.cpu2_10_5,
    106: rd.cpu2_10_6,
    107: rd.cpu2_10_7,

    124: rd.cpu2_12_4,
    125: rd.cpu2_12_5,
    126: rd.cpu2_12_6,
    127: rd.cpu2_12_7,

    164: rd.cpu2_16_4,
    165: rd.cpu2_16_5,
    166: rd.cpu2_16_6,
    167: rd.cpu2_16_7,
}


def format_data(d_dict):
    t_data = {}
    _keys = list(d_dict.keys())
    s4 = 0
    s5 = 1
    s6 = 2
    s7 = 3
    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(d_dict[j])

                s4 += 4
            else:
                t_data[4] = [d_dict[j]]

                s4 += 4
        elif i == s5:
            if 5 in t_data:
                t_data[5].append(d_dict[j])

                s5 += 4
            else:
                t_data[5] = [d_dict[j]]

                s5 += 4
        elif i == s6:
            if 6 in t_data:
                t_data[6].append(d_dict[j])

                s6 += 4
            else:
                t_data[6] = [d_dict[j]]

                s6 += 4
        elif i == s7:
            if 7 in t_data:
                t_data[7].append(d_dict[j])

                s7 += 4
            else:
                t_data[7] = [d_dict[j]]

                s7 += 4
    #print(t_data)
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


def plot_cpu(plot_data, ax, no):
    global ax1, ax2, ax3, ax4

    # _map = {5:4, 6:5, 4:6, 7:7}
    # ax_map = {ax1: ax3, ax2: ax1, ax3: ax2, ax4:ax4}
    # #no = _map[no]
    # ax = ax_map[axis]

    for i in plot_data:
        style_id = plot_data.index(i)
        # if (style_id == 2) and (no == 6):
        #     mv = _mov_avg(i)
        #     # sample.append(len(mv))
        #     pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
        #     if pt[-1] != mv[-1]:
        #         pt.append(mv[-1])
        #
        #     a = list(range(0, 222))
        #     ptx = a[0:len(a):int((len(a) / 10)) + 1]
        #     if ptx[-1] != a[-1]:
        #         ptx.append(a[-1])
        # else:
        mv = _mov_avg(i[:])

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
                style[style_id],
                linewidth=2,
                label=f'{algo_dict[names[style_id]]} (Avg) : {mv[-1]}')
    ax.set_title(f'Moving Utilization for {no} MEC Set-up', fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font)
    ax.set_ylabel('CPU Utilization in Percentage', fontdict=font)
    ax.set_ylim(top=8.1)
    ax.set_ylim(bottom=1.5)
    ax.legend(prop={"size":14})
    plt.subplot(ax)


def _plot_cpu(plot_data, ax, no):
    ax.grid(True)

    for i in plot_data:
        style_id = plot_data.index(i)

        ax.plot(i,

                linewidth=2,
                label=names[style_id])
    ax.set_title(f'Moving Utilization for {no} MEC Set-up', fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font)
    ax.legend()
    plt.subplot(ax)


def call_plot():
    axis = {4:ax1, 5:ax2, 6:ax3, 7:ax4}
    k = format_data(_cpu)

    for i in k:
        plot_cpu(k[i], axis[i], i)
    #fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    # plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()


call_plot()

