# rangos
import os
os.system("cls")

nums = range(5)# no es una lista
print(nums)
for ran in range(10):
    print(ran, end=" " )

for num in range(5, 0, -1):
    print(num)

lista = range(10)
list_ran = list(lista)
print(list_ran)

for _ in range(5):
    print("hacer 5 veces algo")# el _ es una variable que no se va utilizar

# ejercicios de rangos

for numss in range(11):
    print( numss, end=" ")
print("numero pares")
for no in range(21):
    if no % 2 == 0:
        print(no)

suma = 0
for mult in range(101):
    if mult:
        suma += mult
print(suma)
