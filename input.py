nombre = input("hola como te llamas?\n")
print(F"hola {nombre} encantado de conocerte")

age = int(input("cuantos ages tienes?\n"))
print(F"dentro de 20 ages tendras {age + 20}")

print("obtener multiples valores a la vez")
country, city = input("en que pais y ciudad vives?\n").split()

print(F"vives en { country}, {city}")