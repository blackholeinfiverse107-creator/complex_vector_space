import unittest
from src.vector_space import ComplexVector, LinearOperator

class TestLinearOperator(unittest.TestCase):
    def test_initialization(self):
        m = [[1, 2j], [3, 4]]
        op = LinearOperator(m)
        self.assertEqual(op.input_dim, 2)
        self.assertEqual(op.output_dim, 2)
        self.assertEqual(op.matrix, [[1+0j, 0+2j], [3+0j, 4+0j]])

    def test_application(self):
        op = LinearOperator([[1, 0], [0, 1j]]) # Identity-like
        v = ComplexVector([1, 1])
        result = op(v)
        self.assertEqual(result, ComplexVector([1, 1j]))

    def test_composition(self):
        op1 = LinearOperator([[0, 1], [1, 0]]) # Swap
        op2 = LinearOperator([[1, 0], [0, -1]]) # Z-like
        # op1 @ op2 = [[0, -1], [1, 0]]
        op3 = op1 @ op2
        v = ComplexVector([1, 1]) 
        # op2(v) = [1, -1]
        # op1([1, -1]) = [-1, 1]
        self.assertEqual(op3(v), ComplexVector([-1, 1]))

    def test_adjoint(self):
        op = LinearOperator([[1, 2j], [3, 4]])
        adj = op.adjoint()
        # Transpose conjugate: [[1, 3], [-2j, 4]]
        self.assertEqual(adj.matrix, [[1, 3], [-2j, 4]])

    def test_dimension_mismatch(self):
        op = LinearOperator([[1, 2], [3, 4]])
        v = ComplexVector([1])
        with self.assertRaises(ValueError):
            op(v)

if __name__ == '__main__':
    unittest.main()
