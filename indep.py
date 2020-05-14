import numpy as np
import math
import random
from plot import plot2D, plot3D

class Indep():
    def __init__(self, number, dimension):
        self.number = number
        self.dimension = dimension
    
    def generate(self):
        array = np.random.rand(self.number, self.dimension)
        np.savetxt('indep' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array, fmt='%f')
        return array

def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    indep = Indep(number, dimension)
    data = indep.generate()
if __name__ == "__main__":
    main()

