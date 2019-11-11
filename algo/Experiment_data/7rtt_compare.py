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


def one_four():
    ax1.grid(True)
    for i in data.rtt_1:
        mv = _mov_avg(data.rtt_1[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax1.plot(ptx,
                 pt,
                 style[list(data.rtt_1.keys()).index(i)],
                 linewidth=2,
                 )
    ax1.set_title('RMS + Bankers ')
    # ax1.set_ylabel('Moving RTT')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel(f'4 MECs', rotation=0, fontsize=15, labelpad=30)
    # ax1.legend()
    plt.subplot(ax1)


def three_four():
    ax2.grid(True)
    for i in data.rtt_3:
        mv = _mov_avg(data.rtt_3[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax2.plot(ptx,
                 pt,
                 style[list(data.rtt_3.keys()).index(i)],
                 linewidth=2,
                 )
    ax2.set_title('EDF + Bankers')
    ax2.set_xlabel('Time (seconds)')
    # ax2.legend()
    plt.subplot(ax2)


def five_four():
    ax3.grid(True)
    for i in data.rtt_5:
        mv = _mov_avg(data.rtt_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax3.plot(ptx,
                 pt,
                 style[list(data.rtt_5.keys()).index(i)],
                 linewidth=2,
                 )
    ax3.set_title('RMS + Wound Wait')
    ax3.set_xlabel('Time (seconds)')
    # ax3.legend()
    plt.subplot(ax3)


def eight_four():
    ax4.grid(True)
    for i in data.rtt_8:
        mv = _mov_avg(data.rtt_8[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax4.plot(ptx,
                 pt,
                 style[list(data.rtt_8.keys()).index(i)],
                 linewidth=2,
                 )
    ax4.set_title('RMS + Wait Die')
    ax4.set_xlabel('Time (seconds)')
    # ax4.legend()
    plt.subplot(ax4)


def eleven_four():
    ax5.grid(True)
    for i in data.rtt_11:
        mv = _mov_avg(data.rtt_11[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax5.plot(ptx,
                 pt,
                 style[list(data.rtt_11.keys()).index(i)],
                 linewidth=2,
                 )
    ax5.set_title('EDF + Wound Wait')
    ax5.set_xlabel('Time (seconds)')
    # ax5.legend()
    plt.subplot(ax5)


def sixteen_four():
    ax6.grid(True)
    for i in data.rtt_16:
        mv = _mov_avg(data.rtt_16[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax6.plot(ptx,
                 pt,
                 style[list(data.rtt_16.keys()).index(i)],
                 linewidth=2,
                 )
    ax6.set_title('EDF + Wait Die')
    ax6.set_xlabel('Time (seconds)')
    # ax6.legend()
    plt.subplot(ax6)


def one_five():
    ax7.grid(True)
    for i in data.rtt_1_5:
        mv = _mov_avg(data.rtt_1_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax7.plot(ptx,
                 pt,
                 style[list(data.rtt_1_5.keys()).index(i)],
                 linewidth=2,
                 )
    # ax7.set_ylabel('Moving RTT')
    ax7.set_xlabel('Time (seconds)')
    ax7.set_ylabel(f'5 MECs', rotation=0, fontsize=15, labelpad=30)
    # ax7.legend()
    plt.subplot(ax7)


def three_five():
    ax8.grid(True)
    for i in data.rtt_3_5:
        mv = _mov_avg(data.rtt_3_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax8.plot(ptx,
                 pt,
                 style[list(data.rtt_3_5.keys()).index(i)],
                 linewidth=2,
                 )
    ax8.set_xlabel('Time (seconds)')
    # ax8.legend()
    plt.subplot(ax8)


def five_five():
    ax9.grid(True)
    for i in data.rtt_5_5:
        mv = _mov_avg(data.rtt_5_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax9.plot(ptx,
                 pt,
                 style[list(data.rtt_5_5.keys()).index(i)],
                 linewidth=2,
                 )
    ax9.set_xlabel('Time (seconds)')
    # ax9.legend()
    plt.subplot(ax9)


def eight_five():
    ax10.grid(True)
    for i in data.rtt_8_5:
        mv = _mov_avg(data.rtt_8_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax10.plot(ptx,
                  pt,
                  style[list(data.rtt_8_5.keys()).index(i)],
                  linewidth=2,
                  )
    ax10.set_xlabel('Time (seconds)')
    # ax10.legend()
    plt.subplot(ax10)


def eleven_five():
    ax11.grid(True)
    for i in data.rtt_11_5:
        mv = _mov_avg(data.rtt_11_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax11.plot(ptx,
                  pt,
                  style[list(data.rtt_11_5.keys()).index(i)],
                  linewidth=2,
                  )
    ax11.set_xlabel('Time (seconds)')
    # ax11.legend()
    plt.subplot(ax11)


def sixteen_five():
    ax12.grid(True)
    for i in data.rtt_16_5:
        mv = _mov_avg(data.rtt_16_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax12.plot(ptx,
                  pt,
                  style[list(data.rtt_16_5.keys()).index(i)],
                  linewidth=2,
                  )
    ax12.set_xlabel('Time (seconds)')
    # ax12.legend()
    plt.subplot(ax12)


def one_six():
    ax13.grid(True)
    for i in data.rtt_1_6:
        mv = _mov_avg(data.rtt_1_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax13.plot(ptx,
                  pt,
                  style[list(data.rtt_1_6.keys()).index(i)],
                  linewidth=2,
                  )
    # ax13.set_ylabel('Moving RTT')
    ax13.set_xlabel('Time (seconds)')
    ax13.set_ylabel(f'6 MECs', rotation=0, fontsize=15, labelpad=30)
    # ax13.legend()
    plt.subplot(ax13)


def three_six():
    ax14.grid(True)
    for i in data.rtt_3_6:
        mv = _mov_avg(data.rtt_3_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax14.plot(ptx,
                  pt,
                  style[list(data.rtt_3_6.keys()).index(i)],
                  linewidth=2,
                  )
    ax14.set_xlabel('Time (seconds)')
    # ax14.legend()
    plt.subplot(ax14)


def five_six():
    ax15.grid(True)
    for i in data.rtt_5_6:
        mv = _mov_avg(data.rtt_5_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax15.plot(ptx,
                  pt,
                  style[list(data.rtt_5_6.keys()).index(i)],
                  linewidth=2,
                  )
    ax15.set_xlabel('Time (seconds)')
    # ax15.legend()
    plt.subplot(ax15)


def eight_six():
    ax16.grid(True)
    for i in data.rtt_8_6:
        mv = _mov_avg(data.rtt_8_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax16.plot(ptx,
                  pt,
                  style[list(data.rtt_8_6.keys()).index(i)],
                  linewidth=2,
                  )
    ax16.set_xlabel('Time (seconds)')
    # ax16.legend()
    plt.subplot(ax16)


def eleven_six():
    ax17.grid(True)
    for i in data.rtt_11_6:
        mv = _mov_avg(data.rtt_11_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax17.plot(ptx,
                  pt,
                  style[list(data.rtt_11_6.keys()).index(i)],
                  linewidth=2,
                  )
    ax17.set_xlabel('Time (seconds)')
    # ax17.legend()
    plt.subplot(ax17)


def sixteen_six():
    ax18.grid(True)
    for i in data.rtt_16_6:
        mv = _mov_avg(data.rtt_16_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax18.plot(ptx,
                  pt,
                  style[list(data.rtt_16_6.keys()).index(i)],
                  linewidth=2,
                  )
    ax18.set_xlabel('Time (seconds)')
    # ax18.legend()
    plt.subplot(ax18)


def one_seven():
    ax19.grid(True)
    for i in rd.rtt_1_7:
        mv = _mov_avg(rd.rtt_1_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax19.plot(ptx,
                  pt,
                  style[list(rd.rtt_1_7.keys()).index(i)],
                  linewidth=2,
                  )
    # ax19.set_ylabel('Moving RTT')
    ax19.set_xlabel('Time (seconds)')
    ax19.set_ylabel(f'7 MECs', rotation=0, fontsize=15, labelpad=30)
    # ax19.legend()
    plt.subplot(ax19)


def three_seven():
    ax20.grid(True)
    for i in rd.rtt_3_7:
        mv = _mov_avg(rd.rtt_3_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax20.plot(ptx,
                  pt,
                  style[list(rd.rtt_3_7.keys()).index(i)],
                  linewidth=2,
                  )
    ax20.set_xlabel('Time (seconds)')
    # ax20.legend()
    plt.subplot(ax20)


def five_seven():
    ax21.grid(True)
    for i in rd.rtt_5_7:
        mv = _mov_avg(rd.rtt_5_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax21.plot(ptx,
                  pt,
                  style[list(rd.rtt_5_7.keys()).index(i)],
                  linewidth=2,
                  )
    ax21.set_xlabel('Time (seconds)')
    # ax21.legend()
    plt.subplot(ax21)


def eight_seven():
    ax22.grid(True)
    for i in rd.rtt_8_7:
        mv = _mov_avg(rd.rtt_8_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax22.plot(ptx,
                  pt,
                  style[list(rd.rtt_8_7.keys()).index(i)],
                  linewidth=2,
                  )
    ax22.set_xlabel('Time (seconds)')
    # ax22.legend()
    plt.subplot(ax22)


def eleven_seven():
    ax23.grid(True)
    for i in rd.rtt_11_7:
        mv = _mov_avg(rd.rtt_11_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax23.plot(ptx,
                  pt,
                  style[list(rd.rtt_11_7.keys()).index(i)],
                  linewidth=2,
                  )
    ax23.set_xlabel('Time (seconds)')
    # ax23.legend()
    plt.subplot(ax23)


def sixteen_seven():
    ax24.grid(True)
    for i in rd.rtt_16_7:
        mv = _mov_avg(rd.rtt_16_7[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax24.plot(ptx,
                  pt,
                  style[list(rd.rtt_16_7.keys()).index(i)],
                  linewidth=2,
                  )
    ax24.set_xlabel('Time (seconds)')
    # ax24.legend()
    plt.subplot(ax24)


def plot_graphs():
    one_four()
    three_four()
    five_four()
    eight_four()
    eleven_four()
    sixteen_four()
    one_five()
    three_five()
    five_five()
    eight_five()
    eleven_five()
    sixteen_five()
    one_six()
    three_six()
    five_six()
    eight_six()
    eleven_six()
    sixteen_six()
    one_seven()
    three_seven()
    five_seven()
    eight_seven()
    eleven_seven()
    sixteen_seven()
    fig.suptitle('MEC RTT Performance During Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()