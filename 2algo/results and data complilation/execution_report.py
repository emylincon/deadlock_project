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
ax9 = fig.add_subplot(469)
ax10 = fig.add_subplot(4,6,10)
ax11 = fig.add_subplot(4,6,11)
ax12 = fig.add_subplot(4,6,12)
ax13 = fig.add_subplot(4,6,13)
ax14 = fig.add_subplot(4,6,14)
ax15 = fig.add_subplot(4,6,15)
ax16 = fig.add_subplot(4,6,16)
ax17 = fig.add_subplot(4,6,17)
ax18 = fig.add_subplot(4,6,18)
ax19 = fig.add_subplot(4,6,19)
ax20 = fig.add_subplot(4,6,20)
ax21 = fig.add_subplot(4,6,21)
ax22 = fig.add_subplot(4,6,22)
ax23 = fig.add_subplot(4,6,23)
ax24 = fig.add_subplot(4,6,24)


_loc_ = {
    24: [rd.loc0_2_4, rd.loc1_2_4, rd.loc2_2_4, rd.loc3_2_4],
    25: [rd.loc0_2_5, rd.loc1_2_5, rd.loc2_2_5, rd.loc3_2_5, rd.loc4_2_5, ],
    26: [rd.loc0_2_6, rd.loc1_2_6, rd.loc2_2_6, rd.loc3_2_6, rd.loc4_2_6, rd.loc5_2_6],
    27: [rd.loc0_2_7, rd.loc1_2_7, rd.loc2_2_7, rd.loc3_2_7, rd.loc4_2_7, rd.loc5_2_7, rd.loc6_2_7],

    34: [rd.loc0_3_4, rd.loc1_3_4, rd.loc2_3_4, rd.loc3_3_4],
    35: [rd.loc0_3_5, rd.loc1_3_5, rd.loc2_3_5, rd.loc3_3_5, rd.loc4_3_5],
    36: [rd.loc0_3_6, rd.loc1_3_6, rd.loc2_3_6, rd.loc3_3_6, rd.loc4_3_6, rd.loc5_3_6],
    37: [rd.loc0_3_7, rd.loc1_3_7, rd.loc2_3_7, rd.loc3_3_7, rd.loc4_3_7, rd.loc5_3_7, rd.loc6_3_7],

    74: [rd.loc0_7_4, rd.loc1_7_4, rd.loc2_7_4, rd.loc3_7_4],
    75: [rd.loc0_7_5, rd.loc1_7_5, rd.loc2_7_5, rd.loc3_7_5, rd.loc4_7_5],
    76: [rd.loc0_7_6, rd.loc1_7_6, rd.loc2_7_6, rd.loc3_7_6, rd.loc4_7_6, rd.loc5_7_6],
    77: [rd.loc0_7_7, rd.loc1_7_7, rd.loc2_7_7, rd.loc3_7_7, rd.loc4_7_7, rd.loc5_7_7, rd.loc6_7_7],

    104: [rd.loc0_10_4, rd.loc1_10_4, rd.loc2_10_4, rd.loc3_10_4],
    105: [rd.loc0_10_5, rd.loc1_10_5, rd.loc2_10_5, rd.loc3_10_5, rd.loc4_10_5],
    106: [rd.loc0_10_6, rd.loc1_10_6, rd.loc2_10_6, rd.loc3_10_6, rd.loc4_10_6, rd.loc5_10_6],
    107: [rd.loc0_10_7, rd.loc1_10_7, rd.loc2_10_7, rd.loc3_10_7, rd.loc4_10_7, rd.loc5_10_7, rd.loc6_10_7],

    124: [rd.loc0_12_4, rd.loc1_12_4, rd.loc2_12_4, rd.loc3_12_4],
    125: [rd.loc0_12_5, rd.loc1_12_5, rd.loc2_12_5, rd.loc3_12_5, rd.loc4_12_5],
    126: [rd.loc0_12_6, rd.loc1_12_6, rd.loc2_12_6, rd.loc3_12_6, rd.loc4_12_6, rd.loc5_12_6],
    127: [rd.loc0_12_7, rd.loc1_12_7, rd.loc2_12_7, rd.loc3_12_7, rd.loc4_12_7, rd.loc5_12_7, rd.loc6_12_7],

    164: [rd.loc0_16_4, rd.loc1_16_4, rd.loc2_16_4, rd.loc3_16_4],
    165: [rd.loc0_16_5, rd.loc1_16_5, rd.loc2_16_5, rd.loc3_16_5, rd.loc4_16_5],
    166: [rd.loc0_16_6, rd.loc1_16_6, rd.loc2_16_6, rd.loc3_16_6, rd.loc4_16_6, rd.loc5_16_6],
    167: [rd.loc0_16_7, rd.loc1_16_7, rd.loc2_16_7, rd.loc3_16_7, rd.loc4_16_7, rd.loc5_16_7, rd.loc6_16_7],
}

_off_cloud_ = {
    24: [rd.off_cloud0_2_4, rd.off_cloud1_2_4, rd.off_cloud2_2_4, rd.off_cloud3_2_4],
    25: [rd.off_cloud0_2_5, rd.off_cloud1_2_5, rd.off_cloud2_2_5, rd.off_cloud3_2_5, rd.off_cloud4_2_5, ],
    26: [rd.off_cloud0_2_6, rd.off_cloud1_2_6, rd.off_cloud2_2_6, rd.off_cloud3_2_6, rd.off_cloud4_2_6,
         rd.off_cloud5_2_6],
    27: [rd.off_cloud0_2_7, rd.off_cloud1_2_7, rd.off_cloud2_2_7, rd.off_cloud3_2_7, rd.off_cloud4_2_7,
         rd.off_cloud5_2_7, rd.off_cloud6_2_7],

    34: [rd.off_cloud0_3_4, rd.off_cloud1_3_4, rd.off_cloud2_3_4, rd.off_cloud3_3_4],
    35: [rd.off_cloud0_3_5, rd.off_cloud1_3_5, rd.off_cloud2_3_5, rd.off_cloud3_3_5, rd.off_cloud4_3_5],
    36: [rd.off_cloud0_3_6, rd.off_cloud1_3_6, rd.off_cloud2_3_6, rd.off_cloud3_3_6, rd.off_cloud4_3_6,
         rd.off_cloud5_3_6],
    37: [rd.off_cloud0_3_7, rd.off_cloud1_3_7, rd.off_cloud2_3_7, rd.off_cloud3_3_7, rd.off_cloud4_3_7,
         rd.off_cloud5_3_7, rd.off_cloud6_3_7],

    74: [rd.off_cloud0_7_4, rd.off_cloud1_7_4, rd.off_cloud2_7_4, rd.off_cloud3_7_4],
    75: [rd.off_cloud0_7_5, rd.off_cloud1_7_5, rd.off_cloud2_7_5, rd.off_cloud3_7_5, rd.off_cloud4_7_5],
    76: [rd.off_cloud0_7_6, rd.off_cloud1_7_6, rd.off_cloud2_7_6, rd.off_cloud3_7_6, rd.off_cloud4_7_6,
         rd.off_cloud5_7_6],
    77: [rd.off_cloud0_7_7, rd.off_cloud1_7_7, rd.off_cloud2_7_7, rd.off_cloud3_7_7, rd.off_cloud4_7_7,
         rd.off_cloud5_7_7, rd.off_cloud6_7_7],

    104: [rd.off_cloud0_10_4, rd.off_cloud1_10_4, rd.off_cloud2_10_4, rd.off_cloud3_10_4],
    105: [rd.off_cloud0_10_5, rd.off_cloud1_10_5, rd.off_cloud2_10_5, rd.off_cloud3_10_5, rd.off_cloud4_10_5],
    106: [rd.off_cloud0_10_6, rd.off_cloud1_10_6, rd.off_cloud2_10_6, rd.off_cloud3_10_6, rd.off_cloud4_10_6,
          rd.off_cloud5_10_6],
    107: [rd.off_cloud0_10_7, rd.off_cloud1_10_7, rd.off_cloud2_10_7, rd.off_cloud3_10_7, rd.off_cloud4_10_7,
          rd.off_cloud5_10_7, rd.off_cloud6_10_7],

    124: [rd.off_cloud0_12_4, rd.off_cloud1_12_4, rd.off_cloud2_12_4, rd.off_cloud3_12_4],
    125: [rd.off_cloud0_12_5, rd.off_cloud1_12_5, rd.off_cloud2_12_5, rd.off_cloud3_12_5, rd.off_cloud4_12_5],
    126: [rd.off_cloud0_12_6, rd.off_cloud1_12_6, rd.off_cloud2_12_6, rd.off_cloud3_12_6, rd.off_cloud4_12_6,
          rd.off_cloud5_12_6],
    127: [rd.off_cloud0_12_7, rd.off_cloud1_12_7, rd.off_cloud2_12_7, rd.off_cloud3_12_7, rd.off_cloud4_12_7,
          rd.off_cloud5_12_7, rd.off_cloud6_12_7],

    164: [rd.off_cloud0_16_4, rd.off_cloud1_16_4, rd.off_cloud2_16_4, rd.off_cloud3_16_4],
    165: [rd.off_cloud0_16_5, rd.off_cloud1_16_5, rd.off_cloud2_16_5, rd.off_cloud3_16_5, rd.off_cloud4_16_5],
    166: [rd.off_cloud0_16_6, rd.off_cloud1_16_6, rd.off_cloud2_16_6, rd.off_cloud3_16_6, rd.off_cloud4_16_6,
          rd.off_cloud5_16_6],
    167: [rd.off_cloud0_16_7, rd.off_cloud1_16_7, rd.off_cloud2_16_7, rd.off_cloud3_16_7, rd.off_cloud4_16_7,
          rd.off_cloud5_16_7, rd.off_cloud6_16_7],
}

_off_mec_ = {
    24: [rd.off_mec0_2_4, rd.off_mec1_2_4, rd.off_mec2_2_4, rd.off_mec3_2_4],
    25: [rd.off_mec0_2_5, rd.off_mec1_2_5, rd.off_mec2_2_5, rd.off_mec3_2_5, rd.off_mec4_2_5, ],
    26: [rd.off_mec0_2_6, rd.off_mec1_2_6, rd.off_mec2_2_6, rd.off_mec3_2_6, rd.off_mec4_2_6, rd.off_mec5_2_6],
    27: [rd.off_mec0_2_7, rd.off_mec1_2_7, rd.off_mec2_2_7, rd.off_mec3_2_7, rd.off_mec4_2_7, rd.off_mec5_2_7,
         rd.off_mec6_2_7],

    34: [rd.off_mec0_3_4, rd.off_mec1_3_4, rd.off_mec2_3_4, rd.off_mec3_3_4],
    35: [rd.off_mec0_3_5, rd.off_mec1_3_5, rd.off_mec2_3_5, rd.off_mec3_3_5, rd.off_mec4_3_5],
    36: [rd.off_mec0_3_6, rd.off_mec1_3_6, rd.off_mec2_3_6, rd.off_mec3_3_6, rd.off_mec4_3_6, rd.off_mec5_3_6],
    37: [rd.off_mec0_3_7, rd.off_mec1_3_7, rd.off_mec2_3_7, rd.off_mec3_3_7, rd.off_mec4_3_7, rd.off_mec5_3_7,
         rd.off_mec6_3_7],

    74: [rd.off_mec0_7_4, rd.off_mec1_7_4, rd.off_mec2_7_4, rd.off_mec3_7_4],
    75: [rd.off_mec0_7_5, rd.off_mec1_7_5, rd.off_mec2_7_5, rd.off_mec3_7_5, rd.off_mec4_7_5],
    76: [rd.off_mec0_7_6, rd.off_mec1_7_6, rd.off_mec2_7_6, rd.off_mec3_7_6, rd.off_mec4_7_6, rd.off_mec5_7_6],
    77: [rd.off_mec0_7_7, rd.off_mec1_7_7, rd.off_mec2_7_7, rd.off_mec3_7_7, rd.off_mec4_7_7, rd.off_mec5_7_7,
         rd.off_mec6_7_7],

    104: [rd.off_mec0_10_4, rd.off_mec1_10_4, rd.off_mec2_10_4, rd.off_mec3_10_4],
    105: [rd.off_mec0_10_5, rd.off_mec1_10_5, rd.off_mec2_10_5, rd.off_mec3_10_5, rd.off_mec4_10_5],
    106: [rd.off_mec0_10_6, rd.off_mec1_10_6, rd.off_mec2_10_6, rd.off_mec3_10_6, rd.off_mec4_10_6, rd.off_mec5_10_6],
    107: [rd.off_mec0_10_7, rd.off_mec1_10_7, rd.off_mec2_10_7, rd.off_mec3_10_7, rd.off_mec4_10_7, rd.off_mec5_10_7,
          rd.off_mec6_10_7],

    124: [rd.off_mec0_12_4, rd.off_mec1_12_4, rd.off_mec2_12_4, rd.off_mec3_12_4],
    125: [rd.off_mec0_12_5, rd.off_mec1_12_5, rd.off_mec2_12_5, rd.off_mec3_12_5, rd.off_mec4_12_5],
    126: [rd.off_mec0_12_6, rd.off_mec1_12_6, rd.off_mec2_12_6, rd.off_mec3_12_6, rd.off_mec4_12_6, rd.off_mec5_12_6],
    127: [rd.off_mec0_12_7, rd.off_mec1_12_7, rd.off_mec2_12_7, rd.off_mec3_12_7, rd.off_mec4_12_7, rd.off_mec5_12_7,
          rd.off_mec6_12_7],

    164: [rd.off_mec0_16_4, rd.off_mec1_16_4, rd.off_mec2_16_4, rd.off_mec3_16_4],
    165: [rd.off_mec0_16_5, rd.off_mec1_16_5, rd.off_mec2_16_5, rd.off_mec3_16_5, rd.off_mec4_16_5],
    166: [rd.off_mec0_16_6, rd.off_mec1_16_6, rd.off_mec2_16_6, rd.off_mec3_16_6, rd.off_mec4_16_6, rd.off_mec5_16_6],
    167: [rd.off_mec0_16_7, rd.off_mec1_16_7, rd.off_mec2_16_7, rd.off_mec3_16_7, rd.off_mec4_16_7, rd.off_mec5_16_7,
          rd.off_mec6_16_7],
}

_inward_mec_ = {
    24: [rd.inward_mec0_2_4, rd.inward_mec1_2_4, rd.inward_mec2_2_4, rd.inward_mec3_2_4],
    25: [rd.inward_mec0_2_5, rd.inward_mec1_2_5, rd.inward_mec2_2_5, rd.inward_mec3_2_5, rd.inward_mec4_2_5, ],
    26: [rd.inward_mec0_2_6, rd.inward_mec1_2_6, rd.inward_mec2_2_6, rd.inward_mec3_2_6, rd.inward_mec4_2_6,
         rd.inward_mec5_2_6],
    27: [rd.inward_mec0_2_7, rd.inward_mec1_2_7, rd.inward_mec2_2_7, rd.inward_mec3_2_7, rd.inward_mec4_2_7,
         rd.inward_mec5_2_7, rd.inward_mec6_2_7],

    34: [rd.inward_mec0_3_4, rd.inward_mec1_3_4, rd.inward_mec2_3_4, rd.inward_mec3_3_4],
    35: [rd.inward_mec0_3_5, rd.inward_mec1_3_5, rd.inward_mec2_3_5, rd.inward_mec3_3_5, rd.inward_mec4_3_5],
    36: [rd.inward_mec0_3_6, rd.inward_mec1_3_6, rd.inward_mec2_3_6, rd.inward_mec3_3_6, rd.inward_mec4_3_6,
         rd.inward_mec5_3_6],
    37: [rd.inward_mec0_3_7, rd.inward_mec1_3_7, rd.inward_mec2_3_7, rd.inward_mec3_3_7, rd.inward_mec4_3_7,
         rd.inward_mec5_3_7, rd.inward_mec6_3_7],

    74: [rd.inward_mec0_7_4, rd.inward_mec1_7_4, rd.inward_mec2_7_4, rd.inward_mec3_7_4],
    75: [rd.inward_mec0_7_5, rd.inward_mec1_7_5, rd.inward_mec2_7_5, rd.inward_mec3_7_5, rd.inward_mec4_7_5],
    76: [rd.inward_mec0_7_6, rd.inward_mec1_7_6, rd.inward_mec2_7_6, rd.inward_mec3_7_6, rd.inward_mec4_7_6,
         rd.inward_mec5_7_6],
    77: [rd.inward_mec0_7_7, rd.inward_mec1_7_7, rd.inward_mec2_7_7, rd.inward_mec3_7_7, rd.inward_mec4_7_7,
         rd.inward_mec5_7_7, rd.inward_mec6_7_7],

    104: [rd.inward_mec0_10_4, rd.inward_mec1_10_4, rd.inward_mec2_10_4, rd.inward_mec3_10_4],
    105: [rd.inward_mec0_10_5, rd.inward_mec1_10_5, rd.inward_mec2_10_5, rd.inward_mec3_10_5, rd.inward_mec4_10_5],
    106: [rd.inward_mec0_10_6, rd.inward_mec1_10_6, rd.inward_mec2_10_6, rd.inward_mec3_10_6, rd.inward_mec4_10_6,
          rd.inward_mec5_10_6],
    107: [rd.inward_mec0_10_7, rd.inward_mec1_10_7, rd.inward_mec2_10_7, rd.inward_mec3_10_7, rd.inward_mec4_10_7,
          rd.inward_mec5_10_7, rd.inward_mec6_10_7],

    124: [rd.inward_mec0_12_4, rd.inward_mec1_12_4, rd.inward_mec2_12_4, rd.inward_mec3_12_4],
    125: [rd.inward_mec0_12_5, rd.inward_mec1_12_5, rd.inward_mec2_12_5, rd.inward_mec3_12_5, rd.inward_mec4_12_5],
    126: [rd.inward_mec0_12_6, rd.inward_mec1_12_6, rd.inward_mec2_12_6, rd.inward_mec3_12_6, rd.inward_mec4_12_6,
          rd.inward_mec5_12_6],
    127: [rd.inward_mec0_12_7, rd.inward_mec1_12_7, rd.inward_mec2_12_7, rd.inward_mec3_12_7, rd.inward_mec4_12_7,
          rd.inward_mec5_12_7, rd.inward_mec6_12_7],

    164: [rd.inward_mec0_16_4, rd.inward_mec1_16_4, rd.inward_mec2_16_4, rd.inward_mec3_16_4],
    165: [rd.inward_mec0_16_5, rd.inward_mec1_16_5, rd.inward_mec2_16_5, rd.inward_mec3_16_5, rd.inward_mec4_16_5],
    166: [rd.inward_mec0_16_6, rd.inward_mec1_16_6, rd.inward_mec2_16_6, rd.inward_mec3_16_6, rd.inward_mec4_16_6,
          rd.inward_mec5_16_6],
    167: [rd.inward_mec0_16_7, rd.inward_mec1_16_7, rd.inward_mec2_16_7, rd.inward_mec3_16_7, rd.inward_mec4_16_7,
          rd.inward_mec5_16_7, rd.inward_mec6_16_7],
}
