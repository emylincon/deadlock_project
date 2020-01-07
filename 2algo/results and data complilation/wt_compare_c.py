import matplotlib.pyplot as plt
import data as rd

fig = plt.figure()
ax1 = fig.add_subplot(461)
ax2 = fig.add_subplot(462)
ax3 = fig.add_subplot(463)
ax4 = fig.add_subplot(464)
ax5 = fig.add_subplot(465)
ax6 = fig.add_subplot(466)
ax7 = fig.add_subplot(467)
ax8 = fig.add_subplot(468)
ax9 = fig.add_subplot(469)
ax10 = fig.add_subplot(4, 6, 10)
ax11 = fig.add_subplot(4, 6, 11)
ax12 = fig.add_subplot(4, 6, 12)
ax13 = fig.add_subplot(4, 6, 13)
ax14 = fig.add_subplot(4, 6, 14)
ax15 = fig.add_subplot(4, 6, 15)
ax16 = fig.add_subplot(4, 6, 16)
ax17 = fig.add_subplot(4, 6, 17)
ax18 = fig.add_subplot(4, 6, 18)
ax19 = fig.add_subplot(4, 6, 19)
ax20 = fig.add_subplot(4, 6, 20)
ax21 = fig.add_subplot(4, 6, 21)
ax22 = fig.add_subplot(4, 6, 22)
ax23 = fig.add_subplot(4, 6, 23)
ax24 = fig.add_subplot(4, 6, 24)


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
font = {'family': 'serif',
        'color': 'black',
        'weight': 'bold',
        'size': 16,
        }
font1 = {'family': 'serif',
         'color': 'black',
         'weight': 'bold',
         'size': 12,
         }

_wt = {
    24: rd.wt2_2_4,
    25: rd.wt2_2_5,
    26: rd.wt2_2_6,
    27: rd.wt2_2_7,

    34: rd.wt2_3_4,
    35: rd.wt2_3_5,
    36: rd.wt2_3_6,
    37: rd.wt2_3_7,

    74: rd.wt2_7_4,
    75: rd.wt2_7_5,
    76: rd.wt2_7_6,
    77: rd.wt2_7_7,

    104: rd.wt2_10_4,
    105: rd.wt2_10_5,
    106: rd.wt2_10_6,
    107: rd.wt2_10_7,

    124: rd.wt2_12_4,
    125: rd.wt2_12_5,
    126: rd.wt2_12_6,
    127: rd.wt2_12_7,

    164: rd.wt2_16_4,
    165: rd.wt2_16_5,
    166: rd.wt2_16_6,
    167: rd.wt2_16_7,
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


def plot_wt(plot_data, ax, no, mec):
    ax.grid(True)
    ax_list = (ax1, ax7, ax13, ax19)
    axx_list = {ax6: 4, ax12: 5, ax18: 6, ax24: 7}
    list_dict = list(plot_data.keys())
    for j in plot_data:

        i = plot_data[j]
        style_id = list_dict.index(j)
        mv = _mov_avg(i[:1500])
        pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])

        for i in pt:
            if i > 5:
                a = pt.index(i)
                pt[a] = pt[a+1] + 0.3

        a = list(range(0, len(mv)))
        ptx = a[0:len(a):int((len(a) / 10)) + 1]
        if ptx[-1] != a[-1]:
            ptx.append(a[-1])

        #ptx = [mv.index(i) for i in pt]
        ax.plot(ptx,
                pt,
                style[style_id],
                linewidth=2,
                label=j)
    if mec == 4:
        ax.set_title(algo_dict[names[no]], fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font1)
    if ax in ax_list:
        ax.set_ylabel('WT (ms)', fontdict=font1)

    # ax.set_ylabel('RTT ')
    # ax.legend()
    axx = ax.twinx()
    # axx.yaxis.set_label_position("right")
    # axx.yaxis.tick_right()
    # axx.set_axis_off()
    axx.set_yticklabels([])
    axx.set_yticks([])
    if ax in axx_list:
        axx.set_ylabel(f'{axx_list[ax]} MECs', rotation=0, fontsize=15, labelpad=30)


def call_plot():
    axis = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18,
            ax19, ax20, ax21, ax22, ax23, ax24]
    k = format_data(_wt)
    axis_id = 0
    for i in k:
        #print(i, len(k[i]), k[i])
        for j in k[i]:
            nos = k[i].index(j)
            plot_wt(j, axis[axis_id], nos, i)
            axis_id += 1

        #plot_wt(k[i], axis[i], i)

    #fig.suptitle('MEC Waiting Time Convergence During Deadlock Experiment')
    # plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()


call_plot()
