import numpy as np
from matplotlib import pyplot as plt

def plot2D(data):
    x, y = np.array(data).T
    plt.scatter(x,y,s=3)
    plt.show()

def plot3D(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = []
    y = []
    z = []
    for point in data:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.scatter(x, y, z, s=0.5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.plot3D([0, 1], [0, 1], [0, 1], 'gray')
    plt.show()
