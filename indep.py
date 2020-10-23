import numpy as np
import math
import random
from tqdm import tqdm
from util import PointGenerate

class Indep(PointGenerate):
    def __init__(self, number, dimension):
        self.number = number
        self.dimension = dimension
        super().__init__(number, dimension, 1)
        self.bar = tqdm(total=self.number, desc='Indep-' + str(self.dimension))

    def generate(self):
        with open('indep' + str(self.dimension) + 'D-' + str(self.number) + '.txt', 'a') as file:
            for _ in range(0, self.number):
                point = np.random.rand(self.dimension)
                shuffled_point = self.shuffle(point)
                file.write(' '.join(str("{:0.6f}".format(number)) for number in shuffled_point) + '\n')
                self.bar.update(1)

def main():
    number = int(input("number of points:"))
    dimension = int(input("dimension:"))
    indep = Indep(number, dimension)
    indep.generate()
if __name__ == "__main__":
    main()

