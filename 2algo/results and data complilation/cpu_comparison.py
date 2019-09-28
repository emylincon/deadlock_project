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
