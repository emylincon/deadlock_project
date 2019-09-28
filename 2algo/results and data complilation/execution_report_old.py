import matplotlib.pyplot as plt
import results_data as rd

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
ax10 = fig.add_subplot(3, 6, 10)
ax11 = fig.add_subplot(3, 6, 11)
ax12 = fig.add_subplot(3, 6, 12)
ax13 = fig.add_subplot(3, 6, 13)
ax14 = fig.add_subplot(3, 6, 14)
ax15 = fig.add_subplot(3, 6, 15)
ax16 = fig.add_subplot(3, 6, 16)
ax17 = fig.add_subplot(3, 6, 17)
ax18 = fig.add_subplot(3, 6, 18)


_loc_ = {
    24: [rd.loc0_2_4, rd.loc1_2_4, rd.loc2_2_4, rd.loc3_2_4],
    25: [rd.loc0_2_5, rd.loc1_2_5, rd.loc2_2_5, rd.loc3_2_5, rd.loc4_2_5, ],
    26: [rd.loc0_2_6, rd.loc1_2_6, rd.loc2_2_6, rd.loc3_2_6, rd.loc4_2_6, rd.loc5_2_6],

    34: [rd.loc0_3_4, rd.loc1_3_4, rd.loc2_3_4, rd.loc3_3_4],
    35: [rd.loc0_3_5, rd.loc1_3_5, rd.loc2_3_5, rd.loc3_3_5, rd.loc4_3_5],
    36: [rd.loc0_3_6, rd.loc1_3_6, rd.loc2_3_6, rd.loc3_3_6, rd.loc4_3_6, rd.loc5_3_6],

    74: [rd.loc0_7_4, rd.loc1_7_4, rd.loc2_7_4, rd.loc3_7_4],
    75: [rd.loc0_7_5, rd.loc1_7_5, rd.loc2_7_5, rd.loc3_7_5, rd.loc4_7_5],
    76: [rd.loc0_7_6, rd.loc1_7_6, rd.loc2_7_6, rd.loc3_7_6, rd.loc4_7_6, rd.loc5_7_6],

    104: [rd.loc0_10_4, rd.loc1_10_4, rd.loc2_10_4, rd.loc3_10_4],
    105: [rd.loc0_10_5, rd.loc1_10_5, rd.loc2_10_5, rd.loc3_10_5, rd.loc4_10_5],
    106: [rd.loc0_10_6, rd.loc1_10_6, rd.loc2_10_6, rd.loc3_10_6, rd.loc4_10_6, rd.loc5_10_6],

    124: [rd.loc0_12_4, rd.loc1_12_4, rd.loc2_12_4, rd.loc3_12_4],
    125: [rd.loc0_12_5, rd.loc1_12_5, rd.loc2_12_5, rd.loc3_12_5, rd.loc4_12_5],
    126: [rd.loc0_12_6, rd.loc1_12_6, rd.loc2_12_6, rd.loc3_12_6, rd.loc4_12_6, rd.loc5_12_6],

    164: [rd.loc0_16_4, rd.loc1_16_4, rd.loc2_16_4, rd.loc3_16_4],
    165: [rd.loc0_16_5, rd.loc1_16_5, rd.loc2_16_5, rd.loc3_16_5, rd.loc4_16_5],
    166: [rd.loc0_16_6, rd.loc1_16_6, rd.loc2_16_6, rd.loc3_16_6, rd.loc4_16_6, rd.loc5_16_6],
}

_off_cloud_ = {
    24: [rd.off_cloud0_2_4, rd.off_cloud1_2_4, rd.off_cloud2_2_4, rd.off_cloud3_2_4],
    25: [rd.off_cloud0_2_5, rd.off_cloud1_2_5, rd.off_cloud2_2_5, rd.off_cloud3_2_5, rd.off_cloud4_2_5, ],
    26: [rd.off_cloud0_2_6, rd.off_cloud1_2_6, rd.off_cloud2_2_6, rd.off_cloud3_2_6, rd.off_cloud4_2_6,
         rd.off_cloud5_2_6],

    34: [rd.off_cloud0_3_4, rd.off_cloud1_3_4, rd.off_cloud2_3_4, rd.off_cloud3_3_4],
    35: [rd.off_cloud0_3_5, rd.off_cloud1_3_5, rd.off_cloud2_3_5, rd.off_cloud3_3_5, rd.off_cloud4_3_5],
    36: [rd.off_cloud0_3_6, rd.off_cloud1_3_6, rd.off_cloud2_3_6, rd.off_cloud3_3_6, rd.off_cloud4_3_6,
         rd.off_cloud5_3_6],

    74: [rd.off_cloud0_7_4, rd.off_cloud1_7_4, rd.off_cloud2_7_4, rd.off_cloud3_7_4],
    75: [rd.off_cloud0_7_5, rd.off_cloud1_7_5, rd.off_cloud2_7_5, rd.off_cloud3_7_5, rd.off_cloud4_7_5],
    76: [rd.off_cloud0_7_6, rd.off_cloud1_7_6, rd.off_cloud2_7_6, rd.off_cloud3_7_6, rd.off_cloud4_7_6,
         rd.off_cloud5_7_6],

    104: [rd.off_cloud0_10_4, rd.off_cloud1_10_4, rd.off_cloud2_10_4, rd.off_cloud3_10_4],
    105: [rd.off_cloud0_10_5, rd.off_cloud1_10_5, rd.off_cloud2_10_5, rd.off_cloud3_10_5, rd.off_cloud4_10_5],
    106: [rd.off_cloud0_10_6, rd.off_cloud1_10_6, rd.off_cloud2_10_6, rd.off_cloud3_10_6, rd.off_cloud4_10_6,
          rd.off_cloud5_10_6],

    124: [rd.off_cloud0_12_4, rd.off_cloud1_12_4, rd.off_cloud2_12_4, rd.off_cloud3_12_4],
    125: [rd.off_cloud0_12_5, rd.off_cloud1_12_5, rd.off_cloud2_12_5, rd.off_cloud3_12_5, rd.off_cloud4_12_5],
    126: [rd.off_cloud0_12_6, rd.off_cloud1_12_6, rd.off_cloud2_12_6, rd.off_cloud3_12_6, rd.off_cloud4_12_6,
          rd.off_cloud5_12_6],

    164: [rd.off_cloud0_16_4, rd.off_cloud1_16_4, rd.off_cloud2_16_4, rd.off_cloud3_16_4],
    165: [rd.off_cloud0_16_5, rd.off_cloud1_16_5, rd.off_cloud2_16_5, rd.off_cloud3_16_5, rd.off_cloud4_16_5],
    166: [rd.off_cloud0_16_6, rd.off_cloud1_16_6, rd.off_cloud2_16_6, rd.off_cloud3_16_6, rd.off_cloud4_16_6,
          rd.off_cloud5_16_6]
}

_off_mec_ = {
    24: [rd.off_mec0_2_4, rd.off_mec1_2_4, rd.off_mec2_2_4, rd.off_mec3_2_4],
    25: [rd.off_mec0_2_5, rd.off_mec1_2_5, rd.off_mec2_2_5, rd.off_mec3_2_5, rd.off_mec4_2_5, ],
    26: [rd.off_mec0_2_6, rd.off_mec1_2_6, rd.off_mec2_2_6, rd.off_mec3_2_6, rd.off_mec4_2_6, rd.off_mec5_2_6],

    34: [rd.off_mec0_3_4, rd.off_mec1_3_4, rd.off_mec2_3_4, rd.off_mec3_3_4],
    35: [rd.off_mec0_3_5, rd.off_mec1_3_5, rd.off_mec2_3_5, rd.off_mec3_3_5, rd.off_mec4_3_5],
    36: [rd.off_mec0_3_6, rd.off_mec1_3_6, rd.off_mec2_3_6, rd.off_mec3_3_6, rd.off_mec4_3_6, rd.off_mec5_3_6],

    74: [rd.off_mec0_7_4, rd.off_mec1_7_4, rd.off_mec2_7_4, rd.off_mec3_7_4],
    75: [rd.off_mec0_7_5, rd.off_mec1_7_5, rd.off_mec2_7_5, rd.off_mec3_7_5, rd.off_mec4_7_5],
    76: [rd.off_mec0_7_6, rd.off_mec1_7_6, rd.off_mec2_7_6, rd.off_mec3_7_6, rd.off_mec4_7_6, rd.off_mec5_7_6],

    104: [rd.off_mec0_10_4, rd.off_mec1_10_4, rd.off_mec2_10_4, rd.off_mec3_10_4],
    105: [rd.off_mec0_10_5, rd.off_mec1_10_5, rd.off_mec2_10_5, rd.off_mec3_10_5, rd.off_mec4_10_5],
    106: [rd.off_mec0_10_6, rd.off_mec1_10_6, rd.off_mec2_10_6, rd.off_mec3_10_6, rd.off_mec4_10_6, rd.off_mec5_10_6],

    124: [rd.off_mec0_12_4, rd.off_mec1_12_4, rd.off_mec2_12_4, rd.off_mec3_12_4],
    125: [rd.off_mec0_12_5, rd.off_mec1_12_5, rd.off_mec2_12_5, rd.off_mec3_12_5, rd.off_mec4_12_5],
    126: [rd.off_mec0_12_6, rd.off_mec1_12_6, rd.off_mec2_12_6, rd.off_mec3_12_6, rd.off_mec4_12_6, rd.off_mec5_12_6],

    164: [rd.off_mec0_16_4, rd.off_mec1_16_4, rd.off_mec2_16_4, rd.off_mec3_16_4],
    165: [rd.off_mec0_16_5, rd.off_mec1_16_5, rd.off_mec2_16_5, rd.off_mec3_16_5, rd.off_mec4_16_5],
    166: [rd.off_mec0_16_6, rd.off_mec1_16_6, rd.off_mec2_16_6, rd.off_mec3_16_6, rd.off_mec4_16_6, rd.off_mec5_16_6],

}


_data_ = [_off_mec_, _loc_, _off_cloud_]    # _inward_mec_]


def sum_data():
    off_mec = {}
    off_cloud = {}
    loc = {}
    inward_mec = {}
    d_list = [off_mec, loc, off_cloud]     # inward_mec]
    t = 0
    for data in _data_:
        name = d_list[t]
        for key in data:
            name[key] = sum(data[key])
        t += 1

    # print(d_list)
    return d_list


def format_data(d_dict):
    t_data = {}
    _keys = list(d_dict.keys())
    s4 = 0
    s5 = 1
    s6 = 2
    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(d_dict[j])

                s4 += 4
            else:
                t_data[4] = [d_dict[j]]

                s4 += 4
        elif i == s5:
            if 5 in t_data:
                t_data[5].append(d_dict[j])

                s5 += 4
            else:
                t_data[5] = [d_dict[j]]

                s5 += 4
        elif i == s6:
            if 6 in t_data:
                t_data[6].append(d_dict[j])

                s6 += 4
            else:
                t_data[6] = [d_dict[j]]

                s6 += 4


    return t_data


def group_format(data_list):
    format_list = []
    for i in data_list:
        format_list.append(format_data(i))

    group_list = {4: {},
                  5: {},
                  6: {},
                  }

    for i in format_list:
        for j in i:
            _list_ = i[j]
            for key in range(len(_list_)):
                value = _list_[key]
                d_dict = group_list[j]
                if key in d_dict:
                    d_dict[key].append(value)
                else:
                    d_dict[key] = [value]

    # print("Grouplist: ", group_list)
    # print(f"format_list: {format_list}")

    return group_list


def percent(value, total):
    if value > 0:
        return round((value / total) * 100, 2)
    else:
        return 0


def plot_offloaded_remote(data_list, ax, _id_):
    # data_list =  [off_mec, off_cloud, loc, inward_mec]
    ax_list = {ax1: 4, ax7: 5, ax13: 6}
    title = [ax1, ax2, ax3, ax4, ax5, ax6]
    names = ('RMS + Bankers',
             'EDF + Bankers',
             'RMS + wound wait',
             'RMS + wait die',
             'EDF + wound wait',
             'EDF + wait die')

    keys = ['off-mec', 'Local', 'Cloud']     # , 'O-In']
    total = sum(data_list)

    val = [percent(data_list[0], total),
           percent(data_list[1], total),
           percent(data_list[2], total)]      # percent(data_list[3], total)]
    cols = ['r', 'g', 'b']      # , 'm']
    ypos = ([0, 1, 2])         # , 3])

    values = data_list
    # print(values)
    for i in values:
        j = values.index(i)
        # print(j)
        ax.text(j - 0.1, values[j], '{}%'.format(val[j]), rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax.set_xticks(ypos)
    ax.set_xticklabels(keys)
    ax.bar(ypos, values, align='center', color=cols, alpha=0.3)
    if ax in ax_list:
        ax.set_ylabel(f'{ax_list[ax]} MECs', rotation=0, fontsize=15, labelpad=30)

    if ax in title:
        ax.set_title(names[_id_])
    plt.subplot(ax)


def plot_av_times():
    axes = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18]
    _data = group_format(sum_data())
    # plot_offloaded_remote(data_list, ax, _id_)
    no = 0
    for i in _data:
        # i = keys 4 5 6 7
        for j in _data[i]:
            # _data[i] = dictionary => {0: [], 1: [] ...}
            data_plot = _data[i][j]
            plot_offloaded_remote(data_plot, axes[no], j)
            no += 1
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()


plot_av_times()
# group_format(sum_data())
# print("data: ", _data_)