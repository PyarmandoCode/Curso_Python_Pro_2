
import random


"""

EJEMPLO CON EL MODULO RANDOM

Crear un script que me permita adivinar la fruta
elegida por el sistema

frutas = ["manzana","pera","melocoton","durazno"]
num_azar= random.random()
num_azar= random.randrange(10,100)
fruta_azar =random.choice(frutas)
#print(f"El Numero Aleatorio generado es {num_azar}")
#print(f"La Fruta al Azar es {fruta_azar}")

while True:
    fruta_usuario=input("Ingrese la Fruta:")
    if fruta_usuario==fruta_azar:
        print("Acertastes la Fruta")
        break
    else:
        print("No Acertastes")    

"""

"""
EJEMPLO CON EL MODULO DATETIME

import datetime as trabajo_fechas #modulo o paquete desde el nucleo de python
#obtener la fecha y la hora actual
fecha_actual= trabajo_fechas.datetime.now()
#formatear fechas
fecha_formateada=fecha_actual.strftime("%d/%m/%Y")
#23print(f"la fecha y hora actual del sistema es {fecha_formateada}")
#extrayendo informacion
año=fecha_actual.year
mes=fecha_actual.month
dia=fecha_actual.day
# print(f"el Año actual es {año}")
# print(f"el mes actual es {mes}")
# print(f"el Dia actual es {dia}")


Crear un Script que me permita hallar la diferencia de dias que hay entre dos fechas 


fecha1 = trabajo_fechas.datetime(2023, 11, 23)
fecha2 = trabajo_fechas.datetime(2023, 12, 24)
diferencia = fecha2 - fecha1
print(f"Diferencia entre dias {diferencia.days}")


"""

"""
EJEMPLO CON EL MODULO MATH

import math as mis_matematicas
print(f" El Valor de PI es  {mis_matematicas.pi}")
print(f" La Raiz Cuadrada de n  {mis_matematicas.sqrt(5)}")
print(f" Logaritmo en Base 10 de 100 {mis_matematicas.log10(100)}")


Calcular el seno de un angulo en radianes

angulo=mis_matematicas.radians(45) #Convertir 45 grados a radianes
seno = mis_matematicas.sin(angulo)
print(f"El Seno de 45 Grados {seno} ")

"""

"""
EJEMPLO CON EL MODULO STATISTICS


import statistics as mis_estadisticas

datos = [10, 15, 20, 25, 30]

#Calcular la media
media = mis_estadisticas.mean(datos)
print(f"la Media es {media}")

#Calcular la mediana
mediana=mis_estadisticas.median(datos)
print(f"la Mediana es {mediana}")

#Calcular la Moda
datos = [1, 2, 2, 3, 4, 5, 5, 5, 6]
moda =mis_estadisticas.mode(datos)
print(f"la Moda es {moda}")

"""

