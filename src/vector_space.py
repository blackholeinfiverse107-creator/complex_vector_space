from typing import List, Union
import math
import cmath

class ComplexVector:
    def __init__(self, coordinates: List[complex]):
        self._coordinates = tuple(complex(c) for c in coordinates)
        self._dimension = len(coordinates)

    @property
    def coordinates(self) -> tuple:
        return self._coordinates

    @property
    def dimension(self) -> int:
        return self._dimension

    def __add__(self, other: 'ComplexVector') -> 'ComplexVector':
        if not isinstance(other, ComplexVector):
            return NotImplemented
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for addition.")
        
        return ComplexVector([c1 + c2 for c1, c2 in zip(self.coordinates, other.coordinates)])

    def __mul__(self, scalar: Union[int, float, complex]) -> 'ComplexVector':
        if not isinstance(scalar, (int, float, complex)):
            return NotImplemented
        return ComplexVector([c * scalar for c in self.coordinates])

    def __rmul__(self, scalar: Union[int, float, complex]) -> 'ComplexVector':
        return self.__mul__(scalar)

    def __neg__(self) -> 'ComplexVector':
        return self * -1

    def __sub__(self, other: 'ComplexVector') -> 'ComplexVector':
        return self + (-other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexVector):
            return NotImplemented
        return self.coordinates == other.coordinates

    def __repr__(self) -> str:
        return f"ComplexVector({self.coordinates})"

    def inner_product(self, other: 'ComplexVector') -> complex:
        if not isinstance(other, ComplexVector):
            raise TypeError("Argument must be a ComplexVector.")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for inner product.")
        
        # Conjugate linear in the first argument (physics convention)
        return sum(c1.conjugate() * c2 for c1, c2 in zip(self.coordinates, other.coordinates))


    def norm(self) -> float:
        return math.sqrt(self.inner_product(self).real)


class LinearOperator:
    def __init__(self, matrix: List[List[complex]]):
        """
        Initialize with a matrix representation.
        matrix[i][j] is the element at row i, column j.
        """
        self._matrix = [[complex(c) for c in row] for row in matrix]
        self._rows = len(matrix)
        self._cols = len(matrix[0]) if self._rows > 0 else 0
        
        # Verify matrix is rectangular
        if not all(len(row) == self._cols for row in matrix):
            raise ValueError("Matrix must be rectangular.")

    @property
    def matrix(self) -> List[List[complex]]:
        return self._matrix

    @property
    def input_dim(self) -> int:
        return self._cols

    @property
    def output_dim(self) -> int:
        return self._rows

    def __call__(self, vector: ComplexVector) -> ComplexVector:
        if not isinstance(vector, ComplexVector):
            raise TypeError("Argument must be a ComplexVector.")
        if vector.dimension != self.input_dim:
            raise ValueError(f"Dimension mismatch: Operator expects input dimension {self.input_dim}, got {vector.dimension}.")
        
        result_coords = []
        for i in range(self.output_dim):
            val = sum(self.matrix[i][j] * vector.coordinates[j] for j in range(self.input_dim))
            result_coords.append(val)
        
        return ComplexVector(result_coords)

    def __matmul__(self, other: 'LinearOperator') -> 'LinearOperator':
        if not isinstance(other, LinearOperator):
            return NotImplemented
        if self.input_dim != other.output_dim:
            raise ValueError(f"Dimension mismatch: Cannot compose operator with input dim {self.input_dim} and operator with output dim {other.output_dim}.")
        
        new_matrix = []
        for i in range(self.output_dim):
            row = []
            for j in range(other.input_dim):
                val = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.input_dim))
                row.append(val)
            new_matrix.append(row)
            
        return LinearOperator(new_matrix)

    def adjoint(self) -> 'LinearOperator':
        # Transpose and conjugate
        new_matrix = [[self.matrix[j][i].conjugate() for j in range(self.output_dim)] for i in range(self.input_dim)]
        return LinearOperator(new_matrix)

    def __repr__(self) -> str:
        return f"LinearOperator(dims={self.output_dim}x{self.input_dim})"
