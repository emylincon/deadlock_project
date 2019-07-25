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
                 label=i)
    ax1.set_title('RTT Utilization over Time')
    ax1.set_ylabel('Moving RTT')
    ax1.set_xlabel('Time (seconds)')
    ax1.legend()
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
                 label=i)
    ax2.set_title('RTT Utilization over Time')
    ax2.set_ylabel('Moving RTT')
    ax2.set_xlabel('Time (seconds)')
    ax2.legend()
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
                 label=i)
    ax3.set_title('RTT Utilization over Time')
    ax3.set_ylabel('Moving RTT')
    ax3.set_xlabel('Time (seconds)')
    ax3.legend()
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
                 label=i)
    ax4.set_title('RTT Utilization over Time')
    ax4.set_ylabel('Moving RTT')
    ax4.set_xlabel('Time (seconds)')
    ax4.legend()
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
                 label=i)
    ax5.set_title('RTT Utilization over Time')
    ax5.set_ylabel('Moving RTT')
    ax5.set_xlabel('Time (seconds)')
    ax5.legend()
    plt.subplot(ax5)


def sixteen_four(a):
    ax6.grid(True)
    for i in data.rtt_16:
        mv = _mov_avg(data.rtt_1[i])
        pt = mv[0:len(mv):int((len(mv) / 7)) + 1]
        if pt[-1] != mv[-1]:
            pt.append(mv[-1])
        ptx = [mv.index(i) for i in pt]
        ax6.plot(ptx,
                 pt,
                 style[list(data.rtt_1.keys()).index(i)],
                 linewidth=2,
                 label=i)
    ax6.set_title('RTT Utilization over Time')
    ax6.set_ylabel('Moving RTT')
    ax6.set_xlabel('Time (seconds)')
    ax6.legend()
    plt.subplot(ax6)


def one_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec1_5, data.off_cloud1_5, data.loc1_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax7.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax7.set_title('Remote vs Local Frequency')
    plt.subplot(ax7)


def three_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec3_5, data.off_cloud3_5, data.loc3_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax8.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax8.set_title('Remote vs Local Frequency')
    plt.subplot(ax8)


def five_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec5_5, data.off_cloud5_5, data.loc5_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax9.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax9.set_title('Remote vs Local Frequency')
    plt.subplot(ax9)


def eight_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec8_5, data.off_cloud8_5, data.loc8_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax10.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax10.set_title('Remote vs Local Frequency')
    plt.subplot(ax10)


def eleven_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec11_5, data.off_cloud11_5, data.loc11_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax11.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax11.set_title('Remote vs Local Frequency')
    plt.subplot(ax11)


def sixteen_five():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec16_5, data.off_cloud16_5, data.loc16_5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax12.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax12.set_title('Remote vs Local Frequency')
    plt.subplot(ax12)


def one_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec1_6, data.off_cloud1_6, data.loc1_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax13.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax13.set_title('Remote vs Local Frequency')
    plt.subplot(ax13)


def three_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec3_6, data.off_cloud3_6, data.loc3_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax14.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax14.set_title('Remote vs Local Frequency')
    plt.subplot(ax14)


def five_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec5_6, data.off_cloud5_6, data.loc5_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax15.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax15.set_title('Remote vs Local Frequency')
    plt.subplot(ax15)


def eight_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec8_6, data.off_cloud8_6, data.loc8_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax16.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax16.set_title('Remote vs Local Frequency')
    plt.subplot(ax16)


def eleven_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec11_6, data.off_cloud11_6, data.loc11_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax17.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax17.set_title('Remote vs Local Frequency')
    plt.subplot(ax17)


def sixteen_six():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec16_6, data.off_cloud16_6, data.loc16_6]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax18.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    #ax18.set_title('Remote vs Local Frequency')
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