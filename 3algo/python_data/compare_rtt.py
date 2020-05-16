import matplotlib.pyplot as plt
from data_het.mec_data import *

fig = plt.figure()
ax1 = fig.add_subplot(361)
ax2 = fig.add_subplot(362)
ax3 = fig.add_subplot(363)
ax4 = fig.add_subplot(364)
ax5 = fig.add_subplot(365)
ax6 = fig.add_subplot(366)
ax7 = fig.add_subplot(367)
ax8 = fig.add_subplot(368)
ax9 = fig.add_subplot(369)
ax10 = fig.add_subplot(3, 6, 10)
ax11 = fig.add_subplot(3, 6, 11)
ax12 = fig.add_subplot(3, 6, 12)
ax13 = fig.add_subplot(3, 6, 13)
ax14 = fig.add_subplot(3, 6, 14)
ax15 = fig.add_subplot(3, 6, 15)
ax16 = fig.add_subplot(3, 6, 16)
ax17 = fig.add_subplot(3, 6, 17)
ax18 = fig.add_subplot(3, 6, 18)

style1 = [{'color': 'g', 'marker': '^'}, {'color': 'aqua', 'marker': '*'}, {'color': 'purple', 'marker': 'X'},
          {'color': 'r', 'marker': 'v'}, {'color': 'k', 'marker': '>'}, {'color': 'brown', 'marker': 'D'},
          {'color': 'b', 'marker': 's'}, {'color': 'c', 'marker': '1'}, {'color': 'olive', 'marker': 'p'}, ]
style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>', 'c-.s', 'c-.s', 'c-.s', 'c-.s', 'c-.s', 'c-.s']
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
font = {'family': 'serif',
        'color': 'black',
        'weight': 'medium',
        'size': 16,
        }
font1 = {'family': 'serif',
         'color': 'black',
         'weight': 'bold',
         'size': 12,
         }
_rtt = {
    24: rtt2_2_4,
    27: rtt2_2_7,
    210: rtt2_2_10,

    34: rtt2_3_4,
    37: rtt2_3_7,
    310: rtt2_3_10,

    74: rtt2_7_4,
    77: rtt2_7_7,
    710: rtt2_7_10,

    104: rtt2_10_4,
    107: rtt2_10_7,
    1010: rtt2_10_10,

    124: rtt2_12_4,
    127: rtt2_12_7,
    1210: rtt2_12_10,

    164: rtt2_16_4,
    167: rtt2_16_7,
    1610: rtt2_16_10,

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


def plot_rtt(plot_data, ax, no, mec):
    ax.grid(True)
    ax_list = (ax1, ax7, ax13)
    axx_list = {ax6: 4, ax12: 7, ax18: 10}
    list_dict = list(plot_data.keys())
    for j in plot_data:

        i = plot_data[j]
        style_id = list_dict.index(j)
        mv = _mov_avg(i)
        pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])

        a = list(range(0, len(mv)))
        ptx = a[0:len(a):int((len(a) / 10)) + 1]
        if ptx[-1] != a[-1]:
            ptx.append(a[-1])
        ax.plot(ptx,
                pt,
                **style1[style_id],
                linestyle=(0, (3, 1, 1, 1, 1, 1)),
                linewidth=2,
                label=j)

    if mec == 4:
        ax.set_title(algo_dict[names[no]], fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font1)
    if ax in ax_list:
        ax.set_ylabel('RTT (ms)', fontdict=font1)
    # ax.set_ylim(top=4.6)
    # ax.set_ylim(bottom=0)
    axx = ax.twinx()
    axx.set_yticklabels([])
    axx.set_yticks([])
    if ax in axx_list:
        axx.set_ylabel(f'{axx_list[ax]} MECs', rotation=0, fontsize=15, labelpad=30)


def call_plot():
    axis = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18]
    k = format_data(_rtt)
    axis_id = 0
    for i in k:
        for j in k[i]:
            nos = k[i].index(j)
            plot_rtt(j, axis[axis_id], nos, i)
            axis_id += 1
    plt.show()


call_plot()
