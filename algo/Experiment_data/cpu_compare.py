from drawnow import *
from matplotlib import pyplot as plt
import data

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)


def four_mec():
    ax1.grid(True)
    ax1.plot(list(range(len(_mov_avg(_cpu)))), _mov_avg(_cpu), linewidth=2, label='CPU')
    ax1.set_title('Moving CPU Utilization')
    ax1.set_ylabel('Moving CPU')
    ax1.set_xlabel('Time (seconds)')
    ax1.fill_between(list(range(len(_mov_avg(_cpu)))), _mov_avg(_cpu), 0, alpha=0.5)
    ax1.legend()
    plt.subplot(ax4)