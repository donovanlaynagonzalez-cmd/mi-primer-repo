
import os
os.system("cls")

#Ejercicios de listas
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
lista1.insert(1, 10)
lista1.insert(0, 0)
print(lista1)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
eliminado = lista_a.pop(3)
print(lista_a)
print(eliminado)
lista_a.clear()
print(lista_a)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista2[2:3]
del lista2[5]
print(lista2)
