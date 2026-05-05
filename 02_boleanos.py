import os
os.system("cls")
num1 = int(input("escribe el primer numero\n"))
num2 = int(input("escribe el segundo numero\n"))
operacion = input("escribe la operacion")

if operacion == "*":
    print(num1 * num2)
elif operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)

