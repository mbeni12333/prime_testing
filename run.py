
from src.experiments import *

import numpy as np




##Question 1.c
#experience_gcd_inverse(30, 3)
#experience_gcd_inverse(3000, 300, inverse=False)

##Question 1.d
#experience_exp_mod(10000, 1000, n_exp=3)


##Question 2.a / b
experience_first_test(60, 6, n_exp=100)


##Question 2.c
#print("Nombre de nombres premier jusqu'a 1e5 compté via first_test:", experience_comptage_premier_naiif())

##Question 2.d
#experience_carmichael()