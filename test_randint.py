import numpy as np
import math

dim = 13
fac = math.factorial(dim)

with open('test.txt', 'a') as file:
    for i in range(0, 1000):
        rand = np.random.randint(0, fac)
        file.write(str(rand) + '\n')
