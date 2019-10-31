from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# x, y, z = axes3d.get_test_data(0.05)

x = [1, 2, 3, 5,  1, 8, 9]
y = [1, 7, 5, 9, 1, 2, 3]
z = [1, 6, 8, 4, 5, 8, 3]

#ax.scatter(x,y,z, c='r', marker='o')
ax.scatter(x,y,z, c=np.linalg.norm([x,y,x], axis=0), marker='o')


ax.set_ylabel('y axis')
ax.set_xlabel('x axis')
ax.set_zlabel('z axis')

plt.show()