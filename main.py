import time # Importamos la librería time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random  # Importamos la librería random

puntaje = 0

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
puntaje = random.randint(0, 10)
despuntaje = random.randint(0, 5)
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (BLUE+"Bienvenido a mi trivia sobre computación"+RESET)
time.sleep(2)
print (BLUE+"Pondremos a prueba tus conocimientos"+RESET)
time.sleep(2)
print (GREEN+"Tienes", puntaje, "puntos"+RESET)
time.sleep(2)
nombre = input ("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
time.sleep(2)
print (BLUE+"\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
time.sleep(2)
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("Intento número:", intentos)
  input("\nPresiona Enter para continuar\n")

  print("Primera pregunta...\n")
  time.sleep(2)
  print (YELLOW+"1) ¿Quién fue el personaje biblico que traiciono a Jesus?"+RESET)
  time.sleep(3)
  print ("a) Satanas")
  time.sleep(1)
  print ("b) Pedro")
  time.sleep(1)
  print ("c) Judas")
  time.sleep(1)
  print ("d) Chabelo")
  time.sleep(1)
  respuesta_1 = input(CYAN+"\nTu respuesta: "+RESET)
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if(respuesta_1 == "c" or respuesta_1 == "C"):
    puntaje += 10
    time.sleep(2)
    print(GREEN+"\nCorrecto   :)\n"+RESET)
    print(nombre, "llevas", puntaje, "puntos")
  else:
    puntaje -= despuntaje
    time.sleep(2)
    print(RED+"\nIncorrecto   :( \n"+RESET)
    print("Puntaje actual : ",puntaje)
    time.sleep(2)
  print (YELLOW+"\n2) ¿Quién fue el personaje biblico que escribio el libro de Apocalipsis?"+RESET)
  time.sleep(3)
  print ("a) Juan")
  time.sleep(1)
  print ("b) Adan")
  time.sleep(1)
  print ("c) Mateo")
  time.sleep(1)
  print ("d) Pablo")
  time.sleep(1)
  respuesta_2 = input(CYAN+"\nTu respuesta: "+RESET)
  while respuesta_2 not in ("a", "b", "c", "d","x"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "x":
    print("Esto es un mensaje secreto")
  if respuesta_2 == "b":
    puntaje -= despuntaje
    time.sleep(2)
    print(RED+"\nIncorrecto!", nombre, "Adan ya no existia en ese tiempo \n"+RESET)
    print("\nPuntaje actual : ",puntaje)
    time.sleep(2)
  elif respuesta_2 == "c":
    puntaje -= despuntaje
    time.sleep(2)
    print(RED+"Incorrecto!", nombre, "Mateo ya no existia en ese tiempo"+RESET)
    print("Puntaje actual : ",puntaje)
    time.sleep(2)
  elif respuesta_2 == "d":
    puntaje -= despuntaje
    time.sleep(2)
    print(RED+"Incorrecto!", nombre, "Pablo ya no existia en ese tiempo"+RESET)
    print("Puntaje actual : ",puntaje)
    time.sleep(2)
  else:
    puntaje += 10
    time.sleep(2)
    print(GREEN+"\nCorrecto   :)\n"+RESET)
    print(nombre, "llevas", puntaje, "puntos\n")
    time.sleep(2)
            
  print (YELLOW+"1) ¿Cual fue el dia en que resucito Jesus ?"+RESET)
  time.sleep(3)
  print ("a) Martes")
  time.sleep(1)
  print ("b) Viernes")
  time.sleep(1)
  print ("c) Sabado")
  time.sleep(1)
  print ("d) Domingo")
  time.sleep(1)
  respuesta_3 = input(CYAN+"\nTu respuesta: "+RESET)
  while respuesta_3 not in ("a", "b", "c", "d","y"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "y":
    print("Esto es un mensaje secreto 2.0")
  if respuesta_3 == "a":
    time.sleep(2)
    print(RED+"\nTotalmente incorrecto! ...", nombre, "martes no es "+RESET)
    puntaje = puntaje / 2
    time.sleep(2)
  elif respuesta_3 == "b":
    print ("...")
    time.sleep(2)
    print(RED+"\nIncorrecto!", nombre, "viernes no es"+RESET)
    puntaje = puntaje + 5
    time.sleep(2)
  elif respuesta_3 == "c":
    time.sleep(2)
    print(RED+"\nIncorrecto! ...", nombre, "Sabado no es"+RESET)
    puntaje = puntaje - 5
    time.sleep(2)
  else:
    time.sleep(2)
    print(GREEN+"\nCorrecto! ...", nombre, "!"+RESET)
    puntaje = puntaje * 2
    time.sleep(2)
    print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  # != significa "distinto"
    print("\nEspero ",nombre, "que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.