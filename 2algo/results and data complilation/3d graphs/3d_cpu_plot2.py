from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import random as r
import heterogenous_data as het_data
import homogenous_data as hom_data

fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
ax1 = fig.add_subplot(132, projection='3d')
ax2 = fig.add_subplot(133, projection='3d')

def _mov_avg(a1):
    ma1=[] # moving average list
    avg1=0 # movinf average pointwise
    count=0
    for i in range(len(a1)):
        count+=1
        avg1=((count-1)*avg1+a1[i])/count
        ma1.append(avg1) #cumulative average formula
        # μ_n=((n-1) μ_(n-1)  + x_n)/n
    return ma1


def line_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    '''
    x, y, z = np.array([[r.randrange(10) for i in list(range(10))]]), np.array([[r.randrange(10) for j in list(range(10))]]), \
              np.array([[r.randrange(10) for k in list(range(10))], [r.randrange(10) for h in list(range(10))]])
    '''
    # ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    y = np.array(_mov_avg(hom_data.cpu_1))
    x = np.array(list(range(500)))
    z = np.array([i for i in list(range(500))])
    ax.plot(x,y,z)
    #ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)

    plt.show()


def surface_graph():
    # ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    y1 = np.array([_mov_avg(hom_data.cpu_1)])
    x1 = np.array([list(range(500))])
    z1 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x1, y1, z1, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0, label='RMS + Bankers')

    y2 = np.array([_mov_avg(hom_data.cpu_3)])
    x2 = np.array([list(range(500))])
    z2 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x2, y2, z2, color='r', rstride=1, cstride=1, linewidth=0, label='EDF + Bankers')

    y3 = np.array([_mov_avg(hom_data.cpu_5)])
    x3 = np.array([list(range(500))])
    z3 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x3, y3, z3, color='y', rstride=1, cstride=1, linewidth=0, label='RMS + wound wait')

    y4 = np.array([_mov_avg(hom_data.cpu_8)])
    x4 = np.array([list(range(500))])
    z4 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x4, y4, z4, color='m', rstride=1, cstride=1, linewidth=0, label='RMS + wait die')

    y5 = np.array([_mov_avg(hom_data.cpu_11)])
    x5 = np.array([list(range(500))])
    z5 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x5, y5, z5, color='c', rstride=1, cstride=1, linewidth=0, label='EDF + wound wait')

    y6 = np.array([_mov_avg(hom_data.cpu_16)])
    x6 = np.array([list(range(500))])
    z6 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax.plot_surface(x6, y6, z6, color='k', rstride=1, cstride=1, linewidth=0, label='EDF + wait die')

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # cmap=cm.coolwarm

    ax.set_title('Moving CPU Utilization for 4 MEC Set-up')
    ax.set_ylabel('Moving CPU')
    ax.set_xlabel('Time (seconds)')
    #ax.legend()

    #plt.show()


def surface_5_graph():
    # ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    y1 = np.array([_mov_avg(hom_data.cpu_1_5)])
    x1 = np.array([list(range(500))])
    z1 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x1, y1, z1, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0, label='RMS + Bankers')

    y2 = np.array([_mov_avg(hom_data.cpu_3_5)])
    x2 = np.array([list(range(500))])
    z2 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x2, y2, z2, color='r', rstride=1, cstride=1, linewidth=0, label='EDF + Bankers')

    y3 = np.array([_mov_avg(hom_data.cpu_5_5)])
    x3 = np.array([list(range(500))])
    z3 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x3, y3, z3, color='y', rstride=1, cstride=1, linewidth=0, label='RMS + wound wait')

    y4 = np.array([_mov_avg(hom_data.cpu_8_5)])
    x4 = np.array([list(range(500))])
    z4 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x4, y4, z4, color='m', rstride=1, cstride=1, linewidth=0, label='RMS + wait die')

    y5 = np.array([_mov_avg(hom_data.cpu_11_5)])
    x5 = np.array([list(range(500))])
    z5 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x5, y5, z5, color='c', rstride=1, cstride=1, linewidth=0, label='EDF + wound wait')

    y6 = np.array([_mov_avg(hom_data.cpu_16_5)])
    x6 = np.array([list(range(500))])
    z6 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax1.plot_surface(x6, y6, z6, color='k', rstride=1, cstride=1, linewidth=0, label='EDF + wait die')

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # cmap=cm.coolwarm

    ax1.set_title('Moving CPU Utilization for 5 MEC Set-up')
    ax1.set_ylabel('Moving CPU')
    ax1.set_xlabel('Time (seconds)')


def surface_6_graph():
    # ax1.plot(list(range(500)), _mov_avg(data.cpu_1), linewidth=2, label='RMS + Bankers')
    y1 = np.array([_mov_avg(hom_data.cpu_1_6)])
    x1 = np.array([list(range(500))])
    z1 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x1, y1, z1, cmap=plt.cm.jet, rstride=3, cstride=3, linewidth=0, label='RMS + Bankers')

    y2 = np.array([_mov_avg(hom_data.cpu_3_6)])
    x2 = np.array([list(range(500))])
    z2 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x2, y2, z2, color='r', rstride=3, cstride=3, linewidth=0, label='EDF + Bankers')

    y3 = np.array([_mov_avg(hom_data.cpu_5_6)])
    x3 = np.array([list(range(500))])
    z3 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x3, y3, z3, color='y', rstride=3, cstride=3, linewidth=0, label='RMS + wound wait')

    y4 = np.array([_mov_avg(hom_data.cpu_8_6)])
    x4 = np.array([list(range(500))])
    z4 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x4, y4, z4, color='m', rstride=3, cstride=3, linewidth=0, label='RMS + wait die')

    y5 = np.array([_mov_avg(hom_data.cpu_11_6)])
    x5 = np.array([list(range(500))])
    z5 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x5, y5, z5, color='c', rstride=3, cstride=3, linewidth=0, label='EDF + wound wait')

    y6 = np.array([_mov_avg(hom_data.cpu_16_6)])
    x6 = np.array([list(range(500))])
    z6 = np.array([[i for i in list(range(500))], [i for i in list(range(500))]])
    ax2.plot_surface(x6, y6, z6, color='k', rstride=3, cstride=3, linewidth=0, label='EDF + wait die')

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # cmap=cm.coolwarm

    ax2.set_title('Moving CPU Utilization for 6 MEC Set-up')
    ax2.set_ylabel('Moving CPU')
    ax2.set_xlabel('Time (seconds)')


def plot_graphs():
    surface_graph()
    surface_5_graph()
    surface_6_graph()
    fig.suptitle('MEC CPU Utilization During Deadlock Experiment')
    plt.show()



plot_graphs()


#surface_graph()