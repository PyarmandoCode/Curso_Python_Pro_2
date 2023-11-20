"""
INDENTACION
A los espacios o Tabulaciuones que se utilizan al 
escribir codigo para estructurar y delimitar bloques
de codigo.
es fundamental y se usa para definir la estructura y jeraquia dentro del codigo
"""

# edad = int(input("Ingrese la edad:"))
# if edad <18:
#     print("la persona es menor de edad")
# elif edad==18:
#     print("la persona tiene 18 años")
# else:
#     print("la persona es mayor edad")    
    

edad = 25
ciudad = "New York"

if edad > 18 and ciudad == "New York":
    print("Eres mayor de edad y vives en New York.")
else:
    print("No cumples con las condiciones.")


nombre = "Alice"
ciudad = "San Francisco"

if nombre == "Alice" or ciudad == "New York":
    print("Eres Alice o vives en New York.")
else:
    print("No cumples con las condiciones.")


numero = 7

if not numero == 5:
    print("El número no es igual a 5.")
else:
    print("El número es igual a 5.")