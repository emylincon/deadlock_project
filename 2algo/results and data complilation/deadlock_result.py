import matplotlib.pyplot as plt
import data as rd

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

_deadlock = {
    24: [rd.deadlock0_2_4, rd.deadlock1_2_4, rd.deadlock2_2_4, rd.deadlock3_2_4],
    25: [rd.deadlock0_2_5, rd.deadlock1_2_5, rd.deadlock2_2_5, rd.deadlock3_2_5, rd.deadlock4_2_5, ],
    26: [rd.deadlock0_2_6, rd.deadlock1_2_6, rd.deadlock2_2_6, rd.deadlock3_2_6, rd.deadlock4_2_6, rd.deadlock5_2_6],
    27: [rd.deadlock0_2_7, rd.deadlock1_2_7, rd.deadlock2_2_7, rd.deadlock3_2_7, rd.deadlock4_2_7, rd.deadlock5_2_7,
         rd.deadlock6_2_7],

    34: [rd.deadlock0_3_4, rd.deadlock1_3_4, rd.deadlock2_3_4, rd.deadlock3_3_4],
    35: [rd.deadlock0_3_5, rd.deadlock1_3_5, rd.deadlock2_3_5, rd.deadlock3_3_5, rd.deadlock4_3_5],
    36: [rd.deadlock0_3_6, rd.deadlock1_3_6, rd.deadlock2_3_6, rd.deadlock3_3_6, rd.deadlock4_3_6, rd.deadlock5_3_6],
    37: [rd.deadlock0_3_7, rd.deadlock1_3_7, rd.deadlock2_3_7, rd.deadlock3_3_7, rd.deadlock4_3_7, rd.deadlock5_3_7,
         rd.deadlock6_3_7],

    74: [rd.deadlock0_7_4, rd.deadlock1_7_4, rd.deadlock2_7_4, rd.deadlock3_7_4],
    75: [rd.deadlock0_7_5, rd.deadlock1_7_5, rd.deadlock2_7_5, rd.deadlock3_7_5, rd.deadlock4_7_5],
    76: [rd.deadlock0_7_6, rd.deadlock1_7_6, rd.deadlock2_7_6, rd.deadlock3_7_6, rd.deadlock4_7_6, rd.deadlock5_7_6],
    77: [rd.deadlock0_7_7, rd.deadlock1_7_7, rd.deadlock2_7_7, rd.deadlock3_7_7, rd.deadlock4_7_7, rd.deadlock5_7_7,
         rd.deadlock6_7_7],

    104: [rd.deadlock0_10_4, rd.deadlock1_10_4, rd.deadlock2_10_4, rd.deadlock3_10_4],
    105: [rd.deadlock0_10_5, rd.deadlock1_10_5, rd.deadlock2_10_5, rd.deadlock3_10_5, rd.deadlock4_10_5],
    106: [rd.deadlock0_10_6, rd.deadlock1_10_6, rd.deadlock2_10_6, rd.deadlock3_10_6, rd.deadlock4_10_6,
          rd.deadlock5_10_6],
    107: [rd.deadlock0_10_7, rd.deadlock1_10_7, rd.deadlock2_10_7, rd.deadlock3_10_7, rd.deadlock4_10_7,
          rd.deadlock5_10_7, rd.deadlock6_10_7],

    124: [rd.deadlock0_12_4, rd.deadlock1_12_4, rd.deadlock2_12_4, rd.deadlock3_12_4],
    125: [rd.deadlock0_12_5, rd.deadlock1_12_5, rd.deadlock2_12_5, rd.deadlock3_12_5, rd.deadlock4_12_5],
    126: [rd.deadlock0_12_6, rd.deadlock1_12_6, rd.deadlock2_12_6, rd.deadlock3_12_6, rd.deadlock4_12_6,
          rd.deadlock5_12_6],
    127: [rd.deadlock0_12_7, rd.deadlock1_12_7, rd.deadlock2_12_7, rd.deadlock3_12_7, rd.deadlock4_12_7,
          rd.deadlock5_12_7, rd.deadlock6_12_7],

    164: [rd.deadlock0_16_4, rd.deadlock1_16_4, rd.deadlock2_16_4, rd.deadlock3_16_4],
    165: [rd.deadlock0_16_5, rd.deadlock1_16_5, rd.deadlock2_16_5, rd.deadlock3_16_5, rd.deadlock4_16_5],
    166: [rd.deadlock0_16_6, rd.deadlock1_16_6, rd.deadlock2_16_6, rd.deadlock3_16_6, rd.deadlock4_16_6,
          rd.deadlock5_16_6],
    167: [rd.deadlock0_16_7, rd.deadlock1_16_7, rd.deadlock2_16_7, rd.deadlock3_16_7, rd.deadlock4_16_7,
          rd.deadlock5_16_7, rd.deadlock6_16_7],
}


def sum_deadlock():
    s_deadlock= {}
    _deadlock_ = {}

    # cleaning data
    for i in _deadlock:
        _deadlock_[i] = [j[0] - 1 for j in _deadlock[i]]

    for i in _deadlock_:
        s_deadlock[i] = sum(_deadlock_[i])

    # print("s: ", s_deadlock)

    # print(f"_dead_: {_deadlock_}")

    return s_deadlock


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


print(format_data(sum_deadlock()))
# print("d: ", _deadlock)

# no difference in results