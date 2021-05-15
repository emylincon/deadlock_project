import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 22})
# marker size
n = 10

x = np.arange(1, 100, 10)
# x = np.arange(1, 7)
algo_dict = {'RMS+Bankers': r'$ALG_1$',
             'EDF+Bankers': r'$ALG_2$',
             'RMS+wound wait': r'$ALG_3$',
             'RMS+wait die': r'$ALG_4$',
             'EDF+wound wait': r'$ALG_5$',
             'EDF+wait die': r'$ALG_6$'}
y1 = x ** 2
y2 = x * (2 ** (1 / x) - 1)
y3 = x * np.log2(x)
y4 = x
y5 = x

case1 = y1 + y2
case2 = y3 + y1
case3 = y2 + y4
case4 = y2 + y5
case5 = y3 + y4
case6 = y3 + y5

plt.grid(True)

plt.yscale('log')

plt.plot(x, case1, 'r--+', label=algo_dict['RMS+Bankers'], markersize=n)
plt.plot(x, case2, 'g-->', label=algo_dict['EDF+Bankers'], markersize=n)
plt.plot(x, case3, 'y--o', label=algo_dict['RMS+wound wait'], markersize=n)
plt.plot(x, case4, 'b--*', label=algo_dict['RMS+wait die'], markersize=n)
plt.plot(x, case5, 'c--s', label=algo_dict['EDF+wound wait'], markersize=n)
plt.plot(x, case6, 'k--^', label=algo_dict['EDF+wait die'], markersize=n)
plt.ylabel('No of Process')
plt.xlabel('No of Resources Types')

plt.title('Time Complexity Analysis')
# ax_dl.set_title('Deadlock Prevention/Avoidence Algorithms')

plt.legend()
# ax_rt.legend()
plt.show()

#https://matplotlib.org/3.1.1/tutorials/text/mathtext.html