
name = input("escribe tu nombre\n")

print("hola", name, "bienvenido")

edad = int(input("escribe tu edad\n"))

if edad <= 2:
    print("eres un bebe")
elif edad >= 3 and edad <=12:
    print("eres un nino")
elif edad >= 13 and edad <= 17:
    print("eres un adolecente")
elif edad >= 18 and edad <= 30:
    print("eres un adulto")
elif edad >= 31:
    print("eres un adulto mayor")
else:
    print("no existes")


