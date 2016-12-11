import random

class Grid:

    def __init__(self, size: float):
        self.size = size
        self.matrix = Grid.generate_zero_matrix(size)

    def create_new_random_matrix(self):
        self.matrix = Grid.generate_random_matrix(self.size)

    def get_matrix(self) -> list:
        return self.matrix

    def set_matrix(self, matrix: list):
        self.matrix = matrix

    def get_value(self, x: int, y: int) -> float:
        if 0 > x <= self.size or 0 > y <= self.size:
            raise IndexError("Coordinates out of range")
        return self.matrix[y * self.size + x]

    def set_value(self, x: int, y: int, value: float):
        if 0 > x <= self.size or 0 > y <= self.size:
            raise IndexError("Coordinates out of range")

        self.matrix[y * self.size + x] = value

    def get_sub_matrix_average(self, x: int, y: int) -> float:
        sub_matrix_sum = 0.0
        sub_matrix_item_count = 0
        for sub_x in range(x - 1, x + 2):
            for sub_y in range(y - 1, y + 2):
                try:
                    sub_matrix_sum += self.get_value(sub_x, sub_y)
                    sub_matrix_item_count += 1
                except IndexError as indexError:
                    pass

        if sub_matrix_item_count == 0:
            raise IndexError("Sub matrix out of parent")

        return sub_matrix_sum / (sub_matrix_item_count * 1.0)

    def get_average(self) -> float:
        average = 0.0
        for x in self.matrix:
            average += x

        return average / (self.size * self.size * 1.0)

    def get_max_delta(self) -> float:
        return max(self.matrix) - min(self.matrix)

    def calculate_average_grid(self) -> 'Grid':
        new_grid = Grid(self.size)
        for x in range(0, self.size):
            for y in range(0, self.size):
                new_grid.set_value(x, y, self.get_sub_matrix_average(x, y))

        return new_grid

    def to_str(self) -> str:
        values_str = ""
        for x in range(0, self.size):
            values_str += "| "
            for y in range(0, self.size):
                if y > 0:
                    values_str += ", "
                values_str += "{0:.3f}".format(self.get_value(x, y))
            values_str += " |"
            if y < self.size - 1 or x < self.size - 1:
                values_str += "\n"

        return values_str

    def generate_random_matrix(size: float) -> list:
        matrix = []
        for x in range(size * size):
            matrix.append(random.random())

        return matrix

    def generate_zero_matrix(size: float) -> list:
        matrix = []
        for x in range(size * size):
            matrix.append(0.0)

        return matrix
