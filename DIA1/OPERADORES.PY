#todo operadores matematicos
"""
Operadores de suma, resta, multiplicación y división:
Suma: +
Ejemplo: a + b

Resta: -
Ejemplo: a - b

Multiplicación: *
Ejemplo: a * b

División: /
Ejemplo: a / b

División entera: //
Ejemplo: a // b (Devuelve el cociente entero de la división)

Módulo: %
Ejemplo: a % b (Devuelve el residuo de la división)

num = int(input("ingrese un numero:"))
par = num % 2
if par == 0:
    print("El Numero es Par")
else:    
    print("El Numero es ImPar")

Exponente: **
Ejemplo: a ** b (Calcula a elevado a la potencia b)

base = 2
exponente =3
resultado = base ** 3
print(f"{base} elevado al {exponente} es igual al {resultado}")
"""

#todo operadores logicos
"""
Operadores de comparación:
Igualdad: ==
Desigualdad: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=

Operadores lógicos:
and: Devuelve True si ambas expresiones son verdaderas.
or: Devuelve True si al menos una de las expresiones es verdadera.
not: Niega la expresión booleana; devuelve False si la expresión es verdadera y viceversa.
"""


variable=True
resultado = not variable #false
print(f"la variable es {variable}")
print(f"la negacion de la variable {resultado}")