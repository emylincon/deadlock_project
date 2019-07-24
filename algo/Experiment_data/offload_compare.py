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
ax9 = fig.add_subplot(369)
#ax10 = fig.add_subplot(3610)


def one_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec1, data.off_cloud1, data.loc1]
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


def three_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec3, data.off_cloud3, data.loc3]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax2.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax2.set_title('Remote vs Local Frequency')
    plt.subplot(ax2)


def five_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec5, data.off_cloud5, data.loc5]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax3.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax3.set_title('Remote vs Local Frequency')
    plt.subplot(ax3)


def eight_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec8, data.off_cloud8, data.loc8]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax4.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax4.set_title('Remote vs Local Frequency')
    plt.subplot(ax4)


def eleven_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec11, data.off_cloud11, data.loc11]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax5.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax5.set_title('Remote vs Local Frequency')
    plt.subplot(ax5)


def sixteen_four():
    keys = ['MEC', 'Cloud', 'Local']
    val = [data.off_mec16, data.off_cloud16, data.loc16]
    cols = ['r', 'g', 'b']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax6.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax6.set_title('Remote vs Local Frequency')
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
    ax7.set_title('Remote vs Local Frequency')
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
    ax8.set_title('Remote vs Local Frequency')
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
    ax9.set_title('Remote vs Local Frequency')
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
    ax10.set_title('Remote vs Local Frequency')
    plt.subplot(ax10)


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
    #eight_five()
    fig.suptitle('MEC Performance During Deadlock Experiment')


def show_graphs():
    drawnow(plot_graphs)

show_graphs()