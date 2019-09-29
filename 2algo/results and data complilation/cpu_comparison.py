import matplotlib.pyplot as plt
import data as rd

fig = plt.figure()
ax1 = fig.add_subplot(461)
ax2 = fig.add_subplot(462)
ax3 = fig.add_subplot(463)
ax4 = fig.add_subplot(464)
ax5 = fig.add_subplot(465)
ax6 = fig.add_subplot(466)
ax7 = fig.add_subplot(467)
ax8 = fig.add_subplot(468)

style = ['g--^', 'r:o', 'b-.s', 'm--*', 'k-.>', 'c-.s']
names = ('RMS + Bankers',
         'EDF + Bankers',
         'RMS + wound wait',
         'RMS + wait die',
         'EDF + wound wait',
         'EDF + wait die')

_cpu = {
    24: rd.cpu2_2_4,
    25: rd.cpu2_2_5,
    26: rd.cpu2_2_6,
    27: rd.cpu2_2_7,

    34: rd.cpu2_3_4,
    35: rd.cpu2_3_5,
    36: rd.cpu2_3_6,
    37: rd.cpu2_3_7,

    74: rd.cpu2_7_4,
    75: rd.cpu2_7_5,
    76: rd.cpu2_7_6,
    77: rd.cpu2_7_7,

    104: rd.cpu2_10_4,
    105: rd.cpu2_10_5,
    106: rd.cpu2_10_6,
    107: rd.cpu2_10_7,

    124: rd.cpu2_12_4,
    125: rd.cpu2_12_5,
    126: rd.cpu2_12_6,
    127: rd.cpu2_12_7,

    164: rd.cpu2_16_4,
    165: rd.cpu2_16_5,
    166: rd.cpu2_16_6,
    167: rd.cpu2_16_7,
}

_memory = {
    24: rd.memory2_2_4,
    25: rd.memory2_2_5,
    26: rd.memory2_2_6,
    27: rd.memory2_2_7,

    34: rd.memory2_3_4,
    35: rd.memory2_3_5,
    36: rd.memory2_3_6,
    37: rd.memory2_3_7,

    74: rd.memory2_7_4,
    75: rd.memory2_7_5,
    76: rd.memory2_7_6,
    77: rd.memory2_7_7,

    104: rd.memory2_10_4,
    105: rd.memory2_10_5,
    106: rd.memory2_10_6,
    107: rd.memory2_10_7,

    124: rd.memory2_12_4,
    125: rd.memory2_12_5,
    126: rd.memory2_12_6,
    127: rd.memory2_12_7,

    164: rd.memory2_16_4,
    165: rd.memory2_16_5,
    166: rd.memory2_16_6,
    167: rd.memory2_16_7,
}


def format_data(d_dict):
    t_data = {}
    _keys = list(d_dict.keys())
    s4 = 0
    s5 = 1
    s6 = 2
    s7 = 3
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
        elif i == s7:
            if 7 in t_data:
                t_data[7].append(d_dict[j])

                s7 += 4
            else:
                t_data[7] = [d_dict[j]]

                s7 += 4

    return t_data


def _mov_avg(a1):
    ma1 = []  # moving average list
    avg1 = 0  # moving average pointwise
    count = 0
    for i in range(len(a1)):
        count += 1
        avg1 = ((count - 1) * avg1 + a1[i]) / count
        ma1.append(round(avg1, 4))  # cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def plot_cpu(plot_data, ax, style_id):
    ax.grid(True)

    mv = _mov_avg(plot_data)
    pt = mv[0:len(mv):int((len(mv) / 10)) + 1]
    if pt[-1] != mv[-1]:
        pt.append(mv[-1])
    ptx = [mv.index(i) for i in pt]
    ax.plot(ptx,
            pt,
            style[style_id],
            linewidth=2,
            label=names[style_id])
    ax.set_title('RTT Utilization over Time')
    ax3.set_xlabel('Time (seconds)')
    ax3.legend()
    plt.subplot(ax3)


k = format_data(_cpu)
for i in k:
    print(i, k[i])
