
import math

from fonctions import my_gcd, my_expo_mod

###TEST my_gcd
print("Pgcd de 987 et 345:")
print("Avec math.gcd:", math.gcd(987, 345))
print("Avec my_gcd:", my_gcd(987, 345))

print("\nPgcd de 746280942 et 192900103:")
print("Avec math.gcd:", math.gcd(746280942, 192900103))
print("Avec my_gcd:", my_gcd(746280942, 192900103))


###TEST my_expo_mod
print("\n2^10 modulo 67:")
print("Avec pow de python:", pow(2, 10, mod=67))
print("Avec my_expo_mod:", my_expo_mod(2, 10, 67))


print("\n7892^678 modulo 79:")
print("Avec pow de python:", pow(7892, 678, mod=79))
print("Avec my_expo_mod:", my_expo_mod(7892, 678, 79))