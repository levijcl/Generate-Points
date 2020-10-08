import numpy as np
import math
import random
from util import PointGenerate
from tqdm import tqdm
class Cor(PointGenerate):
    def __init__(self, number, dimension):
        sigma = dimension / 5
        super().__init__(number, dimension, sigma)
        self.bar = tqdm(total=self.number, desc='Cor-' + str(self.dimension))

    def generate(self):
        normal_distribution_arr = self.generate_normal_distribution_arr()
        with open('cor' + str(self.dimension) + 'D-' + str(self.number) + '.txt', 'a') as file:
            for i in range(0, self.number):
                point = self.generate_noraml_point(normal_distribution_arr[i])
                shuffled_point = self.shuffle(point)
                file.write(' '.join(str("{:0.6f}".format(number)) for number in shuffled_point) + '\n')
                self.bar.update(1)

    def output_points(self):
        normal_distribution_arr = self.generate_normal_distribution_arr()
        array2D = np.empty((self.number, self.dimension), dtype=float)
        for i in range(0, self.number):
            point = self.generate_noraml_point(normal_distribution_arr[i])
            array2D[i] = point
            self.bar.update(1)
        return array2D
  
def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    cor = Cor(number, dimension)
    cor.generate()

if __name__ == "__main__":
    main()
