import os
os.system("cls")

#Bloques de codigos reustilizables para hacer y tareas especificas
''' definicion de una funcion
utilizamos def para definirla seguido de el nombre en snake case
def funcion_ejemplo(parametro1, parametro2):
 # docstring
 # cuerpo de la funcion
 return valor_retorno # opcional

'''
def saludar():
    print("hola")

saludar()
# Ejemplo de una funcion con parametr0s
def saludo(nombre):
    print(f"hola bienvenido! {nombre}")
saludo("donovan")
saludo(" Frida")

def resta(a , b):
    return a - b

a = int(input("escribe un numero\n"))
b = int(input("escribe otro numero\n"))
print(resta(a, b))
# argumentos por posicion
def mis_datos(nombre, edad, sexo):
    print(f"Me llamo {nombre} tengo {edad} years y me indentifico como {sexo}")

mis_datos("donovsn", 25, "hombre")
#Argumentos por clave
mis_datos(edad=26, sexo="hombre", nombre="Donovan")

#Argumentos de longitud de variebales

def sumar_numeros(*args):
    suma=0
    for numeros in args:
        suma += numeros
    return suma
print(sumar_numeros(1,2,3,4,45,45,))