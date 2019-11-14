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


def one_four():
    keys = ['offload', 'Local']
    val = [data.off_mec1 + data.off_cloud1, data.loc1]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax1.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax1.set_ylabel(f'4 MECs', rotation=0, fontsize=15, labelpad=40)
    ax1.set_title('RMS + Bankers ')
    plt.subplot(ax1)


def three_four():
    keys = ['offload', 'Local']
    val = [data.off_mec3 + data.off_cloud3, data.loc3]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax2.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax2.set_title('EDF + Bankers')
    plt.subplot(ax2)


def five_four():
    keys = ['offload', 'Local']
    val = [data.off_mec5 + data.off_cloud5, data.loc5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax3.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax3.set_title('RMS + Wound Wait')
    plt.subplot(ax3)


def eight_four():
    keys = ['offload', 'Local']
    val = [data.off_mec8 + data.off_cloud8, data.loc8]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax4.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax4.set_title('RMS + Wait Die')
    plt.subplot(ax4)


def eleven_four():
    keys = ['offload', 'Local']
    val = [data.off_mec11 + data.off_cloud11, data.loc11]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax5.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax5.set_title('EDF + Wound Wait')
    plt.subplot(ax5)


def sixteen_four():
    keys = ['offload', 'Local']
    val = [data.off_mec16 + data.off_cloud16, data.loc16]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax6.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax6.set_title('EDF + Wait Die')
    plt.subplot(ax6)


def one_five():
    keys = ['offload', 'Local']
    val = [data.off_mec1_5 + data.off_cloud1_5, data.loc1_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax7.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax7.set_ylabel(f'5 MECs', rotation=0, fontsize=15, labelpad=40)
    # ax7.set_title('Remote vs Local Frequency')
    plt.subplot(ax7)


def three_five():
    keys = ['offload', 'Local']
    val = [data.off_mec3_6 + data.off_cloud3_6, data.loc3_6]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax8.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax8.set_title('Remote vs Local Frequency')
    plt.subplot(ax8)


def five_five():
    keys = ['offload', 'Local']
    val = [data.off_mec5_5 + data.off_cloud5_5, data.loc5_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax9.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax9.set_title('Remote vs Local Frequency')
    plt.subplot(ax9)


def eight_five():
    keys = ['offload', 'Local']
    val = [data.off_mec8_6 + data.off_cloud8_6, data.loc8_6]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax10.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax10.set_title('Remote vs Local Frequency')
    plt.subplot(ax10)


def eleven_five():
    keys = ['offload', 'Local']
    val = [data.off_mec11_6 + data.off_cloud11_6, data.loc11_6]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax11.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax11.set_title('Remote vs Local Frequency')
    plt.subplot(ax11)


def sixteen_five():
    keys = ['offload', 'Local']
    val = [rd.off_mec16_7 + rd.off_cloud16_7, rd.loc16_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax12.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax12.set_title('Remote vs Local Frequency')
    plt.subplot(ax12)


def one_six():
    keys = ['offload', 'Local']
    val = [rd.off_mec1_7 + rd.off_cloud1_7, rd.loc1_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax13.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax13.set_ylabel(f'6 MECs', rotation=0, fontsize=15, labelpad=40)
    # ax13.set_title('Remote vs Local Frequency')
    plt.subplot(ax13)


def three_six():
    keys = ['offload', 'Local']
    val = [rd.off_mec3_7 + rd.off_cloud3_7, rd.loc3_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax14.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax14.set_title('Remote vs Local Frequency')
    plt.subplot(ax14)


def five_six():
    keys = ['offload', 'Local']
    val = [rd.off_mec5_7 + rd.off_cloud5_7, rd.loc5_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax15.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax15.set_title('Remote vs Local Frequency')
    plt.subplot(ax15)


def eight_six():
    keys = ['offload', 'Local']
    val = [data.off_mec8_5 + data.off_cloud8_5, data.loc8_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax16.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax16.set_title('Remote vs Local Frequency')
    plt.subplot(ax16)


def eleven_six():
    keys = ['offload', 'Local']
    val = [rd.off_mec11_7 + rd.off_cloud11_7, rd.loc11_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax17.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax17.set_title('Remote vs Local Frequency')
    plt.subplot(ax17)


def sixteen_six():
    keys = ['offload', 'Local']
    val = [data.off_mec16_6 + data.off_cloud16_6, data.loc16_6]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax18.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax18.set_title('Remote vs Local Frequency')
    plt.subplot(ax18)


def one_seven():
    keys = ['offload', 'Local']
    val = [data.off_mec1_6 + data.off_cloud1_6, data.loc1_6]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax19.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    ax19.set_ylabel(f'7 MECs', rotation=0, fontsize=15, labelpad=40)
    # ax19.set_title('Remote vs Local Frequency')
    plt.subplot(ax19)


def three_seven():
    keys = ['offload', 'Local']
    val = [data.off_mec3_5 + data.off_cloud3_5, data.loc3_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax20.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax14.set_title('Remote vs Local Frequency')
    plt.subplot(ax20)


def five_seven():
    keys = ['offload', 'Local']
    val = [data.off_mec5_5 + data.off_cloud5_5, data.loc5_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax21.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax15.set_title('Remote vs Local Frequency')
    plt.subplot(ax21)


def eight_seven():
    keys = ['offload', 'Local']
    val = [rd.off_mec8_7 + rd.off_cloud8_7, rd.loc8_7]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax22.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax16.set_title('Remote vs Local Frequency')
    plt.subplot(ax22)


def eleven_seven():
    keys = ['offload', 'Local']
    val = [data.off_mec11_5 + data.off_cloud11_5, data.loc11_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax23.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax17.set_title('Remote vs Local Frequency')
    plt.subplot(ax23)


def sixteen_seven():
    keys = ['offload', 'Local']
    val = [data.off_mec16_5 + data.off_cloud16_5, data.loc16_5]
    cols = ['r', 'g']
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax24.pie(val, labels=keys, autopct='%.3f%%', shadow=True, explode=explode, colors=cols)
    # ax18.set_title('Remote vs Local Frequency')
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
    fig.suptitle('MEC Performance During Deadlock Experiment')
    plt.show()


def show_graphs():
    drawnow(plot_graphs)


show_graphs()
