from drawnow import *
from matplotlib import pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)


def plot_offloaded_remote():
    keys = ['MEC', 'Cloud', 'Local']
    val = [_off_mec, _off_cloud, _loc]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax1.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax1.set_title('Remote vs Local Frequency')
    plt.subplot(ax1)

def plot_offloaded_remote():
    keys = ['MEC', 'Cloud', 'Local']
    val = [_off_mec, _off_cloud, _loc]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax1.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax1.set_title('Remote vs Local Frequency')
    plt.subplot(ax1)


def plot_offloaded_remote():
    keys = ['MEC', 'Cloud', 'Local']
    val = [_off_mec, _off_cloud, _loc]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax1.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax1.set_title('Remote vs Local Frequency')
    plt.subplot(ax1)


def plot_graphs():
    plot_offloaded_remote()
    plot_wait_time()
    plot_rtts()
    plot_cpu()
    fig.suptitle('MEC Performance During Deadlock Experiment')


def show_graphs():
    drawnow(plot_graphs)