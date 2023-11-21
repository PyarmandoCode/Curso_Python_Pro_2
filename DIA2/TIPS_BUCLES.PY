nombres = ["Ana", "Carlos", "Eva"]
edades = [30, 25, 28]

"""
zip() permite iterar simultáneamente sobre múltiples listas y combinar sus elementos.

numeros =[5,2,7,1,9]
for nombre,edad in zip(nombres,edades):
    print(f"{nombre} tiene {edad} años")
"""


"""
sorted() itera sobre una secuencia ordenada.
numeros =[5,2,7,1,9]
for numero in sorted(numeros):
    print(numero)
"""    


"""
Comprensiones de Listas
1.-Imprime los cuadros que existen hasta el numero6

cuadrados = [i ** 2 for i in range (1,6)]
print(cuadrados)

2.-Filtrar elementos pares de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

3.-Convertir todos los elementos de una lista a Mayuscula
"""    
# for num in range(1,6):
#     cuadrado = num ** 2
#     print(cuadrado)


frutas = ["manzana", "banana", "naranja", "kiwi"]
mayusculas = [fruta.upper() for fruta in frutas]
print(mayusculas)