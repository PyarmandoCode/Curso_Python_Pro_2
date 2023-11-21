"""
UTILIZE EL BUCLE FOR CUANDO CONOZCA EL # DE VUELTAS QUE VA A ITERAR
"""

# for _ in range(10):
#     print("Hola desde Python")
# print("Adios.....")    

# for indice in range(10): #utilizando End
#     print(f"{indice} - Hola desde Python")
# print("Adios.....")    


# for indice in range(1,10): #utilizando Start y End
#     print(f"{indice} - Hola desde Python")
# print("Adios.....")    


# for indice in range(1,10,3): # utilizando el tercer parametro STEP = SALTO
#     print(f"{indice} - Hola desde Python")
# print("Adios.....")    


"""
Ejemplo de Break = Interrumpir el Bucle ne la vuelta indicada

for indice in range(1,10):
    if indice == 5:
        break
    else:
        print(f"{indice} - Hola desde Python")
"""



"""
Ejemplo con Continue = Es obviar una condicion
for indice in range(1,10):
    if indice == 5:
        continue
    else:
        print(f"{indice} - Hola desde Python")
"""        



"""
Hacer un Script que imprimia los numeros de 0 a 6 (Inclusive)
saltando el numero 2 y deteniendose en el numero 7
for indice in range(1,10):
    if indice ==2:
        continue # Saltar la iteración cuando indice es igual a 2
    if indice ==7:
        break    # Salir del bucle cuando indice es igual a 7
    else:
        print(f"{indice} - Hola desde Python")
"""

"""
Desde se puede iterar ? - Variables - Colecciones

frase = "Murcielago"
for letra in frase:
    print(letra)
"""



dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia  in dias_semana:
    print(dia)






