'''
para imprimir texto entre comillas las comillas de afuera tienen
que ser diferentes a las comillasd de adentro ejemplo
'''
print('hola"mundo"')

ingles = "i'm donovan"
multiples = """hola
mundo"""

print(ingles)
print(multiples)
palara = "murcielago"
print(len(palara))# len sirve para saber cuantas letras tiene la palabra
 
texto = "este curso es de fundamentos de python"
estaIncluida = "python" in texto #in sirve para saber si hay algo en el texto
noEstaIncluida = "javascrit" not in  texto
print(estaIncluida)
print(noEstaIncluida)

mayuscula = texto.upper()

print(mayuscula)

minuscula = texto.lower()

print(minuscula)

espacios ="   esto   es el  texto"
sinEspacios = espacios.strip()

print(sinEspacios)

print(noEstaIncluida)

ten = "zoologico"
print(len(ten))