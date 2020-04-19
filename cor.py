import numpy as np
import math
import random

class Cor():
    def __init__(self, number, dimension, mean=None, sigma=None):
        self.number = number
        self.dimension = dimension
        self.mean = mean or (math.pow(dimension, 0.5)) / 2
        self.sigma= sigma or 0.1
    
    def generate(self):
        noraml_distribution_arr = np.random.normal(self.mean, self.sigma, self.number)
        for i in noraml_distribution_arr:
            self.__generate_point(i)

        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            array2D[i] = self.__generate_point(noraml_distribution_arr[i])
        np.savetxt('cor' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array2D, fmt='%f')
    
    def __generate_point(self, normal_distribution_value):
            array = np.empty(self.dimension, dtype=float)
            max_value = normal_distribution_value
            count = 0
            for i in range (0, self.dimension - 1):
                random_value = np.random.random_sample() * max_value
                array[i] = (random_value)
                max_value -= random_value
                count += random_value
            array[self.dimension - 1] = normal_distribution_value - count
            np.random.shuffle(array)
            return array
            
cor = Cor(1, 5)
cor.generate()
