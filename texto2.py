# ind   0123456789
texto ="esto es un texto"

print(texto[0:13])
#si se quiere imprimir desde el inicio no se pone numero ejemplo
print(texto[:16])
# si se quiere de enmedio al final se omite en segundi numero ejemplo
print(texto[5:])

curso = "este curso es de javascrip"
# para remplazar palabras usamos replace 
print(curso.replace("javascrip", "python"))

textoDividido = texto.split(" ")
print(textoDividido)

#normalizacion 
texto2 = "este texto tiene mayusculas y minusculas y necesito encontrar ciertas palabras" 
print("mayusculas".lower() in texto2.lower())
