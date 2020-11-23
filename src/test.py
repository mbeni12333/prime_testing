
from fonctions import my_gcd, my_expo_mod

"""
Le pgcd de 987 et 345 est 3 :
"""
print("Pgcd de 987 et 345:", my_gcd(987, 345))


"""
2^10 modulo 67 vaut 19
"""

print("\n2^10 modulo 67:")
print("Avec pow de python:", pow(2, 10, mod=67))
print("Avec my_expo_mod:", my_expo_mod(2, 10, 67))


print("\n7892^678 modulo 79:")
print("Avec pow de python:", pow(7892, 678, mod=79))
print("Avec my_expo_mod:", my_expo_mod(7892, 678, 79))