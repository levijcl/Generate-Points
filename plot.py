import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import cm

def plot2D(data):
    x, y = np.array(data).T
    plt.scatter(x, y, s=3)
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

def plot_mosaic(data):
    """
    Helper function to plot data with associated colormap.
    """
    viridis = cm.get_cmap('viridis', 256)

    arr = np.array(data)
    length = len(data)
    bar = [viridis]
    for i in range(0, length - 1):
        bar += [viridis]

    fig, axs = plt.subplots(4, 3, figsize=(8, 6),
                            constrained_layout=True, squeeze=False)

    count = 0
    for [ax, cmap] in zip(axs.flat, bar):
        psm = ax.pcolormesh(data[count], cmap=cmap, rasterized=True, vmin=arr.min(), vmax=arr.max())
        fig.colorbar(psm, ax=ax)
        count += 1 

    
    plt.show()

def read_file(file_path):
    start = file_path.find('-')
    end = file_path.find('.csv')
    size = int(file_path[start + 1 : end])
    m = {}
    for i in range(0, size):
        m.update({i: 0})
    
    with open(file_path, 'r') as f:
        for i in f.readlines():
            key = int(i.split(',')[0])
            value = int(i.split(',')[1])
            m.update({key: value})
    return m

def generate_2d(m, dimension=1):
    data = []
    for d in range(0, dimension):
        length  = len(m) / dimension
        size = math.ceil((math.sqrt(length))) 
        arr_2d = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                row.append(m.get(j * size + i + d * size * size))
            arr_2d.append(row)
        data.append(arr_2d)
    return data

m = read_file('/Users/chiangchanglin/Desktop/localSkyline-54000.csv')
data = generate_2d(m, 60)
plot_mosaic(data)
