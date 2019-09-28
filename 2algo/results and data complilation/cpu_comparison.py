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
    24: [rd.cpu0_2_4, rd.cpu1_2_4, rd.cpu2_2_4, rd.cpu3_2_4],
    25: [rd.cpu0_2_5, rd.cpu1_2_5, rd.cpu2_2_5, rd.cpu3_2_5, rd.cpu4_2_5, ],
    26: [rd.cpu0_2_6, rd.cpu1_2_6, rd.cpu2_2_6, rd.cpu3_2_6, rd.cpu4_2_6, rd.cpu5_2_6],
    27: [rd.cpu0_2_7, rd.cpu1_2_7, rd.cpu2_2_7, rd.cpu3_2_7, rd.cpu4_2_7, rd.cpu5_2_7,
         rd.cpu6_2_7],

    34: [rd.cpu0_3_4, rd.cpu1_3_4, rd.cpu2_3_4, rd.cpu3_3_4],
    35: [rd.cpu0_3_5, rd.cpu1_3_5, rd.cpu2_3_5, rd.cpu3_3_5, rd.cpu4_3_5],
    36: [rd.cpu0_3_6, rd.cpu1_3_6, rd.cpu2_3_6, rd.cpu3_3_6, rd.cpu4_3_6, rd.cpu5_3_6],
    37: [rd.cpu0_3_7, rd.cpu1_3_7, rd.cpu2_3_7, rd.cpu3_3_7, rd.cpu4_3_7, rd.cpu5_3_7,
         rd.cpu6_3_7],

    74: [rd.cpu0_7_4, rd.cpu1_7_4, rd.cpu2_7_4, rd.cpu3_7_4],
    75: [rd.cpu0_7_5, rd.cpu1_7_5, rd.cpu2_7_5, rd.cpu3_7_5, rd.cpu4_7_5],
    76: [rd.cpu0_7_6, rd.cpu1_7_6, rd.cpu2_7_6, rd.cpu3_7_6, rd.cpu4_7_6, rd.cpu5_7_6],
    77: [rd.cpu0_7_7, rd.cpu1_7_7, rd.cpu2_7_7, rd.cpu3_7_7, rd.cpu4_7_7, rd.cpu5_7_7,
         rd.cpu6_7_7],

    104: [rd.cpu0_10_4, rd.cpu1_10_4, rd.cpu2_10_4, rd.cpu3_10_4],
    105: [rd.cpu0_10_5, rd.cpu1_10_5, rd.cpu2_10_5, rd.cpu3_10_5, rd.cpu4_10_5],
    106: [rd.cpu0_10_6, rd.cpu1_10_6, rd.cpu2_10_6, rd.cpu3_10_6, rd.cpu4_10_6,
          rd.cpu5_10_6],
    107: [rd.cpu0_10_7, rd.cpu1_10_7, rd.cpu2_10_7, rd.cpu3_10_7, rd.cpu4_10_7,
          rd.cpu5_10_7, rd.cpu6_10_7],

    124: [rd.cpu0_12_4, rd.cpu1_12_4, rd.cpu2_12_4, rd.cpu3_12_4],
    125: [rd.cpu0_12_5, rd.cpu1_12_5, rd.cpu2_12_5, rd.cpu3_12_5, rd.cpu4_12_5],
    126: [rd.cpu0_12_6, rd.cpu1_12_6, rd.cpu2_12_6, rd.cpu3_12_6, rd.cpu4_12_6,
          rd.cpu5_12_6],
    127: [rd.cpu0_12_7, rd.cpu1_12_7, rd.cpu2_12_7, rd.cpu3_12_7, rd.cpu4_12_7,
          rd.cpu5_12_7, rd.cpu6_12_7],

    164: [rd.cpu0_16_4, rd.cpu1_16_4, rd.cpu2_16_4, rd.cpu3_16_4],
    165: [rd.cpu0_16_5, rd.cpu1_16_5, rd.cpu2_16_5, rd.cpu3_16_5, rd.cpu4_16_5],
    166: [rd.cpu0_16_6, rd.cpu1_16_6, rd.cpu2_16_6, rd.cpu3_16_6, rd.cpu4_16_6,
          rd.cpu5_16_6],
    167: [rd.cpu0_16_7, rd.cpu1_16_7, rd.cpu2_16_7, rd.cpu3_16_7, rd.cpu4_16_7,
          rd.cpu5_16_7, rd.cpu6_16_7],
}


_memory = {
    24: [rd.memory0_2_4, rd.memory1_2_4, rd.memory2_2_4, rd.memory3_2_4],
    25: [rd.memory0_2_5, rd.memory1_2_5, rd.memory2_2_5, rd.memory3_2_5, rd.memory4_2_5, ],
    26: [rd.memory0_2_6, rd.memory1_2_6, rd.memory2_2_6, rd.memory3_2_6, rd.memory4_2_6, rd.memory5_2_6],
    27: [rd.memory0_2_7, rd.memory1_2_7, rd.memory2_2_7, rd.memory3_2_7, rd.memory4_2_7, rd.memory5_2_7,
         rd.memory6_2_7],

    34: [rd.memory0_3_4, rd.memory1_3_4, rd.memory2_3_4, rd.memory3_3_4],
    35: [rd.memory0_3_5, rd.memory1_3_5, rd.memory2_3_5, rd.memory3_3_5, rd.memory4_3_5],
    36: [rd.memory0_3_6, rd.memory1_3_6, rd.memory2_3_6, rd.memory3_3_6, rd.memory4_3_6, rd.memory5_3_6],
    37: [rd.memory0_3_7, rd.memory1_3_7, rd.memory2_3_7, rd.memory3_3_7, rd.memory4_3_7, rd.memory5_3_7,
         rd.memory6_3_7],

    74: [rd.memory0_7_4, rd.memory1_7_4, rd.memory2_7_4, rd.memory3_7_4],
    75: [rd.memory0_7_5, rd.memory1_7_5, rd.memory2_7_5, rd.memory3_7_5, rd.memory4_7_5],
    76: [rd.memory0_7_6, rd.memory1_7_6, rd.memory2_7_6, rd.memory3_7_6, rd.memory4_7_6, rd.memory5_7_6],
    77: [rd.memory0_7_7, rd.memory1_7_7, rd.memory2_7_7, rd.memory3_7_7, rd.memory4_7_7, rd.memory5_7_7,
         rd.memory6_7_7],

    104: [rd.memory0_10_4, rd.memory1_10_4, rd.memory2_10_4, rd.memory3_10_4],
    105: [rd.memory0_10_5, rd.memory1_10_5, rd.memory2_10_5, rd.memory3_10_5, rd.memory4_10_5],
    106: [rd.memory0_10_6, rd.memory1_10_6, rd.memory2_10_6, rd.memory3_10_6, rd.memory4_10_6,
          rd.memory5_10_6],
    107: [rd.memory0_10_7, rd.memory1_10_7, rd.memory2_10_7, rd.memory3_10_7, rd.memory4_10_7,
          rd.memory5_10_7, rd.memory6_10_7],

    124: [rd.memory0_12_4, rd.memory1_12_4, rd.memory2_12_4, rd.memory3_12_4],
    125: [rd.memory0_12_5, rd.memory1_12_5, rd.memory2_12_5, rd.memory3_12_5, rd.memory4_12_5],
    126: [rd.memory0_12_6, rd.memory1_12_6, rd.memory2_12_6, rd.memory3_12_6, rd.memory4_12_6,
          rd.memory5_12_6],
    127: [rd.memory0_12_7, rd.memory1_12_7, rd.memory2_12_7, rd.memory3_12_7, rd.memory4_12_7,
          rd.memory5_12_7, rd.memory6_12_7],

    164: [rd.memory0_16_4, rd.memory1_16_4, rd.memory2_16_4, rd.memory3_16_4],
    165: [rd.memory0_16_5, rd.memory1_16_5, rd.memory2_16_5, rd.memory3_16_5, rd.memory4_16_5],
    166: [rd.memory0_16_6, rd.memory1_16_6, rd.memory2_16_6, rd.memory3_16_6, rd.memory4_16_6,
          rd.memory5_16_6],
    167: [rd.memory0_16_7, rd.memory1_16_7, rd.memory2_16_7, rd.memory3_16_7, rd.memory4_16_7,
          rd.memory5_16_7, rd.memory6_16_7],
}