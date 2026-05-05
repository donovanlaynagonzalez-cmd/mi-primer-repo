import os
os.system("cls")


contador = 0
while contador <=5:
    print(contador)
    contador += 1
print("bucles")
contador = 0
while  True:
    print(contador)
    contador += 1
    if contador == 10:
        break
print("bucles")   

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue
    print(contador)

    # else en bucles 

contador = 0
while contador <5:
    print(contador)
    contador += 1
else:
    print("bucle trminado")

#Pedir al usuario un numero 

numero = -1
while numero <0:
    numero = int(input("escribe un numero positivo\n"))
    if numero < 0:
        print("el numero tiene que ser mayor que 0")

print(f"el numero que escribiste es: {numero}")
    
       
    
