import unittest
from src.vector_space import ComplexVector

class TestComplexVector(unittest.TestCase):
    def test_initialization(self):
        v = ComplexVector([1, 2j])
        self.assertEqual(v.dimension, 2)
        self.assertEqual(v.coordinates, [1+0j, 0+2j])

    def test_addition(self):
        v1 = ComplexVector([1, 2])
        v2 = ComplexVector([3, 4])
        v3 = v1 + v2
        self.assertEqual(v3, ComplexVector([4, 6]))

    def test_scalar_multiplication(self):
        v = ComplexVector([1, -1])
        v2 = v * 2
        self.assertEqual(v2, ComplexVector([2, -2]))
        v3 = 3 * v
        self.assertEqual(v3, ComplexVector([3, -3]))

    def test_inner_product(self):
        v1 = ComplexVector([1j, 1])
        v2 = ComplexVector([1j, 1])
        # <v1, v2> = (1j)* * 1j + 1* * 1 = -1j * 1j + 1 = -(-1) + 1 = 1 + 1 = 2
        self.assertEqual(v1.inner_product(v2), 2)
    
    def test_norm(self):
        v = ComplexVector([3, 4j])
        # |v|^2 = 3*3 + (-4j)(4j) = 9 + 16 = 25
        self.assertEqual(v.norm(), 5.0)

    def test_dimension_mismatch(self):
        v1 = ComplexVector([1])
        v2 = ComplexVector([1, 2])
        with self.assertRaises(ValueError):
            v1 + v2

    def test_immutability(self):
        v = ComplexVector([1, 2])
        # Verify that coordinates are returned as a tuple (immutable)
        self.assertIsInstance(v.coordinates, tuple)
        # Verify that we cannot assign to elements of the coordinates
        with self.assertRaises(TypeError):
            v.coordinates[0] = 5

    def test_triangle_inequality(self):
        # |x + y| <= |x| + |y|
        v1 = ComplexVector([1+1j, 2])
        v2 = ComplexVector([3, 4j])
        norm_v1_plus_v2 = (v1 + v2).norm()
        norm_v1 = v1.norm()
        norm_v2 = v2.norm()
        self.assertLessEqual(norm_v1_plus_v2, norm_v1 + norm_v2 + 1e-9)

    def test_zero_vector_norm(self):
        # Norm = 0 if and only if vector = zero vector
        z = ComplexVector([0, 0])
        self.assertEqual(z.norm(), 0.0)
        
        non_zero = ComplexVector([1e-9, 0])
        self.assertGreater(non_zero.norm(), 0.0)

    def test_conjugate_symmetry(self):
        # <x,y> = conjugate(<y,x>)
        v1 = ComplexVector([1+2j, 3])
        v2 = ComplexVector([2-1j, 4])
        inner_12 = v1.inner_product(v2)
        inner_21 = v2.inner_product(v1)
        self.assertAlmostEqual(inner_12, inner_21.conjugate())

if __name__ == '__main__':
    unittest.main()
