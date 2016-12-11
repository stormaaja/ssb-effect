import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest
from grid import Grid

class TestGridMethods(unittest.TestCase):

    def create_example_3by3_grid() -> Grid:
        grid = Grid(3)
        grid.set_value(0, 0, 0.1)
        grid.set_value(0, 1, 0.1)
        grid.set_value(0, 2, 0.1)
        grid.set_value(1, 0, 0.2)
        grid.set_value(1, 1, 0.2)
        grid.set_value(1, 2, 0.2)
        grid.set_value(2, 0, 0.3)
        grid.set_value(2, 1, 0.3)
        grid.set_value(2, 2, 0.3)

        return grid

    def create_new_random_matrix(self):
        grid = Grid(9)
        grid.create_new_random_matrix()
        self.assertEqual(len(grid.get_matrix()), 9 * 9)
        self.assertTrue(grid.get_value(3, 3) >= 0.0)
        self.assertTrue(grid.get_value(3, 3) <= 1.0)

    def test_generate_zero_matrix(self):
        matrix = Grid.generate_zero_matrix(3)
        self.assertTrue(len(matrix), 3 * 3)
        self.assertEqual(matrix[0], 0.0)
        self.assertEqual(matrix[8], 0.0)

    def test_get_sub_matrix_average(self):
        grid = Grid(9)
        grid.set_value(1, 1, 0.5)
        grid.set_value(1, 2, 0.5)
        grid.set_value(1, 3, 0.5)
        grid.set_value(2, 1, 0.5)
        grid.set_value(2, 2, 0.5)
        grid.set_value(2, 3, 0.5)
        grid.set_value(3, 1, 0.5)
        grid.set_value(3, 2, 0.5)
        grid.set_value(3, 3, 0.5)
        self.assertAlmostEqual(
            grid.get_sub_matrix_average(2, 2), 0.5, delta=0.001)

        grid = Grid(9)
        grid.set_value(0, 0, 0.1)
        grid.set_value(0, 1, 0.1)
        grid.set_value(1, 1, 0.3)
        grid.set_value(1, 0, 0.3)
        self.assertAlmostEqual(
            grid.get_sub_matrix_average(0, 0), 0.2, delta=0.001)

        with self.assertRaises(IndexError):
            grid.get_sub_matrix_average(-2, -2)

    def test_get_value(self):
        grid = Grid(9)
        grid.set_value(0, 0, 0.5)
        self.assertAlmostEqual(grid.get_value(0, 0), 0.5, delta=0.001)

        grid.set_value(8, 8, 0.1)
        self.assertAlmostEqual(grid.get_value(8, 8), 0.1, delta=0.001)

        grid.set_value(0, 3, 0.2)
        self.assertAlmostEqual(grid.get_value(0, 3), 0.2, delta=0.001)

        with self.assertRaises(IndexError):
            grid.get_value(-1, -1)
        with self.assertRaises(IndexError):
            grid.get_value(9, 9)

    def test_set_value(self):
        grid = Grid(9)
        grid.set_value(2, 2, 0.9)
        self.assertAlmostEqual(grid.get_value(2, 2), 0.9, delta=0.001)

        with self.assertRaises(IndexError):
            grid.set_value(-1, -1, 0.0)
        with self.assertRaises(IndexError):
            grid.set_value(9, 9, 0.0)

    def test_calculate_average_grid(self):
        grid = TestGridMethods.create_example_3by3_grid()
        average_grid = grid.calculate_average_grid()
        self.assertAlmostEqual(
            average_grid.get_value(0, 0), 0.15, delta=0.0001)

        self.assertAlmostEqual(
            average_grid.get_value(1, 1), 0.2, delta=0.0001)

    def test_get_average(self):
        grid = TestGridMethods.create_example_3by3_grid()

        self.assertAlmostEqual(grid.get_average(), 0.2, delta=0.0001)

    def test_get_max_delta(self):
        grid = TestGridMethods.create_example_3by3_grid()

        self.assertAlmostEqual(grid.get_max_delta(), 0.2, delta=0.0001)

    def test_to_str(self):
        grid = TestGridMethods.create_example_3by3_grid()
        self.assertEqual(grid.to_str(),
            "| 0.100, 0.100, 0.100 |\n| 0.200, 0.200, 0.200 |\n| 0.300, 0.300, 0.300 |")

if __name__ == '__main__':
    unittest.main()
