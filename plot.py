import numpy as np
from matplotlib import pyplot as plt

def plot2D(data):
    x, y = np.array(data).T
    plt.scatter(x,y)
    plt.show()
