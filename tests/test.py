import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from src.fonctions import *


"""
Le pgcd de 987 et 345 est 3 :
"""
# print("Pgcd de 987 et 345:", my_gcd(987, 345))


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

if __name__ == '__main__':
    unittest.main()