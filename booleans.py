


v = True
f = False

print(v)
print(f)

print(4 < 2)#esto es falso
print(5 > 4)# esto es verdadero

print(type(f))

# un booleano da true o false dependiendo el contenido
print(bool("hola mundo"))
print(bool(""))

# los siguientes caracteres texto numeros y listas son true
print(bool("abc"))
print(bool(123))
print(bool(["manzanas", "peras"]))

# los siguientes caracteres seran falsos

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

x = 123

print(isinstance(x, int))
print(isinstance(x, float))

y = 2.3

print(isinstance(y, float))