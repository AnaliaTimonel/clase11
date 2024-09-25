#Ejercicio 2: Generador de Números Aleatorios con el Módulo
#random
#• Objetivo: Trabajar con funciones de generación de números
#aleatorios del módulo random.
#• Descripción: Simula el lanzamiento de un dado y genera una
#lista de números aleatorios.
#• Instrucciones:
#✓ Simula el lanzamiento de un dado de 6 caras (números
#del 1 al 6) cinco veces.
#✓ Genera una lista de 10 números aleatorios entre 1 y 100.
#✓ Selecciona aleatoriamente un número de la lista
#generada.

import random

print("A jugar!!!")
puntos=[]
intentos=5


for intentos in range(1,7):

 lista=[1,2,3,4,5,6]
 asar=random.choice(lista)
 print("***************************")
 print("****Tira tu dado****")
 print("Sacaste el numero:", asar)
 puntos.append(asar)
 intentos-=1
 print("intentos:", intentos)
 print("***************************")


print("Sus puntos son:", sum(puntos))







