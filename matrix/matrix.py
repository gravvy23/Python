import numpy as np

class Matrix:

	dimention = 0
	matrix = list()

	def __init__(self, *matrix_elements):
		self.dimention = int(len(matrix_elements) ** (1/2))
		self.matrix = [[0 for x in range(self.dimention)] for y in range(self.dimention)] 
		for x in range(0, self.dimention):
			for y in range(0, self.dimention):
				self.matrix[x][y] = matrix_elements[x*self.dimention + y]

	def __str__(self):
		return str(self.matrix)

	def add(self, matrix_to_add):
		if self.dimention == matrix_to_add.dimention:
			matrix_to_return = list()
			for x in range(0, self.dimention):
				for y in range(0, self.dimention):
					matrix_to_return.append(self.matrix[x][y] + matrix_to_add.matrix[x][y])
			return Matrix(*matrix_to_return)
		else:
			raise Exception('Inconsistent agrument!')

	def subtract(self, matrix_to_subtract):
		if self.dimention == matrix_to_subtract.dimention:
			matrix_to_return = list()
			for x in range(0, self.dimention):
				for y in range(0, self.dimention):
					matrix_to_return.append(self.matrix[x][y] - matrix_to_subtract.matrix[x][y])
			return Matrix(*matrix_to_return)
		else:
			raise Exception('Inconsistent agrument!')

	def dummy_multiply(self, matrix_to_multiply):
		if self.dimention == matrix_to_multiply.dimention:
			matrix_to_return = list()
			for x in range(0, self.dimention):
				for y in range(0, self.dimention):
					matrix_to_return.append(self.matrix[x][y] * matrix_to_multiply.matrix[x][y])
			return Matrix(*matrix_to_return)
		else:
			raise Exception('Inconsistent agrument!')

	def multiply(self, matrix_to_multiply):
		if self.dimention == matrix_to_multiply.dimention:
			matrix_to_return = np.zeros(self.dimention ** 2,)
			for x in range(0, self.dimention):
				for y in range(0, self.dimention):
					for z in range(0, self.dimention):
							matrix_to_return[x*self.dimention + y] += self.matrix[x][z] * matrix_to_multiply.matrix[z][y]
			return Matrix(*matrix_to_return)
		else:
			raise Exception('Inconsistent agrument!')
	
	def add_one(self):
		for x in range(0, self.dimention):
			for y in range(0, self.dimention):
				self.matrix[x][y] += 1
	
	def subtract_one(self):
		for x in range(0, self.dimention):
			for y in range(0, self.dimention):
				self.matrix[x][y] = 1 - self.matrix[x][y]
	
	def double_matrix(self):
		for x in range(0, self.dimention):
			for y in range(0, self.dimention):
				self.matrix[x][y] += self.matrix[x][y]


