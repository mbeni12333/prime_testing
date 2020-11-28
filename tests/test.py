import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from src.fonctions import *
from src.exercice3 import estimate_proba_test_fermat, test_fermat


class TestPGCD(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(my_gcd(987, 345), 3)
        self.assertEqual(my_gcd(345, 987), 3)
    def test_etendu(self):
        gcd, u, v = my_gcd_etendu(987, 345)
        self.assertEqual(u*987 + v*345, gcd)

class TestInverse(unittest.TestCase):
    def test_normal(self):
        inv = my_inverse(14, 11)
        self.assertEqual(inv*14%11, 1)
    def test_bezout(self):
        inv = my_inverse_bezout(14, 11)
        self.assertEqual(inv*14%11, 1)

class TestExpMod(unittest.TestCase):

    def test1(self):
        pythonResult = pow(2, 10, mod=67)
        ourResult = my_expo_mod(2, 10, 67)
        self.assertEqual(pythonResult, ourResult)

    def test2(self):
        pythonResult = pow(7892, 678, mod=79)
        ourResult = my_expo_mod(7892, 678, 79)
        self.assertEqual(pythonResult, ourResult)

class TestFermat(unittest.TestCase):


    def testGood(self):

        prime = 377791
        a = 253432

        goodResult = first_test(prime)
        ourResult = test_fermat(prime, a)
        self.assertEqual(goodResult, ourResult)


    def testFail(self):

        prime = 561
        a = 5

        goodResult = first_test(prime)
        ourResult = test_fermat(prime, a)
        self.assertEqual(goodResult, not ourResult)


if __name__ == '__main__':
    unittest.main()