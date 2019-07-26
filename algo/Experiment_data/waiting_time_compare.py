from drawnow import *
from matplotlib import pyplot as plt
import data

fig = plt.figure()
ax1 = fig.add_subplot(361)
ax2 = fig.add_subplot(362)
ax3 = fig.add_subplot(363)
ax4 = fig.add_subplot(364)
ax5 = fig.add_subplot(365)
ax6 = fig.add_subplot(366)
ax7 = fig.add_subplot(367)
ax8 = fig.add_subplot(368)
ax9 = fig.add_subplot(3,6,9)
ax10 = fig.add_subplot(3,6,10)
ax11 = fig.add_subplot(3,6,11)
ax12 = fig.add_subplot(3,6,12)
ax13 = fig.add_subplot(3,6,13)
ax14 = fig.add_subplot(3,6,14)
ax15 = fig.add_subplot(3,6,15)
ax16 = fig.add_subplot(3,6,16)
ax17 = fig.add_subplot(3,6,17)
ax18 = fig.add_subplot(3,6,18)

style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>']


def _mov_avg(a1):
    ma1=[] # moving average list
    avg1=0 # movinf average pointwise
    count=0
    for i in range(len(a1)):
        count+=1
        avg1=((count-1)*avg1+a1[i])/count
        ma1.append(avg1) #cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def one_four():
    ax1.grid(True)
    for i in data.wt_1:
        mv = _mov_avg(data.wt_1[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax1.plot(ptx,
                 pt,
                 style[list(data.wt_1.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax1.set_title('RMS + Bankers ')
    ax1.set_ylabel('Moving wt')
    ax1.set_xlabel('Time (seconds)')
    ax1.legend()
    plt.subplot(ax1)


def three_four():
    ax2.grid(True)
    for i in data.wt_3:
        mv = _mov_avg(data.wt_3[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax2.plot(ptx,
                 pt,
                 style[list(data.wt_3.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax2.set_title('EDF + Bankers')
    ax2.set_xlabel('Time (seconds)')
    ax2.legend()
    plt.subplot(ax2)


def five_four():
    ax3.grid(True)
    for i in data.wt_5:
        mv = _mov_avg(data.wt_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax3.plot(ptx,
                 pt,
                 style[list(data.wt_5.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax3.set_title('RMS + Wound Wait')
    ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


def eight_four():
    ax4.grid(True)
    for i in data.wt_8:
        mv = _mov_avg(data.wt_8[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax4.plot(ptx,
                 pt,
                 style[list(data.wt_8.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax4.set_title('RMS + Wait Die')
    ax4.set_xlabel('Time (seconds)')
    ax4.legend()
    plt.subplot(ax4)


def eleven_four():
    ax5.grid(True)
    for i in data.wt_11:
        mv = _mov_avg(data.wt_11[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax5.plot(ptx,
                 pt,
                 style[list(data.wt_11.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax5.set_title('EDF + Wound Wait')
    ax5.set_xlabel('Time (seconds)')
    ax5.legend()
    plt.subplot(ax5)


def sixteen_four():
    ax6.grid(True)
    for i in data.wt_16:
        mv = _mov_avg(data.wt_16[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax6.plot(ptx,
                 pt,
                 style[list(data.wt_16.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax6.set_title('EDF + Wait Die')
    ax6.set_xlabel('Time (seconds)')
    ax6.legend()
    plt.subplot(ax6)


def one_five():
    ax7.grid(True)
    for i in data.wt_1_5:
        mv = _mov_avg(data.wt_1_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax7.plot(ptx,
                 pt,
                 style[list(data.wt_1_5.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax7.set_ylabel('Moving wt')
    ax7.set_xlabel('Time (seconds)')
    ax7.legend()
    plt.subplot(ax7)


def three_five():
    ax8.grid(True)
    for i in data.wt_3_5:
        mv = _mov_avg(data.wt_3_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax8.plot(ptx,
                 pt,
                 style[list(data.wt_3_5.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax8.set_xlabel('Time (seconds)')
    ax8.legend()
    plt.subplot(ax8)


def five_five():
    ax9.grid(True)
    for i in data.wt_5_5:
        mv = _mov_avg(data.wt_5_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax9.plot(ptx,
                 pt,
                 style[list(data.wt_5_5.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax9.set_xlabel('Time (seconds)')
    ax9.legend()
    plt.subplot(ax9)


def eight_five():
    ax10.grid(True)
    for i in data.wt_8_5:
        mv = _mov_avg(data.wt_8_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax10.plot(ptx,
                  pt,
                  style[list(data.wt_8_5.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax10.set_xlabel('Time (seconds)')
    ax10.legend()
    plt.subplot(ax10)


def eleven_five():
    ax11.grid(True)
    for i in data.wt_11_5:
        mv = _mov_avg(data.wt_11_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax11.plot(ptx,
                  pt,
                  style[list(data.wt_11_5.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax11.set_xlabel('Time (seconds)')
    ax11.legend()
    plt.subplot(ax11)


def sixteen_five():
    ax12.grid(True)
    for i in data.wt_16_5:
        mv = _mov_avg(data.wt_16_5[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax12.plot(ptx,
                  pt,
                  style[list(data.wt_16_5.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax12.set_xlabel('Time (seconds)')
    ax12.legend()
    plt.subplot(ax12)


def one_six():
    ax13.grid(True)
    for i in data.wt_1_6:
        mv = _mov_avg(data.wt_1_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax13.plot(ptx,
                  pt,
                  style[list(data.wt_1_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax13.set_ylabel('Moving wt')
    ax13.set_xlabel('Time (seconds)')
    ax13.legend()
    plt.subplot(ax13)


def three_six():
    ax14.grid(True)
    for i in data.wt_3_6:
        mv = _mov_avg(data.wt_3_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax14.plot(ptx,
                  pt,
                  style[list(data.wt_3_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax14.set_xlabel('Time (seconds)')
    ax14.legend()
    plt.subplot(ax14)


def five_six():
    ax15.grid(True)
    for i in data.wt_5_6:
        mv = _mov_avg(data.wt_5_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax15.plot(ptx,
                  pt,
                  style[list(data.wt_5_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax15.set_xlabel('Time (seconds)')
    ax15.legend()
    plt.subplot(ax15)


def eight_six():
    ax16.grid(True)
    for i in data.wt_8_6:
        mv = _mov_avg(data.wt_8_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax16.plot(ptx,
                  pt,
                  style[list(data.wt_8_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax16.set_xlabel('Time (seconds)')
    ax16.legend()
    plt.subplot(ax16)


def eleven_six():
    ax17.grid(True)
    for i in data.wt_11_6:
        mv = _mov_avg(data.wt_11_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax17.plot(ptx,
                  pt,
                  style[list(data.wt_11_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax17.set_xlabel('Time (seconds)')
    ax17.legend()
    plt.subplot(ax17)


def sixteen_six():
    ax18.grid(True)
    for i in data.wt_16_6:
        mv = _mov_avg(data.wt_16_6[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax18.plot(ptx,
                  pt,
                  style[list(data.wt_16_6.keys()).index(i)],
                  linewidth=2,
                  label=i)
    ax18.set_xlabel('Time (seconds)')
    ax18.legend()
    plt.subplot(ax18)


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
    fig.suptitle('MEC Performance During Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()