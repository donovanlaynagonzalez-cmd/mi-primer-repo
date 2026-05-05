import os
os.system("cls")

for num in range (1, 20):
    if num % 2 == 0:
        print(num)
num += 1

# calcula la media de los siguientes numero

numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num

media = suma / len(numeros)
print(f"la media de los numeros es {media}")

# encontrar el nmero mayor
numeros = [ 4, 6, 27 , 3, 11]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print(f"el numero mayor es {mayor}")

lista = ["ferrocarril", "ssopreno", "cel", "vici", "pancrias"]

for mas5 in lista:
    if len(mas5) >= 5:
         print(mas5)
