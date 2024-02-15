class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def get_num_rows(self):
        return self.rows

    def get_num_cols(self):
        return self.cols

    def set_element(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value
        else:
            print("Invalid position for setting element")

    def add(self, other):
        if self.rows != other.get_num_rows() or self.cols != other.get_num_cols():
            print("Matrices cannot be added")
            return None

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def multiply(self, other):
        if self.cols != other.get_num_rows():
            print("Matrices cannot be multiplied")
            return None

        result = Matrix(self.rows, other.get_num_cols())
        for i in range(self.rows):
            for j in range(other.get_num_cols()):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

# Example usage:
# Create two matrices
matrix1 = Matrix(2, 3)
matrix2 = Matrix(2, 3)

# Set elements of matrix1
matrix1.set_element(0, 0, 1)
matrix1.set_element(0, 1, 2)
matrix1.set_element(0, 2, 3)
matrix1.set_element(1, 0, 4)
matrix1.set_element(1, 1, 5)
matrix1.set_element(1, 2, 6)

# Set elements of matrix2
matrix2.set_element(0, 0, 7)
matrix2.set_element(0, 1, 8)
matrix2.set_element(0, 2, 9)
matrix2.set_element(1, 0, 10)
matrix2.set_element(1, 1, 11)
matrix2.set_element(1, 2, 12)

# Add matrices
result_addition = matrix1 + matrix2
if result_addition:
    print("Addition Result:")
    for row in result_addition.matrix:
        print(row)

# Multiply matrices
result_multiplication = matrix1 * matrix2
if result_multiplication:
    print("Multiplication Result:")
    for row in result_multiplication.matrix:
        print(row)
