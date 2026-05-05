
import random


opciones = ["piedra", "papel", "tijera"]
print("bienvenido al juego piedra, papel o tijera\n")


jugador = input("elige piedra, papel o tijera\n").lower()
if jugador not in opciones:
     print("Error")
     quit()
computador = random.choice(opciones)

if computador == jugador:
     print("juego enpatado")
     
elif jugador == "tijera" and computador == "piedra" or jugador == "piedra" and computador == "papel" or jugador == "papel" and computador == "tijeras":
     print("has perdido")

elif jugador == "tijera" and computador == "papel" or \
jugador == "papel" and computador == "piedra" or \
jugador == "piedra" and computador == "tijeras":
     print("has ganado el juego")


        
   
      




    
