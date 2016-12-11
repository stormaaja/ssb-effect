#!/bin/python

from grid import Grid
import time

initial_time = time.time()
grid = Grid(30)
grid.create_new_random_matrix()
print("Initial matrix:")
print(grid.to_str())
initial_average = grid.get_average()
print("Initial average: {}".format(initial_average))
print("\n")
iterations = 0
while grid.get_max_delta() > 0.0001:
    average_grid = grid.calculate_average_grid()
    grid.set_matrix(average_grid.get_matrix())
    iterations += 1

print("Final matrix:")
print(grid.to_str())
print("With {0} iterations in {1:.3f} milliseconds".format(
    iterations, (time.time() - initial_time) * 1000.0))
print("Difference of averages: {}".format(
    abs(initial_average - grid.get_average())))
