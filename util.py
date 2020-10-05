import numpy as np
import math
class PointGenerate():
    def __init__(self, number, dimension, sigma, mean=None):
        self.number = number
        self.dimension = dimension
        self.mean = mean or dimension / 2
        self.sigma = sigma
        self.factorial = math.factorial(dimension) / 2

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
        point_arr = list(point_arr)
        sort_point = point_arr[:]
        sort_point.sort()
        sort_point = sort_point[::-1]

        order_list = []
        shuffled_arr = np.full(self.dimension, -1, dtype=float)

        for i in range(1, self.dimension - 1):
            fac = math.factorial(self.dimension - i) / 2
            order = int(rand / fac)
            order_list.append(order)
            rand = rand % fac

        order_list = order_list[::-1]
        for i in range(0, len(order_list)):
            for j in range(i + 1 , len(order_list)):
                if order_list[i] >= order_list[j]:
                    order_list[i] = order_list[i] +1
        order_list = order_list[::-1]

        for index, value in enumerate(order_list):
            target_value = sort_point.pop(0)
            shuffled_arr[value] = target_value
            point_arr.pop(point_arr.index(target_value))

        for index, value in enumerate(shuffled_arr):
            if value == -1:
                shuffled_arr[index] = point_arr.pop(0)

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
