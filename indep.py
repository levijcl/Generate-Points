import numpy as np
import math
import random

class Indep():
    def __init__(self, number, dimension):
        self.number = number
        self.dimension = dimension
    
    def generate(self):
        array2D = np.random.rand(self.number, self.dimension)
        np.savetxt('indep' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array2D, fmt='%f')

def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    indep = Indep(number, dimension)
    indep.generate()

if __name__ == "__main__":
    main()

