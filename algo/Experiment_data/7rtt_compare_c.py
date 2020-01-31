from drawnow import *
from matplotlib import pyplot as plt
import data
import redo_data as rd

fig = plt.figure()
ax1 = fig.add_subplot(461)
ax2 = fig.add_subplot(462)
ax3 = fig.add_subplot(463)
ax4 = fig.add_subplot(464)
ax5 = fig.add_subplot(465)
ax6 = fig.add_subplot(466)
ax7 = fig.add_subplot(467)
ax8 = fig.add_subplot(468)
ax9 = fig.add_subplot(4, 6, 9)
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

style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>', 'c--']

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
font1 = {
         'color': 'black',
         'weight': 'bold',
         'size': 14,
         }


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
avg = []

def plot_rtt(plot_data, ax, no, mec):
    ax.grid(True)
    ax_list = (ax1, ax7, ax13, ax19)
    axx_list = {ax6: 4, ax12: 5, ax18: 6, ax24: 7}
    list_dict = list(plot_data.keys())
    data = []
    for j in plot_data:

        i = plot_data[j]
        data.append(i[-1])
        style_id = list_dict.index(j)
        mv = _mov_avg(i)
        pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])

        for i in pt:
            if i > 5:
                a = pt.index(i)
                pt[a] = pt[a + 1] + 0.3

        a = list(range(0, len(mv)))
        ptx = a[0:len(a):int((len(a) / 10)) + 1]
        if ptx[-1] != a[-1]:
            ptx.append(a[-1])

        ax.plot(ptx,
                pt,
                style[style_id],
                linewidth=2,
                label=j)
    avg_set = avg_rtt(data)
    avg.append(avg_set)
    #print(avg_set)
    if mec == 4:
        ax.set_title(algo_dict[names[no]], fontdict=font)
    ax.set_xlabel('Time Period', fontdict=font1)
    if ax in ax_list:
        ax.set_ylabel('RTT (ms)', fontdict=font1)

    # ax.set_ylabel('RTT ')
    # ax.legend()
    ax.set_ylim(top=4.2)
    ax.set_ylim(bottom=0.5)
    axx = ax.twinx()
    axx.set_yticklabels([])
    axx.set_yticks([])
    if ax in axx_list:
        axx.set_ylabel(f'{axx_list[ax]} MECs', rotation=0, fontdict=font, labelpad=38)


def call_plot():
    axis = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18,
            ax19, ax20, ax21, ax22, ax23, ax24]
    data_plot = [data.rtt_1, data.rtt_3, data.rtt_5, data.rtt_8, data.rtt_11, data.rtt_16, data.rtt_1_5,
                 data.rtt_3_5, data.rtt_5_5, data.rtt_8_5, data.rtt_11_5, data.rtt_16_5, data.rtt_1_6,
                 data.rtt_3_6, data.rtt_5_6, data.rtt_8_6, data.rtt_11_6, data.rtt_16_6, rd.rtt_1_7,
                 rd.rtt_3_7, rd.rtt_5_7, rd.rtt_8_7, rd.rtt_11_7, rd.rtt_16_7]
    tp = [ax1, ax2, ax3, ax4, ax5, ax6]  # (plot_data, ax, no, mec)

    for i in range(len(axis)):
        if axis[i] in tp:
            k = 4
        else:
            k = 0  # k = mec
        if (i + 1) % 6 == 0:
            n = 5
        else:
            n = ((i + 1) % 6) -1  # n = no
        #print(f'k={k}, n={n}')
        plot_rtt(data_plot[i], axis[i], n, k)

    plt.show()


def avg_rtt(data):
    return sum(data)/len(data)


call_plot()


def cal_mec_avg():
    for i in avg:
        print(round(i, 3))
    n = 10
    print('*'*n + 'Average RTT for Algorithms' + '*'*n )
    for i in range(6):
        a = avg[i:len(avg)+1:6]
        print(f'{algo_dict[names[i]]}: ', sum(a)/len(a))


cal_mec_avg()