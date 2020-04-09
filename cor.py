import numpy as np
import math
import random

class Cor():
    def __init__(self, number, dimension):
        self.number = number
        self.dimension = dimension
    
    def generate(self):
        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            array2D[i] = np.random.uniform(0, 10000, self.dimension)
        np.savetxt('cor' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array2D, fmt='%f')


cor = Cor(1000000, 4)
cor.generate()
