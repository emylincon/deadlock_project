from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as snc

fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

no_of_mec = 7
no_of_req = 9000


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


y = get_truncated_normal(mean=4,
                         sd=4.5,
                         low=1,
                         upp=5).rvs(no_of_req)

# print(y)

y = [round(i) for i in y]
freq = {i:y.count(i) for i in set(y)}
a, b = list(freq.keys()), list(freq.values())
ax1.bar(a, b, label='5 MEC', color='g', alpha=0.3)
ax1.plot([1]+a+[5], [0]+b+[0], 'g-.^', lw=2, alpha=0.6)
#ax1.legend()
ax1.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax1.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax1.set_xticks(np.arange(min(y), max(y) + 1,1))
ax1.set_title("Distribution for 5 MECs", fontdict={'weight': 'bold', 'size': 17})
#ax2.set_xticks([min(y) - 1, max(y) + 1])
#snc.kdeplot(y, label='sd=1')
print('freq5 =',freq)
print(f'mec5 = {y}')
#print(y)
z = get_truncated_normal(mean=5,
                         sd=7,
                         low=1,
                         upp=10).rvs(no_of_req)
#snc.kdeplot(z, label='sd=2')
z = [round(i) for i in z]
freq = {i:z.count(i) for i in set(z)}
print('freq10 =',freq)
print(f'mec10 = {z}')
x, y = list(freq.keys()), list(freq.values())
ax2.bar(x, y, width=.7, color='r', alpha=0.3)
ax2.plot([1]+x+[10], [0]+y+[0], 'r-.o', lw=2, alpha=0.6)
#ax2.legend()
ax2.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax2.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax2.set_xticks(np.arange(min(z), max(z) + 1,1))
ax2.set_title("Distribution for 10 MECs", fontdict={'weight': 'bold', 'size': 17})
w = get_truncated_normal(mean=10,
                         sd=8,
                         low=1,
                         upp=15).rvs(no_of_req)
#ax2.set_xticks([min(z) - 1, max(z) + 1])
#snc.kdeplot(x, label='sd=3')
w = [round(i) for i in w]
freq = {i:w.count(i) for i in set(w)}
print('freq15 =',freq)
print(f'mec15 = {w}')
#ax3.hist(w, label='15 MEC', color='b', alpha=0.3)
x, y = list(freq.keys()), list(freq.values())
ax3.bar(x, y, width=.5, color='b', alpha=0.3)
ax3.plot([1]+x+[15], [0]+y+[0], 'b-.s', lw=2, alpha=0.6)
#ax3.legend()
ax3.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax3.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax3.set_xticks(np.arange(min(w), max(w) + 1, 1))
ax3.set_title("Distribution for 15 MECs", fontdict={'weight': 'bold', 'size': 17})


plt.show()
