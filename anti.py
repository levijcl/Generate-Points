import numpy as np
import math
import random

from tqdm import tqdm
from util import PointGenerate

class Anti(PointGenerate):
    def __init__(self, number, dimension):
        sigma= math.pow(dimension, 0.5) / 14
        super().__init__(number, dimension, sigma)
        self.bar = tqdm(total=self.number, desc='Anti-' + str(self.dimension))

    def generate(self):
        normal_distribution_arr = self.generate_normal_distribution_arr()
        with open('anti' + str(self.dimension) + 'D-' + str(self.number) + '.txt', 'a') as file:
            for i in range(0, self.number):
                point = self.generate_uniform_point(normal_distribution_arr[i])
                shuffled_point = self.shuffle(point)
                file.write(' '.join(str("{:0.6f}".format(number)) for number in shuffled_point) + '\n')
                self.bar.update(1)

    def output_points(self):
        normal_distribution_arr = self.generate_normal_distribution_arr()
        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            point = self.generate_uniform_point(normal_distribution_arr[i])
            array2D[i] = point
            self.bar.update(1)
        return array2D
  
def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    anti = Anti(number, dimension)
    anti.generate()
if __name__ == "__main__":
    main()
