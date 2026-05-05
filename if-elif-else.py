x = 5
y = 4
z = 1

if x > y and y > z:# if es una condicional verdadera 
    print("x es mayor")

elif x == z:#elif es paraca cuando if no se cumple es como un if extra
    print("x igual a z")
else:# else es por si ninguna se cumple
    print("una de las condiciones es real")

# los if tambien sirven para comparar textos 

b = "carrosel"
n = "carro"
m = "carrosel"

if b > n:
   if b == m:
       print("b es igual que m")
   else:
       print("no es verdad")
print("b es mayor que n")

# si aun no sabes que hacer si el if es correctpo se usa pass

p = 10
g = 10

if g == p:
    pass
# ejemplo de condicionales
#saber si es mayor o menor de edad

edad = int(input("escribe tu edad "))
if edad >= 18:
    print("eres mayor de edad")
elif edad >=0:
    print("eres menor de edad")
else:
    print("dato invalido")
   




 