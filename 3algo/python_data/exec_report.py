import matplotlib.pyplot as plt
from data_het.client_data import *

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

_local_timely = {
    24: timely_4_2_4['local'] + timely_5_2_4['local'] + timely_6_2_4['local'],
    27: timely_4_2_7['local'] + timely_5_2_7['local'] + timely_6_2_7['local'],
    210: timely_4_2_10['local'] + timely_5_2_10['local'] + timely_6_2_10['local'],

    34: timely_4_3_4['local'] + timely_5_3_4['local'] + timely_6_3_4['local'],
    37: timely_4_3_7['local'] + timely_5_3_7['local'] + timely_6_3_7['local'],
    310: timely_4_3_10['local'] + timely_5_3_10['local'] + timely_6_3_10['local'],

    74: timely_4_7_4['local'] + timely_5_7_4['local'] + timely_6_7_4['local'],
    77: timely_4_7_7['local'] + timely_5_7_7['local'] + timely_6_7_7['local'],
    710: timely_4_7_10['local'] + timely_5_7_10['local'] + timely_6_7_10['local'],

    104: timely_4_10_4['local'] + timely_5_10_4['local'] + timely_6_10_4['local'],
    107: timely_4_10_7['local'] + timely_5_10_7['local'] + timely_6_10_7['local'],
    1010: timely_4_10_10['local'] + timely_5_10_10['local'] + timely_6_10_10['local'],

    124: timely_4_12_4['local'] + timely_5_12_4['local'] + timely_6_12_4['local'],
    127: timely_4_12_7['local'] + timely_5_12_7['local'] + timely_6_12_7['local'],
    1210: timely_4_12_10['local'] + timely_5_12_10['local'] + timely_6_12_10['local'],

    164: timely_4_16_4['local'] + timely_5_16_4['local'] + timely_6_16_4['local'],
    167: timely_4_16_7['local'] + timely_5_16_7['local'] + timely_6_16_7['local'],
    1610: timely_4_16_10['local'] + timely_5_16_10['local'] + timely_6_16_10['local'],

}

_local_untimely = {
    24: untimely_4_2_4['local'] + untimely_5_2_4['local'] + untimely_6_2_4['local'],
    27: untimely_4_2_7['local'] + untimely_5_2_7['local'] + untimely_6_2_7['local'],
    210: untimely_4_2_10['local'] + untimely_5_2_10['local'] + untimely_6_2_10['local'],

    34: untimely_4_3_4['local'] + untimely_5_3_4['local'] + untimely_6_3_4['local'],
    37: untimely_4_3_7['local'] + untimely_5_3_7['local'] + untimely_6_3_7['local'],
    310: untimely_4_3_10['local'] + untimely_5_3_10['local'] + untimely_6_3_10['local'],

    74: untimely_4_7_4['local'] + untimely_5_7_4['local'] + untimely_6_7_4['local'],
    77: untimely_4_7_7['local'] + untimely_5_7_7['local'] + untimely_6_7_7['local'],
    710: untimely_4_7_10['local'] + untimely_5_7_10['local'] + untimely_6_7_10['local'],

    104: untimely_4_10_4['local'] + untimely_5_10_4['local'] + untimely_6_10_4['local'],
    107: untimely_4_10_7['local'] + untimely_5_10_7['local'] + untimely_6_10_7['local'],
    1010: untimely_4_10_10['local'] + untimely_5_10_10['local'] + untimely_6_10_10['local'],

    124: untimely_4_12_4['local'] + untimely_5_12_4['local'] + untimely_6_12_4['local'],
    127: untimely_4_12_7['local'] + untimely_5_12_7['local'] + untimely_6_12_7['local'],
    1210: untimely_4_12_10['local'] + untimely_5_12_10['local'] + untimely_6_12_10['local'],

    164: untimely_4_16_4['local'] + untimely_5_16_4['local'] + untimely_6_16_4['local'],
    167: untimely_4_16_7['local'] + untimely_5_16_7['local'] + untimely_6_16_7['local'],
    1610: untimely_4_16_10['local'] + untimely_5_16_10['local'] + untimely_6_16_10['local'],

}

_cloud_timely = {
    24: timely_4_2_4['cloud'] + timely_5_2_4['cloud'] + timely_6_2_4['cloud'],
    27: timely_4_2_7['cloud'] + timely_5_2_7['cloud'] + timely_6_2_7['cloud'],
    210: timely_4_2_10['cloud'] + timely_5_2_10['cloud'] + timely_6_2_10['cloud'],

    34: timely_4_3_4['cloud'] + timely_5_3_4['cloud'] + timely_6_3_4['cloud'],
    37: timely_4_3_7['cloud'] + timely_5_3_7['cloud'] + timely_6_3_7['cloud'],
    310: timely_4_3_10['cloud'] + timely_5_3_10['cloud'] + timely_6_3_10['cloud'],

    74: timely_4_7_4['cloud'] + timely_5_7_4['cloud'] + timely_6_7_4['cloud'],
    77: timely_4_7_7['cloud'] + timely_5_7_7['cloud'] + timely_6_7_7['cloud'],
    710: timely_4_7_10['cloud'] + timely_5_7_10['cloud'] + timely_6_7_10['cloud'],

    104: timely_4_10_4['cloud'] + timely_5_10_4['cloud'] + timely_6_10_4['cloud'],
    107: timely_4_10_7['cloud'] + timely_5_10_7['cloud'] + timely_6_10_7['cloud'],
    1010: timely_4_10_10['cloud'] + timely_5_10_10['cloud'] + timely_6_10_10['cloud'],

    124: timely_4_12_4['cloud'] + timely_5_12_4['cloud'] + timely_6_12_4['cloud'],
    127: timely_4_12_7['cloud'] + timely_5_12_7['cloud'] + timely_6_12_7['cloud'],
    1210: timely_4_12_10['cloud'] + timely_5_12_10['cloud'] + timely_6_12_10['cloud'],

    164: timely_4_16_4['cloud'] + timely_5_16_4['cloud'] + timely_6_16_4['cloud'],
    167: timely_4_16_7['cloud'] + timely_5_16_7['cloud'] + timely_6_16_7['cloud'],
    1610: timely_4_16_10['cloud'] + timely_5_16_10['cloud'] + timely_6_16_10['cloud'],

}

_cloud_untimely = {
    24: untimely_4_2_4['cloud'] + untimely_5_2_4['cloud'] + untimely_6_2_4['cloud'],
    27: untimely_4_2_7['cloud'] + untimely_5_2_7['cloud'] + untimely_6_2_7['cloud'],
    210: untimely_4_2_10['cloud'] + untimely_5_2_10['cloud'] + untimely_6_2_10['cloud'],

    34: untimely_4_3_4['cloud'] + untimely_5_3_4['cloud'] + untimely_6_3_4['cloud'],
    37: untimely_4_3_7['cloud'] + untimely_5_3_7['cloud'] + untimely_6_3_7['cloud'],
    310: untimely_4_3_10['cloud'] + untimely_5_3_10['cloud'] + untimely_6_3_10['cloud'],

    74: untimely_4_7_4['cloud'] + untimely_5_7_4['cloud'] + untimely_6_7_4['cloud'],
    77: untimely_4_7_7['cloud'] + untimely_5_7_7['cloud'] + untimely_6_7_7['cloud'],
    710: untimely_4_7_10['cloud'] + untimely_5_7_10['cloud'] + untimely_6_7_10['cloud'],

    104: untimely_4_10_4['cloud'] + untimely_5_10_4['cloud'] + untimely_6_10_4['cloud'],
    107: untimely_4_10_7['cloud'] + untimely_5_10_7['cloud'] + untimely_6_10_7['cloud'],
    1010: untimely_4_10_10['cloud'] + untimely_5_10_10['cloud'] + untimely_6_10_10['cloud'],

    124: untimely_4_12_4['cloud'] + untimely_5_12_4['cloud'] + untimely_6_12_4['cloud'],
    127: untimely_4_12_7['cloud'] + untimely_5_12_7['cloud'] + untimely_6_12_7['cloud'],
    1210: untimely_4_12_10['cloud'] + untimely_5_12_10['cloud'] + untimely_6_12_10['cloud'],

    164: untimely_4_16_4['cloud'] + untimely_5_16_4['cloud'] + untimely_6_16_4['cloud'],
    167: untimely_4_16_7['cloud'] + untimely_5_16_7['cloud'] + untimely_6_16_7['cloud'],
    1610: untimely_4_16_10['cloud'] + untimely_5_16_10['cloud'] + untimely_6_16_10['cloud'],

}


_mec_timely = {
    24: timely_4_2_4['mec'] + timely_5_2_4['mec'] + timely_6_2_4['mec'],
    27: timely_4_2_7['mec'] + timely_5_2_7['mec'] + timely_6_2_7['mec'],
    210: timely_4_2_10['mec'] + timely_5_2_10['mec'] + timely_6_2_10['mec'],

    34: timely_4_3_4['mec'] + timely_5_3_4['mec'] + timely_6_3_4['mec'],
    37: timely_4_3_7['mec'] + timely_5_3_7['mec'] + timely_6_3_7['mec'],
    310: timely_4_3_10['mec'] + timely_5_3_10['mec'] + timely_6_3_10['mec'],

    74: timely_4_7_4['mec'] + timely_5_7_4['mec'] + timely_6_7_4['mec'],
    77: timely_4_7_7['mec'] + timely_5_7_7['mec'] + timely_6_7_7['mec'],
    710: timely_4_7_10['mec'] + timely_5_7_10['mec'] + timely_6_7_10['mec'],

    104: timely_4_10_4['mec'] + timely_5_10_4['mec'] + timely_6_10_4['mec'],
    107: timely_4_10_7['mec'] + timely_5_10_7['mec'] + timely_6_10_7['mec'],
    1010: timely_4_10_10['mec'] + timely_5_10_10['mec'] + timely_6_10_10['mec'],

    124: timely_4_12_4['mec'] + timely_5_12_4['mec'] + timely_6_12_4['mec'],
    127: timely_4_12_7['mec'] + timely_5_12_7['mec'] + timely_6_12_7['mec'],
    1210: timely_4_12_10['mec'] + timely_5_12_10['mec'] + timely_6_12_10['mec'],

    164: timely_4_16_4['mec'] + timely_5_16_4['mec'] + timely_6_16_4['mec'],
    167: timely_4_16_7['mec'] + timely_5_16_7['mec'] + timely_6_16_7['mec'],
    1610: timely_4_16_10['mec'] + timely_5_16_10['mec'] + timely_6_16_10['mec'],

}

_mec_untimely = {
    24: untimely_4_2_4['mec'] + untimely_5_2_4['mec'] + untimely_6_2_4['mec'],
    27: untimely_4_2_7['mec'] + untimely_5_2_7['mec'] + untimely_6_2_7['mec'],
    210: untimely_4_2_10['mec'] + untimely_5_2_10['mec'] + untimely_6_2_10['mec'],

    34: untimely_4_3_4['mec'] + untimely_5_3_4['mec'] + untimely_6_3_4['mec'],
    37: untimely_4_3_7['mec'] + untimely_5_3_7['mec'] + untimely_6_3_7['mec'],
    310: untimely_4_3_10['mec'] + untimely_5_3_10['mec'] + untimely_6_3_10['mec'],

    74: untimely_4_7_4['mec'] + untimely_5_7_4['mec'] + untimely_6_7_4['mec'],
    77: untimely_4_7_7['mec'] + untimely_5_7_7['mec'] + untimely_6_7_7['mec'],
    710: untimely_4_7_10['mec'] + untimely_5_7_10['mec'] + untimely_6_7_10['mec'],

    104: untimely_4_10_4['mec'] + untimely_5_10_4['mec'] + untimely_6_10_4['mec'],
    107: untimely_4_10_7['mec'] + untimely_5_10_7['mec'] + untimely_6_10_7['mec'],
    1010: untimely_4_10_10['mec'] + untimely_5_10_10['mec'] + untimely_6_10_10['mec'],

    124: untimely_4_12_4['mec'] + untimely_5_12_4['mec'] + untimely_6_12_4['mec'],
    127: untimely_4_12_7['mec'] + untimely_5_12_7['mec'] + untimely_6_12_7['mec'],
    1210: untimely_4_12_10['mec'] + untimely_5_12_10['mec'] + untimely_6_12_10['mec'],

    164: untimely_4_16_4['mec'] + untimely_5_16_4['mec'] + untimely_6_16_4['mec'],
    167: untimely_4_16_7['mec'] + untimely_5_16_7['mec'] + untimely_6_16_7['mec'],
    1610: untimely_4_16_10['mec'] + untimely_5_16_10['mec'] + untimely_6_16_10['mec'],

}

_data_ = {'mec': (_mec_untimely, _mec_timely), 'local': (_local_untimely, _local_timely), 'cloud': (_cloud_untimely, _cloud_timely)}


def sum_data():
    # off_mec = {}
    # off_cloud = {}
    # loc = {}
    # d_list = [off_mec, loc, off_cloud]

    new_data = {}
    for data in _data_:
        d_t = _data_[data]
        new_data[data] = {k: d_t[0].get(k, 0) + d_t[1].get(k, 0) for k in set(d_t[0])}

    return list(new_data.values())


def format_data(d_dict):
    t_data = {}
    _keys = list(d_dict.keys())
    s4 = 0
    s7 = 1
    s10 = 2

    for i in range(len(_keys)):
        j = _keys[i]
        if i == s4:
            if 4 in t_data:
                t_data[4].append(d_dict[j])

                s4 += 3
            else:
                t_data[4] = [d_dict[j]]

                s4 += 3
        elif i == s7:
            if 7 in t_data:
                t_data[7].append(d_dict[j])

                s7 += 3
            else:
                t_data[7] = [d_dict[j]]

                s7 += 3
        elif i == s10:
            if 10 in t_data:
                t_data[10].append(d_dict[j])

                s10 += 3
            else:
                t_data[10] = [d_dict[j]]

                s10 += 3

    return t_data


def group_format(data_list):
    format_list = []
    for i in data_list:
        format_list.append(format_data(i))

    group_list = {4: {},
                  7: {},
                  10: {},
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

    return group_list


def percent(value, total):
    if value > 0:
        return round((value / total) * 100, 2)
    else:
        return 0


def plot_offloaded_remote(data_list, ax, _id_):
    # data_list =  [off_mec, off_cloud, loc, inward_mec]
    ax_list = (ax1, ax7, ax13)
    axx_list = {ax6: 4, ax12: 7, ax18: 10}
    title = [ax1, ax2, ax3, ax4, ax5, ax6]
    names = ('RMS+Bankers',
             'EDF+Bankers',
             'RMS+wound wait',
             'RMS+wait die',
             'EDF+wound wait',
             'EDF+wait die')
    algo_dict = {'RMS+Bankers': r'$ALG_1$',
                 'EDF+Bankers': r'$ALG_2$',
                 'RMS+wound wait': r'$ALG_3$',
                 'RMS+wait die': r'$ALG_4$',
                 'EDF+wound wait': r'$ALG_5$',
                 'EDF+wait die': r'$ALG_6$'}
    font = {
        'weight': 'medium',
        'size': 15,
    }

    keys = ['MEC', 'Local', 'Cloud']
    total = sum(data_list)

    val = [percent(data_list[0], total),
           percent(data_list[1], total),
           percent(data_list[2], total)]
    cols = ['r', 'g', 'b']      # , 'm']
    ypos = ([0, 1, 2])         # , 3])

    values = data_list
    # print(values)
    axx = ax.twinx()
    axx.set_yticklabels([])
    axx.set_yticks([])
    if ax in axx_list:
        axx.set_ylabel(f'{axx_list[ax]} MECs', rotation=0, fontsize=15, labelpad=30)

    ax.set_xticks(ypos)
    ax.set_xticklabels(keys, fontdict={'weight': 'medium', 'size': 12})
    ax.bar(ypos, values, align='center', color=cols, alpha=0.3)

    if ax in ax_list:
        ax.set_ylabel('No of Processes', fontdict={'weight': 'medium', 'size': 12})

    if ax in title:
        ax.set_title(algo_dict[names[_id_]], fontdict=font)
    for i in values:
        j = values.index(i)
        ax.text(j - 0.1, values[j], '{}%'.format(val[j]), rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))


def plot_av_times():
    axes = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18]
    _data = group_format(sum_data())
    print(_data)
    no = 0
    for i in _data:
        # i = keys 4 5 6 7
        for j in _data[i]:
            # _data[i] = dictionary => {0: [], 1: [] ...}
            data_plot = _data[i][j]
            plot_offloaded_remote(data_plot, axes[no], j)
            no += 1
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.show()


plot_av_times()