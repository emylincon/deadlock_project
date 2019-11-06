from drawnow import *
from matplotlib import pyplot as plt
import data
import cpu_redo as cp

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)


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


def four_mec():
    ax1.grid(True)
    ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_3), linewidth=2, label='EDF + Bankers')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_5), linewidth=2, label='RMS + wound wait')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_8), linewidth=2, label='RMS + wait die')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_11), linewidth=2, label='EDF + wound wait')
    ax1.plot(list(range(500)), _mov_avg(data.cpu_16), linewidth=2, label='EDF + wait die')

    ax1.set_title('Moving CPU Utilization for 4 MEC Set-up')
    ax1.set_ylabel('Moving CPU')
    ax1.set_xlabel('Time (seconds)')
    ax1.legend()
    plt.subplot(ax1)


def five_mec():
    ax2.grid(True)
    #ax2.plot(list(range(500)), _mov_avg(data.cpu_1_5), linewidth=2, label='RMS + Bankers')
    ax2.plot(list(range(500)), _mov_avg(cp.cpu_1_5), linewidth=2, label='RMS + Bankers')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_3_5), linewidth=2, label='EDF + Bankers')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_5_5), linewidth=2, label='RMS + wound wait')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_8_5), linewidth=2, label='RMS + wait die')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_11_5), linewidth=2, label='EDF + wound wait')
    ax2.plot(list(range(500)), _mov_avg(data.cpu_16_5), linewidth=2, label='EDF + wait die')

    ax2.set_title('Moving CPU Utilization for 5 MEC Set-up')
    ax2.set_ylabel('Moving CPU')
    ax2.set_xlabel('Time (seconds)')
    ax2.legend()
    plt.subplot(ax2)


def six_mec():
    ax3.grid(True)
    ax3.plot(list(range(500)), _mov_avg(data.cpu_1_6), linewidth=2, label='RMS + Bankers')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_3_6), linewidth=2, label='EDF + Bankers')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_5_6), linewidth=2, label='RMS + wound wait')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_8_6), linewidth=2, label='RMS + wait die')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_11_6), linewidth=2, label='EDF + wound wait')
    ax3.plot(list(range(500)), _mov_avg(data.cpu_16_6), linewidth=2, label='EDF + wait die')

    ax3.set_title('Moving CPU Utilization for 6 MEC Set-up')
    ax3.set_ylabel('Moving CPU')
    ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


def plot_graphs():
    four_mec()
    five_mec()
    six_mec()
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()
