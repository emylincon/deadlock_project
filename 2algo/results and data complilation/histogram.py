import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, )
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, )

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))


plt.show()

av = {'timely_4_2': 6760, 'timely_5_2': 10565, 'timely_6_2': 10722, 'timely_7_2': 10940, 'untimely_4_2': 3708,
      'untimely_5_2': 190, 'untimely_6_2': 181, 'untimely_7_2': 116, 'timely_4_3': 9510, 'timely_5_3': 10616,
      'timely_6_3': 10577, 'timely_7_3': 10456, 'untimely_4_3': 965, 'untimely_5_3': 168, 'untimely_6_3': 299,
      'untimely_7_3': 576, 'timely_4_7': 7494, 'timely_5_7': 8928, 'timely_6_7': 10991, 'timely_7_7': 11118,
      'untimely_4_7': 2998, 'untimely_5_7': 1910, 'untimely_6_7': 153, 'untimely_7_7': 41, 'timely_4_10': 9843,
      'timely_5_10': 10714, 'timely_6_10': 10829, 'timely_7_10': 11099, 'untimely_4_10': 665, 'untimely_5_10': 128,
      'untimely_6_10': 176, 'untimely_7_10': 73, 'timely_4_12': 9626, 'timely_5_12': 10542, 'timely_6_12': 10579,
      'timely_7_12': 10506, 'untimely_4_12': 839, 'untimely_5_12': 217, 'untimely_6_12': 291, 'untimely_7_12': 572,
      'timely_4_16': 8264, 'timely_5_16': 9710, 'timely_6_16': 9110, 'timely_7_16': 9758, 'untimely_4_16': 2209,
      'untimely_5_16': 1053, 'untimely_6_16': 1747, 'untimely_7_16': 1298}
