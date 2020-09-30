import numpy as np
import math 
class PointGenerate():
    def __init__(self, number, dimension, sigma, mean=None):
        self.number = number
        self.dimension = dimension
        self.mean = mean or dimension / 2
        self.sigma = sigma
        self.factorial = math.factorial(dimension)

    def generate_normal_distribution_arr(self):
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
        return noraml_distribution_arr

    # def generate_point(self, normal_distribution_value):
    #     while True:
    #         array = np.empty(self.dimension, dtype=float)
    #         value_in_axis = normal_distribution_value / self.dimension
    #         boundary = 1 if value_in_axis > 0.50 else 0
    #         interval = abs(boundary - value_in_axis)
    #         low = boundary if boundary == 0 else value_in_axis - interval
    #         high = boundary if boundary == 1 else value_in_axis + interval
    #         sum = 0
    #         count = 0
    #         while count < self.dimension - 1:
    #             random_value = np.random.uniform(low, high)
    #             if random_value < 1:
    #                 array[count] = random_value
    #                 sum += random_value
    #                 count += 1
    #             else:
    #                 continue
    #         array[self.dimension - 1] = normal_distribution_value - sum
    #         if np.all(array < 1) and np.all(array >= 0):
    #             break
    #     return array
    def generate_noraml_point(self, normal_distribution_value):
        while True:
            array = np.empty(self.dimension, dtype=float)
            value_in_axis = normal_distribution_value / self.dimension
            mean = np.full(self.dimension, value_in_axis)
            cov = self.generate_covariance(normal_distribution_value)
            indiviaul_values = np.random.multivariate_normal(mean, cov)
            scale = normal_distribution_value / sum(indiviaul_values)
            array = np.array([i * scale for i in indiviaul_values])
            if np.all(array < 1) and np.all(array >= 0):
                break
        return array

    def generate_uniform_point(self, normal_distribution_value):
        while True:
            array = np.empty(self.dimension, dtype=float)
            indiviaul_values = np.random.uniform(0, 1, size=self.dimension)
            scale = normal_distribution_value / sum(indiviaul_values)
            array = np.array([i * scale for i in indiviaul_values])
            if np.all(array < 1) and np.all(array >= 0):
                break
        return array

    def shuffle(self, point_arr):
            rand = np.random.randint(0, self.factorial)
            point_arr[::-1].sort()
            order_list = []
            shuffled_arr = []

            for i in range(1, self.dimension):
                fac = math.factorial(self.dimension - i)
                order = int(rand / fac)
                order_list.append(order)
                rand = rand % fac
            
            index_order = []
            pick_order = []
            for i in range(0, self.dimension):
                pick_order.append(i)
            
            for i in range(0, len(order_list)):
                index = order_list[i]
                index_order.append(pick_order[index])
                pick_order.pop(index)

            ready_to_pop = []
            for i in range(0, self.dimension):
                ready_to_pop.append(i)

            for index, item in enumerate(index_order):
                ready_to_pop.pop(ready_to_pop.index(item))

            index_order.append(ready_to_pop[0])

            for index in range(0, len(index_order)):
                shuffled_arr.append(point_arr[index_order.index(index)])

            return shuffled_arr

    def generate_covariance(self, normal_distribution_value):
        value_in_axis = normal_distribution_value / self.dimension
        boundary = 1 if value_in_axis > 0.50 else 0
        interval = abs(boundary - value_in_axis)
        cov = []
        for i in range(0, self.dimension):
            row = []
            for j in range(0, self.dimension):
                if i == j:
                    row.append(math.pow(interval / 3, 2))
                else:
                    row.append(0)
            cov.append(row)
        return cov
