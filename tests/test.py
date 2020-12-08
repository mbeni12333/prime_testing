import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from src.fonctions import *


class TestPGCD(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(my_gcd(987, 345), 3)
        self.assertEqual(my_gcd(345, 987), 3)

    def test_etendu(self):
        gcd, u, v = my_gcd_etendu(987, 345)
        self.assertEqual(u*987 + v*345, gcd)
        gcd, u, v = my_gcd_etendu(345, 987)
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


class TestExponent(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(my_expo_mod(5, 23, 77), pow(5, 23, mod=77))

class TestCarmicael(unittest.TestCase):
    def test_isCarmicael_facteurs(self):
        self.assertTrue(isCarmichael_facteurs(561, [3, 11, 17]))
        self.assertFalse(isCarmichael_facteurs(231, [3, 7, 11]))
        self.assertTrue(216821881, [331, 661, 991])

    def test_isCarmicael(self):
        self.assertTrue(isCarmichael(561))
        self.assertFalse(isCarmichael(231))
        self.assertTrue(216821881)

class TestRSA(unittest.TestCase):
    def testGenRsa(self):
        p, q, n = gen_rsa(3)
        self.assertTrue(test_miller_rabin(p))
        self.assertTrue(test_miller_rabin(q))
        p, q, n = gen_rsa(4)
        self.assertTrue(test_miller_rabin(p))
        self.assertTrue(test_miller_rabin(q))
        p, q, n = gen_rsa(10)
        self.assertTrue(test_miller_rabin(p))
        self.assertTrue(test_miller_rabin(q))

if __name__ == '__main__':
    unittest.main()