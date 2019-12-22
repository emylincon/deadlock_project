import numpy as np
import matplotlib.pyplot as plt

# marker size
n = 10

x = np.arange(1,100,10)
#x = np.arange(1, 7)

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

plt.plot(x, case1, 'r--+', label='RMS+Bankers', markersize=n)
plt.plot(x, case2, 'g-->', label='EDF+Bankers', markersize=n)
plt.plot(x, case3, 'y--o', label='RMS+Wound-wait', markersize=n)
plt.plot(x, case4, 'b--*', label='RMS+wait-die', markersize=n)
plt.plot(x, case5, 'c--s', label='EDF+Wound-wait', markersize=n)
plt.plot(x, case6, 'k--^', label='EDF+Wait-die', markersize=n)
plt.ylabel('No of Process')
plt.xlabel('No of Resources')

plt.title('Time Complexity Analysis')
# ax_dl.set_title('Deadlock Prevention/Avoidence Algorithms')

plt.legend()
# ax_rt.legend()
plt.show()
