import matplotlib.pyplot as plt
from drawnow import *
import matplotlib.patches as patches

deadlock = [1]
fig = plt.figure()
ax1 = fig.add_subplot(111)


def plot_deadlock():
    cols = ['r']
    text = str(deadlock[-1] - 1) + " Deadlock resolved"
    wedges, texts, autotexts = plt.pie(deadlock, shadow=True, autopct=text,
                                       textprops=dict(rotation_mode='anchor', color="w", ha='left'), colors=cols)

    plt.setp(autotexts, size=9, weight="bold")

    #ax5.set_title("Deadlock Resolved Counter")
    plt.show()

# plot_deadlock()


def plot_test():
    name = ['Timely', 'Untimely']
    ypos = ([0, 1])
    timely = 80
    untimely = 20
    values = [timely, untimely]
    ax1.set_xticks(ypos)
    ax1.set_xticklabels(name)
    ax1.bar(ypos, values, align='center', color='m', alpha=0.5)
    dis = 'Seq: {}\nTotal Tasks: {}'.format(timely, untimely)
    ax1.text(1.1, 70, dis, bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8), ))

    plt.title('Task execution Time record')

    # ax1.annotate(dis, xy=(2, 1), xytext=(3, 1.5))

    plt.subplot(ax1)
    fig.suptitle('MEC Performance During Deadlock Experiment')
    plt.show()


def test():
    name = ['Timely', 'Untimely']
    ypos = ([0, 1])
    timely = 80
    untimely = 20
    values = [timely, untimely]
    plt.xticks(ypos, name)
    #plt.ylabel(name)
    dis = 'Seq: {}\nTotal Tasks: {}'.format(timely, untimely)
    '''
    plt.text(70, 5, dis, bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8), ))
    '''
    plt.bar(ypos, values, align='center', color='m', alpha=0.5)
    plt.text(1, 70, dis, size=10, rotation=0,
             ha="center", va="center",
             bbox=dict(boxstyle="round",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )

    plt.show()


def plot_offloaded_remote():
    keys = ['O-Out', 'Cloud', 'Local', 'O-In']
    # total = _off_mec + _off_cloud + _loc + _inward_mec

    val = [10,
           20,
           5,
           25]
    cols = ['r', 'g', 'b', 'm']
    ypos = ([0, 1, 2, 3])
    '''
    explode = []
    for i in val:
        if i == max(val):
            explode.append(0.1)
        else:
            explode.append(0)

    ax2.pie(val, labels=keys, autopct='%.3f%%', wedgeprops=dict(width=0.5), 
    startangle=-40, shadow=True, explode=explode, colors=cols)
    '''
    ax1.set_xticks(ypos)
    ax1.set_xticklabels(keys)
    ax1.bar(ypos, val, align='center', color=cols, alpha=0.3)
    ax1.text(-0.1, 10, '99%', bbox=dict(boxstyle="round",
                                   ec=(1., 0.5, 0.5),
                                   fc=(1., 0.8, 0.8), ))
    ax1.set_title('Remote vs Local Frequency')
    plt.subplot(ax1)
    plt.show()


def plot_rectangle():
    # build a rectangle in axes coords
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    # ax1.add_container([0, 0, 1, 1])
    # axes coordinates are 0,0 is bottom left and 1,1 is upper right
    p = patches.Rectangle(
        (left, bottom), width, height,
        fill=False, transform=ax1.transAxes, clip_on=False
    )

    #ax1.add_patch(p)
    '''
    ax1.text(0.5 * (left + right), 0.5 * (bottom + top), '0 Deadlock resolved',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=10, color='red',
             transform=ax1.transAxes)
    '''
    ax1.text(0.5, 0.6, '0 Deadlock resolved', rotation=0, size=15,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.),))
    ax1.text(0.5, 0.45, '100 Tasks Received', rotation=0, size=15,
             ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
    ax1.set_axis_off()
    plt.subplot(ax1)
    plt.show()


def p_test():
    # build a rectangle in axes coords
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    # axes coordinates are 0,0 is bottom left and 1,1 is upper right
    p = patches.Rectangle(
        (left, bottom), width, height,
        fill=False, transform=ax.transAxes, clip_on=False
    )

    ax.add_patch(p)
    ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'middle',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=20, color='red',
            transform=ax.transAxes)
    ax.set_axis_off()
    plt.show()
#drawnow(plot_test)
#drawnow(test)
#drawnow(plot_offloaded_remote)
drawnow(plot_rectangle)
#drawnow(p_test)