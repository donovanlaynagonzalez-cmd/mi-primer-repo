import os
os.system("cls")

frutas = ["manzana", "pera", "sandia"]

for frutas in frutas:
    print(frutas)

# con el fro podemos iterar casi todo hasta las letras de una palabra

name = "Donovan"

for caracter in name:
    print(caracter)

# para saber el indice de cada fruta utilizamos index,   y enumerate de la siguiente manera

frutas = ["manzana", "pera", "sandia"]

for index,fruta in enumerate(frutas):
    print(f"el indice de es {index} y la fruta es {fruta}")

letras = ["a", "b", "c"]
numeros = [ 1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{numero}{letra}")

animales = ["perro", "loro", "gato", "elefante", "leon"]

for index,animal in enumerate(animales):
        print(f"el numero {index} y el animal es {animal}" )
        if animal == "loro":
             print(f"el loro esta econdido en el indice {index}")
             break
        

# comprecion de listas

frutas = ["fresa", "limon", "pera", "naranja"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

numer = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [num for num in numer if num % 2 == 0]
print(pares)
        
        
       