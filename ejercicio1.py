#Ejercicio 1: Operaciones Matemáticas con el Módulo math
#• Objetivo: Practicar con las funciones matemáticas básicas del
#módulo math.
#• Descripción: Utiliza las funciones del módulo math para realizar
#operaciones matemáticas avanzadas.
#• Instrucciones: Solicita al usuario que ingrese un número
#decimal.
#Usa las siguientes funciones del módulo math para realizar diferentes
#cálculos:
#✓ math.ceil(): Redondear al entero superior.
#✓ math.floor(): Redondear al entero inferior.
#✓ math.sqrt(): Obtener la raíz cuadrada.
#✓ math.factorial(): Calcular el factorial (solo si es un
#número entero no negativo).
#✓ math.pow(): Elevar el número a la potencia de otro
#número.

import math

numero=float(input("Por favor ingrese un numero: "))

redondear=math.ceil(numero)
print(f"Su numero decimal {numero}, a sido redondeado {redondear} al entero superior")

redondear_para_abajo=math.floor(numero)
print(f"Su numero {numero} a sido redondeado para abajo {redondear_para_abajo}") 

raiz_cuadrada= math.sqrt(numero)
print(f"La raíz cuadrada de {numero}, es {raiz_cuadrada}")

factor=math.factorial(redondear)
print(f"El factor de numero {redondear} es {factor}")

potencia=math.pow(numero,2)
print(f" El numero {numero}, elevado a una potencia es {potencia}")







