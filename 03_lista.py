
import os
os.system("cls")
lista = [1, 2, 3, 4, 5]
 # para anadir elementos se utilixa el .append
lista.append(6)
print(lista)
# para incertar un numero en la lista usamos .insert
lista.insert(1, 2.5)# primero la posisicon una coma y despues lo que se quiere incertar
print(lista)
# para anadir datos al final de la lista se puede usar el .extend 
lista.extend([7, 8])# se usan parentecis y corchetes 
print(lista) # para incertar al final puedes utilizar +, += o .extend

# ahora metodos para eliminar elementos de listas
# para eliminar un elemento utilizamos el .remove ()
lista.remove(2.5)
print(lista)# solo remueve el primer elemento no todos lo de la lista

# para eliminar elemento pero desde su indice se utiliza el .pop
lista.pop()# si no introduces un indice se elimina el ultimo de la lista
print( lista)
eliminado = lista.pop(5)# el pop tambien te devuelve el elemento bprrado en una bariable
print(lista)

# otra forma de eliminar un elelemto es con "del" al principio
del lista[-1]# se puede utilizar cualquier indice 
print(lista)
# para eliminar toda la lista se puede utilizar clear
lista.clear()
print(lista)

#para borrar un grupo de elemento se utiliza del lista[:]
lista = [1, 2, 3, 4, 5]
del lista[1:3]
print(lista)

# ahora para odenar listas se utiliza . sort
numbers = [3, 5, 1, 8, 9, 6]
numbers.sort()# el sort no guarda la lista original la tranforma 
print(numbers)

# si queremos que nos devuelva la lista una copia se utiliza
#sorted de la siguente manera

numbers = [3, 5, 1, 8, 9, 6]
number_ordenet = sorted(numbers)#guarda la lista ordenada en una bariable sin modificar la lista original
print(number_ordenet) 
print(numbers)

#Tambien se pueden ordenar palabras pero sin hay mayuscuas utilizamos lo siguiente
frutas = ["pera", "Manzana", "sandia", "Rabano", "frijoles", "Frijoles"]
# si sorteamos asi no respetara el orden por que sortera primero las mayusculas
frutas_ordenada = sorted(frutas)
print(frutas_ordenada)
# para que se sorteen sin inportar las mayusclas usamos .lower
# pero para esto utilizamos sort y la llave"key"de la siguiente manera

frutas.sort(key=str.lower)
print(frutas)
 # para contar en listas esta el len
print(len(frutas))
#para contar cauntas veces aparece un elemento en la lista utilizamos .count
print(frutas.count("frijoles"))

#para saber si hay un elemento en la lista se utiliza el in 
print("frijoles" in frutas)






