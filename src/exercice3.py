
from fonctions import my_expo_mod, first_test, gen_carmichael
import random




"""
n un entier impair, a un entier entre 2 et n - 1.

Retourne vrai si premier possible
faux si composé

"""
def test_fermat(n, a):

	b = pow(a, n-1, n)

	if b != 1:
		return False

	return True


def generateRandomComposite(maxSize=100000):

	notPrime = random.randrange(4, maxSize)

	while first_test(notPrime):
		notPrime = random.randrange(4, maxSize)

	return notPrime


"""

Entrées:
	n : Nombre de test
	maxSize : Taille maximum des valeurs testés
	mode:
		0 = Nombre généré par gen_carmichael
		1 = Nombre composé
		2 = Aléatoire

	Ne retourne rien mais print la probabilité de succes estimé.
"""
def estimate_proba_test_fermat(n, maxSize=100000, mode=0):

	error_counter = 0
		
	for i in range(n):

		if mode == 0:
			prime = gen_carmichael()
			a 	  = random.randrange(1, prime)

			#Random a ou bien un autre nombre de carmichael ?


		elif mode == 1:
			prime = generateRandomComposite(maxSize)
			a 	  = random.randrange(1, prime)

			#Si celle là, que faire dans le cas de prime = 4 ?
			#a 	  = generateRandomComposite(prime)
			

		elif mode == 2:
			#n impair et supérieur a 2
			prime = random.randrange(3, maxSize, 2)
			a 	  = random.randrange(1, prime)

		mayPrime = test_fermat(prime, a)

		isPrime  = first_test(prime)

		if mayPrime != isPrime:
			#print(f"Error on {prime} with a = {a}")
			error_counter += 1


	error_pourcent = error_counter/n

	print(f"{error_counter} erreurs rencontrées sur {n} valeurs, soit une probabilité d'erreur de {round(error_pourcent*100, 3)}% ({round(error_pourcent, 6)})")
