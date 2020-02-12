from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as snc

fig = plt.figure()
ax1 = fig.add_subplot(141)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(144)
#ax5 = fig.add_subplot(211)

'''
4 mecs: mean = 4, sd = 4.5
5 mecs: mean = 4, sd = 4.5
6 mecs: mean = 4, sd = 4
7 mecs: mean = 6, sd = 4
'''

no_of_mec = 7
no_of_req = 1800


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


y = get_truncated_normal(mean=4,
                         sd=4.5,
                         low=1,
                         upp=4).rvs(no_of_req)

# print(y)

y = [round(i) for i in y]
freq = {i:y.count(i) for i in set(y)}
ax1.hist(y, label='4 MEC', color='g', alpha=0.3)
ax1.plot([1]+list(freq.keys())+[4], [0]+list(freq.values())+[0], 'g-.^', lw=2, alpha=0.6)
#ax1.legend()
ax1.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax1.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax1.set_xticks(np.arange(min(y), max(y) + 1,1))
ax1.set_title("Distribution for 4 MECs", fontdict={'weight': 'bold', 'size': 17})
#ax2.set_xticks([min(y) - 1, max(y) + 1])
#snc.kdeplot(y, label='sd=1')
print(freq)
print(f'mec4 = {y}')
#print(y)
z = get_truncated_normal(mean=4,
                         sd=4.5,
                         low=1,
                         upp=5).rvs(no_of_req)
#snc.kdeplot(z, label='sd=2')
z = [round(i) for i in z]
freq = {i:z.count(i) for i in set(z)}
print(freq)
print(f'mec5 = {z}')
ax2.hist(z, label='5 MEC', color='r', alpha=0.3)
ax2.plot([1]+list(freq.keys())+[5], [0]+list(freq.values())+[0], 'r-.o', lw=2, alpha=0.6)
#ax2.legend()
ax2.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax2.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax2.set_xticks(np.arange(min(z), max(z) + 1,1))
ax2.set_title("Distribution for 5 MECs", fontdict={'weight': 'bold', 'size': 17})
x = get_truncated_normal(mean=4,
                         sd=4,
                         low=1,
                         upp=6).rvs(no_of_req)
#ax2.set_xticks([min(z) - 1, max(z) + 1])
#snc.kdeplot(x, label='sd=3')
x = [round(i) for i in x]
freq = {i:x.count(i) for i in set(x)}
print(freq)
print(f'mec6 = {x}')
ax3.hist(x, label='6 MEC', color='b', alpha=0.3)
ax3.plot([1]+list(freq.keys())+[6], [0]+list(freq.values())+[0], 'b-.s', lw=2, alpha=0.6)
#ax3.legend()
ax3.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax3.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax3.set_xticks(np.arange(min(x), max(x) + 1,1))
ax3.set_title("Distribution for 6 MECs", fontdict={'weight': 'bold', 'size': 17})
u = get_truncated_normal(mean=6,
                         sd=4,
                         low=1,
                         upp=7).rvs(no_of_req)
#snc.kdeplot(u, label='sd=4')
u = [round(i) for i in u]
freq = {i:u.count(i) for i in set(u)}
print(freq)
print(f'mec7 = {u}')
ax4.hist(u, label='7 MEC', color='m', alpha=0.3)
ax4.plot([1]+list(freq.keys())+[7], [0]+list(freq.values())+[0], 'm-.*', lw=2, alpha=0.6)
ax4.set_xticks(np.arange(min(u), max(u) + 1,1))
#ax4.legend()
ax4.set_ylabel('No of Requests', fontdict={'weight': 'medium', 'size': 14})
ax4.set_xlabel('No of MECs', fontdict={'weight': 'medium', 'size': 14})
ax4.set_title("Distribution for 7 MECs", fontdict={'weight': 'bold', 'size': 17})
plt.show()
