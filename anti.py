import numpy as np
import math
import random

class Anti():
    def __init__(self, number, dimension, mean=None, sigma=None):
        self.number = number
        self.dimension = dimension
        self.mean = mean or (math.pow(dimension, 0.5)) / 2
        self.sigma= sigma or 0.05
    
    def generate(self):
        noraml_distribution_arr = np.random.normal(self.mean, self.sigma, self.number)
        for i in noraml_distribution_arr:
            self.__generate_point(i)

        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            array2D[i] = self.__generate_point(noraml_distribution_arr[i])
        np.savetxt('cor' + str(self.dimension) + 'D-' + str(self.number) + '.txt', array2D, fmt='%f')
        return array2D
    
    def __generate_point(self, normal_distribution_value):
            array = np.empty(self.dimension, dtype=float)
            max_value = normal_distribution_value
            sum = 0
            count = 0
            while count < self.dimension - 1:
                random_value = np.random.random_sample() * max_value
                if random_value < 1:
                    array[count] = (random_value)
                    max_value -= random_value
                    sum += random_value
                    count += 1
                else:
                    continue
            array[self.dimension - 1] = normal_distribution_value - sum
            np.random.shuffle(array)
            return array
            
def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    anti = Anti(number, dimension)
    anti.generate()

if __name__ == "__main__":
    main()
