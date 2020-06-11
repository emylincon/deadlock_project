import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

timely = ({4: [8556, 8354, 7130, 8138, 7598, 7649], 7: [8827, 8520, 7284, 8588, 7366, 8738], 10: [8799, 9078, 8979, 8776, 8904, 8956]}, {4: [618, 820, 2044, 1036, 1576, 1525], 7: [347, 654, 1890, 586, 1808, 436], 10: [375, 96, 195, 398, 270, 218]})
timely1 = {4: [93.2636, 91.0617, 77.7196, 88.7072, 82.821, 83.3769], 7: [96.2176, 92.8712, 79.3983, 93.6124, 80.2921, 95.2474], 10: [95.9124, 98.9536, 97.8744, 95.6617, 97.0569, 97.6237]}
exec_report = {4: {0: [718, 7218, 1238], 1: [716, 7218, 1240], 2: [1300, 5975, 1899], 3: [1345, 5988, 1841], 4: [698, 7218, 1258], 5: [678, 7211, 1285]}, 7: {0: [772, 7218, 1184], 1: [1307, 5848, 2019], 2: [1230, 6291, 1653], 3: [700, 7211, 1263], 4: [722, 7218, 1234], 5: [786, 7211, 1177]}, 10: {0: [700, 7211, 1263], 1: [1235, 6334, 1605], 2: [756, 7211, 1207], 3: [694, 7218, 1262], 4: [1265, 5926, 1983], 5: [699, 7211, 1264]}}
exec = {'mec': {4: [7.8265, 7.8047, 14.1705, 14.661, 7.6085, 7.3905], 7: [8.4151, 14.2468, 13.4075, 7.6303, 7.8701, 8.5677], 10: [7.6303, 13.462, 8.2407, 7.5649, 13.789, 7.6194]}, 'local': {4: [78.6789, 78.6789, 65.1297, 65.2714, 78.6789, 78.6026], 7: [78.6789, 63.7454, 68.5742, 78.6026, 78.6789, 78.6026], 10: [78.6026, 69.0429, 78.6026, 78.6789, 64.5956, 78.6026]}, 'cloud': {4: [13.4947, 13.5165, 20.6998, 20.0676, 13.7127, 14.007], 7: [12.906, 22.0078, 18.0183, 13.7672, 13.4511, 12.8297], 10: [13.7672, 17.4951, 13.1567, 13.7563, 21.6154, 13.7781]}}
avg_wt = {4: [17.9599, 17.3425, 8.3322, 7.9103, 7.9156, 8.1576], 7: [19.1244, 18.5187, 7.1498, 7.2783, 7.4104, 7.2206], 10: [19.2627, 6.2073, 7.1808, 7.2433, 7.2481, 7.315]}
avg_rtt = {4: [21.9067, 21.1495, 8.2049, 7.7117, 7.8877, 7.9763], 7: [22.1794, 22.099, 8.1193, 7.624, 7.2834, 7.6406], 10: [20.6891, 6.8877, 7.9085, 7.9939, 7.9865, 7.9827]}
avg_cpu = {4: [1.7479, 1.8976, 1.615, 1.6462, 1.5994, 1.5162], 7: [1.099, 1.2932, 0.9423, 0.8702, 0.9621, 0.9257], 10: [1.0134, 0.9768, 0.8683, 0.9988, 0.8821, 0.9492]}
print('-'*100)
# homo
avg_cpu_homo = {4: [2.1136, 1.6612, 1.4683, 1.7405, 1.696, 1.6402], 7: [1.4591, 1.2978, 1.0349, 1.0812, 1.0565, 1.0685], 10: [1.1888, 1.2354, 0.9365, 0.9042, 0.9673, 0.9642]}
avg_rtt_homo = {4: [7.7384, 7.9969, 7.735, 7.9702, 8.1349, 7.8773], 7: [7.7978, 7.6699, 7.606, 7.8255, 7.8163, 7.8323], 10: [8.0141, 8.1465, 7.9518, 7.8366, 8.1125, 8.1812]}
avg_wt_homo = {4: [7.7331, 7.793, 7.6889, 8.0924, 7.9554, 7.9389], 7: [7.2592, 7.1101, 7.0876, 7.343, 7.3246, 7.2702], 10: [7.2452, 7.3179, 7.2795, 7.1666, 7.2656, 7.2886]}
exec_report_homo = {4: {0: [742, 7218, 1214], 1: [726, 7218, 1230], 2: [2151, 4366, 2657], 3: [2201, 4355, 2618], 4: [743, 7218, 1213], 5: [681, 7211, 1282]}, 7: {0: [723, 7218, 1233], 1: [1851, 4841, 2482], 2: [2604, 3937, 2633], 3: [711, 7211, 1252], 4: [718, 7218, 1238], 5: [794, 7211, 1169]}, 10: {0: [719, 7211, 1244], 1: [2552, 3899, 2723], 2: [808, 7211, 1155], 3: [767, 7218, 1189], 4: [1812, 4839, 2523], 5: [727, 7211, 1236]}}
timely_homo = ({4: [7275, 8743, 8530, 8447, 8276, 8425], 7: [8917, 8953, 8851, 8715, 8787, 8808], 10: [8991, 9022, 8945, 8718, 9010, 9013]}, {4: [1899, 431, 644, 727, 898, 749], 7: [257, 221, 323, 459, 387, 366], 10: [183, 152, 229, 456, 164, 161]})
timely2 = {4: [79.3002, 95.3019, 92.9802, 92.0754, 90.2115, 91.8356], 7: [97.1986, 97.591, 96.4792, 94.9967, 95.7816, 96.0105], 10: [98.0052, 98.3431, 97.5038, 95.0294, 98.2123, 98.245]}
exe_homo = {'mec': {4: [8.0881, 7.9137, 23.4467, 23.9917, 8.099, 7.4232], 7: [7.881, 20.1766, 28.3846, 7.7502, 7.8265, 8.6549], 10: [7.8374, 27.8177, 8.8075, 8.3606, 19.7515, 7.9246]}, 'local': {4: [78.6789, 78.6789, 47.591, 47.4711, 78.6789, 78.6026], 7: [78.6789, 52.7687, 42.9148, 78.6026, 78.6789, 78.6026], 10: [78.6026, 42.5005, 78.6026, 78.6789, 52.7469, 78.6026]}, 'cloud': {4: [13.233, 13.4075, 28.9623, 28.5372, 13.2221, 13.9743], 7: [13.4402, 27.0547, 28.7007, 13.6473, 13.4947, 12.7425], 10: [13.5601, 29.6817, 12.5899, 12.9605, 27.5016, 13.4729]}}


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

width = 0.35
algo_dict = {r'$ALG_1$',
             r'$ALG_2$',
             r'$ALG_3$',
             r'$ALG_4$',
             r'$ALG_5$',
             r'$ALG_6$'}
def plot_me(data, names, ax, unit, title, no=None,):
    ind = np.arange(len(data[0]))
    p1 = ax.bar(ind, data[0], width, color='r', alpha=0.4)
    p2 = ax.bar(ind, data[1], width, color='g', bottom=data[0], alpha=0.4)
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    for i in ind:
        d = 0
        if data[1][i] < 17.5: d = 17.5-data[1][i]
        ax.text(i, data[0][i] + data[1][i]+d, f'{round(data[1][i])}{unit[i]}', rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.7, 0.9, 1.), ))
        ax.text(i, data[0][i], f'{round(data[0][i])}{unit[i]}', rotation=0,
                ha="center", va="center", bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ))
    ax.legend((p1[0], p2[0]), ('Exp1', 'Exp2'), loc='upper left', prop={"size": 11})
    ax.set_title(rf'$ALG_{title}$')
    # ax.set_ylabel('\n'.join(wrap(f'Plot for {no} MECs', 8))).set_rotation(0)
    #ax.set_ylabel("No of Processes", fontsize=15)
    for label in ax.get_xticklabels():
        label.set_fontsize(9)
    if no:
        ax.xaxis.set_tick_params(labelsize=9)
        # ax.set_ylabel('\n'.join(wrap(f'{no} MECs', 8)), rotation=0, fontsize=15, labelpad=30)
        axx = ax.twinx()
        axx.set_yticklabels([])
        axx.set_yticks([])
        axx.set_ylabel('\n'.join(wrap(f'{no} MECs', 8)), rotation=0, fontsize=15, labelpad=30)


homo = {'time': timely2, **exe_homo, 'cpu': avg_cpu_homo, 'rtt': avg_rtt_homo, 'wt': avg_wt_homo}
het = {'time': timely1, **exec, 'cpu': avg_cpu, 'rtt': avg_rtt, 'wt': avg_wt}
# timely2 = {4: [79.3002, 95.3019, 92.9802, 92.0754, 90.2115, 91.8356], 7: [97.1986, 97.591, 96.4792, 94.9967, 95.7816, 96.0105], 10: [98.0052, 98.3431, 97.5038, 95.0294, 98.2123, 98.245]}

def form_plot():
    d = homo, het
    data = {i: {j:(list(range(7)),list(range(7))) for j in range(6)} for i in [4,7,10]}
    x = ['rtt', 'wt', 'cpu', 'time', 'mec', 'cloud', 'local']
    unit = ['ms', 'ms', '%', '%', '%', '%', '%']
    y = list(range(7))
    names = dict(zip(x,y))
    for i in range(2):
        for k, v in d[i].items():
            for l, t in v.items():
                for j in range(len(t)):
                    ind = names[k]
                    data[l][j][i][ind] = t[j]

    axes = [ax1, ax2, ax3, ax4, ax5, ax6,
            ax7, ax8, ax9, ax10, ax11, ax12,
            ax13, ax14, ax15, ax16, ax17, ax18]
    # plot_me(data, names, ax, unit, no=None)
    a = 0
    n = [5, 11, 17]
    nam = ['RTT', 'WT', 'CPU', 'Time', 'MEC', 'Cloud', 'Local']
    for no, va in data.items():
        for k, v in va.items():
            if a in n:
                plot_me(data=v, names=nam, ax=axes[a], unit=unit, title=k+1, no=no)
            else:
                plot_me(data=v, names=nam, ax=axes[a], unit=unit, title=k+1, no=None)
            a += 1
    plt.show()


form_plot()
# file = open('spead.csv', 'w', encoding='utf-8')
# file.write('homo\n')
# for k,v in homo.items():
#     file.write(f'{k}\n')
#     for d,j in v.items():
#         file.write(f'{d}\n')
#         t = [str(i) for i in j]
#         file.write(f'{",".join(t)}\n')
# file.write('het\n')
# for k,v in het.items():
#     file.write(f'{k}\n')
#     for d,j in v.items():
#         file.write(f'{d}\n')
#         t = [str(i) for i in j]
#         file.write(f'{",".join(t)}\n')
# file.close()

def do_me():
    names = ['rtt', 'wt', 'cpu', 'time']
    ks = [4,7,10]
    file = open('sp1.csv', 'w', encoding='utf-8')
    does = [homo, het]
    for name in names:
        ho = does[0][name]
        he = does[1][name]
        for k in ks:
            t = does[0][name][k]
            t = [str(i) for i in t]
            file.write(f'{",".join(t)}\n')
            t = does[1][name][k]
            t = [str(i) for i in t]
            file.write(f'{",".join(t)}\n')
    file.close()

#do_me()




def percentage(x, total):
    return round((x/total)*100, 4)

def format_(data):
    avg = {4:[], 7:[], 10:[]}
    for k, v in data[0].items():
        #t = list(v)
        for j in range(len(v)):
            to = v[j] + data[1][k][j]
            avg[k].append(percentage(v[j], to))
    print(avg)

def format_exe(data):
    r = {}
    didi = {0:{4: [], 7: [], 10: []}, 1:{4: [], 7: [], 10: []}, 2:{4: [], 7: [], 10: []}}
    for k, v in data.items():
        #print(v)
        for t,d in v.items():
            su = sum(d)
            for j in range(len(d)):
                g = percentage(d[j], su)
                didi[j][k].append(g)
    pa = {0: 'mec', 1:'local', 2:'cloud'}
    for k,v in didi.items():
        r[pa[k]] = v
    print(r)
                
# 
# format_(timely)
# format_(timely_homo)
#format_exe(exec_report)