
from src.experiments import *
from src.fonctions import *


import numpy as np




##Question 1.c
def q1c():
	experience_gcd_inverse(30, 3)
	experience_gcd_inverse(3000, 300, inverse=False)

##Question 1.d
def q1d():
	experience_exp_mod(10000, 1000, n_exp=3)


##Question 2.a / b
def q2ab():
	experience_first_test(60, 6, n_exp=100)


##Question 2.c
def q2c():
	print("Nombre de nombres premier jusqu'a 1e5 compté via first_test:", experience_comptage_premier_naiif())

##Question 2.d
def q2d():
	experience_carmichael(500000)

##Question 2.e
def q2e():
	print(gen_carmichael3(1e4))
	#187054437571
	#266724927361
	#3610008963601

##Question 2.f
def q2f():
	experience_carmichael_t()

##Question 2.f avec 3
def q2f2():
	experience_carmichael3_t()

##Question 3.b / c
def q3bc():
	estimate_proba_test_fermat(50000, 100000, mode=0)

def q4b():
	estimate_proba_test_rabin(10000, maxSize=1000000)

def q4c():
	experience_miller_rabin()


menu = [("Question 1.c", q1c),
		("Question 1.d", q1d),
		("Question 2.a / 2.b", q2ab),
		("Question 2.c", q2c),
		("Question 2.d", q2d),
		("Question 2.e", q2e),
		("Question 2.f avec carmichael classique", q2f),
		("Question 2.f avec carmichael3", q2f2),
		("Question 3.b / 3.c", q3bc),
		("Question 4.b", q4b),
		("Question 4.c", q4c)]




###Menu
while True:

	print("-1: Stop")

	for i, (name, _) in enumerate(menu):
		print(f"{i}: {name}")

	print("Please enter your choice: ", end='')

	selected = input()

	try:
		selected = int(selected)

	except ValueError:
		print(f"{selected} is not a number.")
		continue


	if selected == -1:
		break

	else:

		if selected < 0 or selected >= len(menu):
			print(f"{selected} is an invalid choice.")
			continue

		menu[selected][1]()

