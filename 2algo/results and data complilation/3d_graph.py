from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# x, y, z = axes3d.get_test_data(0.05)

x = np.array([1, 2, 3, 5,  1, 8, 9])
y = np.array([1, 7, 5, 9, 1, 2, 3])
z = np.array([[1, 6, 8, 4, 5, 8, 3],[1, 3, 7, 6, 5, 9, 3]])

ax.plot_wireframe(x,y,z, rstride=5, cstride=5)

plt.show()