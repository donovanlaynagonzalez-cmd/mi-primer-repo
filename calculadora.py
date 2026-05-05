import os
os.system("cls")

import random
numeros =[ 1, 2, 3]
print("adivina el numero")
computadora = random.choice(numeros)
numero = int(input("ingresa un numero de el 1 al 3\n"))

while numero == computadora:
    print("ganaste")
    print ( computadora, numero)
    break
else:
    print("perdiste")
    print(computadora, numero)


