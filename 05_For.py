import os
os.system("cls")


contador = 10
while contador > 0:
    print(contador)
    contador -= 1

suma = 0
contador = 1

while contador <20:
    if contador % 2 == 0:
        suma += contador
    contador += 1

print(f"suma es igaul a: {suma}")

numero = int(input("Ingresa un número: "))
factorial = 1

while numero > 0:
    factorial *= numero
    numero -= 1

print("El factorial es:", factorial)

contrasena_correcta = 1234
contrasena = ""

while contrasena != contrasena_correcta:
    contrasena = input("escribe la contrasena\n")

print("contrasena correcta")



    
    
    