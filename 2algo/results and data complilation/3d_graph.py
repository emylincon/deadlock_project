from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random as r

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# x, y, z = axes3d.get_test_data(0.05)

'''
x = np.array([[1, 2, 3, 5,  1, 8, 1], [3, 7, 4, 7, 7, 2, 5], [1, 7, 5, 9, 1, 2, 5]])
y = np.array([[1, 7, 5, 9, 1, 2, 5], [1, 9, 6, 5,  4, 8, 8], [3, 7, 4, 7, 7, 2, 5]])
#z = np.array([[1, 6, 8, 4, 5, 8, 3],[1, 3, 7, 6, 5, 9, 3]])
z = np.array([[4, 4, 4, 4, 4, 4, 4],[5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6]])

#ax.plot_wireframe(x,y,z, rstride=5, cstride=5)
ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
'''

x, y, z = [r.randrange(10) for i in list(range(10))], [r.randrange(10) for j in list(range(10))], \
          [r.randrange(10) for k in list(range(10))]
ax.plot(x,y,z)
plt.show()