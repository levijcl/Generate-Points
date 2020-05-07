import numpy as np
import math
import random
from plot import plot2D

class Anti():
    def __init__(self, number, dimension, mean=None, sigma=None):
        self.number = number
        self.dimension = dimension
        self.mean = mean or dimension /2 
        self.sigma= sigma or (math.pow(dimension, 0.5)) / 20
    
    def generate(self):
        noraml_distribution_arr = np.random.normal(self.mean, self.sigma, self.number)
        while True:
            if np.all(noraml_distribution_arr > 0) and np.all(noraml_distribution_arr < self.dimension):
                break
            sholud_delete = []
            for index, value in enumerate(noraml_distribution_arr):
                if value > (self.dimension) or value < 0:
                    sholud_delete.append(index)
            noraml_distribution_arr = np.delete(noraml_distribution_arr, sholud_delete)
            added_noraml_distribution_arr = np.random.normal(self.mean, self.sigma, self.number - np.size(noraml_distribution_arr))
            noraml_distribution_arr = np.append(noraml_distribution_arr, added_noraml_distribution_arr)
        for i in noraml_distribution_arr:
            self.__generate_point(i)
        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            array2D[i] = self.__generate_point(noraml_distribution_arr[i])
        np.savetxt('anti' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array2D, fmt='%f')
        return array2D
    
    def __generate_point(self, normal_distribution_value):
        while True:
            array = np.empty(self.dimension, dtype=float)
            max_value = normal_distribution_value
            sum = 0
            count = 0
            while count < self.dimension - 1:
                random_value = np.random.random_sample() * max_value
                if random_value < 1:
                    array[count] = random_value
                    max_value = max_value - random_value
                    sum += random_value
                    count += 1
                else:
                    continue
            array[self.dimension - 1] = normal_distribution_value - sum
            if np.all(array < 1) and np.all(array >= 0):
                break
        return array
            
def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    anti = Anti(number, dimension)
    data = anti.generate()
if __name__ == "__main__":
    main()
