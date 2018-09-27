import unittest
from matrix import Matrix

#https://github.com/ppaula/kol1_gr1

class test_matrix(unittest.TestCase):

    def test_dimention_return_correct_result(self):
        m = Matrix(1,1,1,1,1,1,1,1,1)
        self.assertEqual(3,m.dimention)

    def test_add_method_return_correct_result(self):
        m = Matrix(1,1,1,1)
        m2 = Matrix(2,2,2,2)
        ms = m.add(m2)
        my_matrix=Matrix(3,3,3,3)
        self.assertEqual(ms.__str__(),my_matrix.__str__())

    def test_add_method_raise_exception_incorrect_argument(self):
        m = Matrix(1,1,1,1)
        m2 = Matrix(1)
        with self.assertRaises(Exception):
            m.add(m2)

    def test_subtract_method_return_correct_result(self):
        m = Matrix(1,2,3,4)
        m2 = Matrix(2,2,2,2)
        ms = m.subtract(m2)
        my_matrix = Matrix(-1,0,1,2)
        self.assertEqual(ms.__str__(),my_matrix.__str__())

    def test_subtract_method_raise_exception_incorrect_argument(self):
        m = Matrix(1,2,3,4,5,6,7,8,9)
        m2 = Matrix(1,2,3,4)
        with self.assertRaises(Exception):
            m.subtract(m2)

    def test_dummy_multiply_method_return_correct_result(self):
        m = Matrix(0,0,0,1,1,1,-1,-1,-1)
        m2 = Matrix(-1,0,1,-1,0,1,-1,0,1)
        ms = m.dummy_multiply(m2)
        my_matrix = Matrix(0,0,0,-1,0,1,1,0,-1)
        self.assertEqual(ms.__str__(),my_matrix.__str__())

    def test_dummy_multiply_method_raise_exception_incorrect_argument(self):
        m = Matrix(0)
        m2 = Matrix(1,2,3,4)
        with self.assertRaises(Exception):
            m.dummy_multiply(m2)

    def test_multiply_method_return_correct_result(self):
        m = Matrix(1,2,3,4,5,6,7,8,9)
        m2 = Matrix(1,0,0,0,1,0,0,0,1)
        ms = m.multiply(m2)
        my_matrix = Matrix(1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0)
        self.assertEqual(ms.__str__(),my_matrix.__str__())

    def test_multiply_method_raise_exception_incorrect_argument(self):
        m = Matrix(1,2,3,4,5,6,7,8,9)
        m2 = Matrix(0,0,0,0)
        with self.assertRaises(Exception):
            m.multiply(m2)

    def test_add_one_method_return_correct_result(self):
        m = Matrix(1,1,1,1)
        m.add_one()
        my_matrix=Matrix(2,2,2,2)
        self.assertEqual(m.__str__(),my_matrix.__str__())

    #test returns error because method has got a bug 
    def test_subtract_one_method_return_correct_result(self):
        m = Matrix(-1,0,1,2)
        m.subtract_one()
        my_matrix = Matrix(-2,-1,0,1)
        self.assertEqual(m.__str__(),my_matrix.__str__())

    def test_double_matrix_method_return_correct_result(self):
        m = Matrix(-2,-1,0,1)
        m.double_matrix()
        my_matrix = Matrix(-4,-2,0,2)
        self.assertEqual(m.__str__(),my_matrix.__str__())

if __name__ == '__main__':
    unittest.main()