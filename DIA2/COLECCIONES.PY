personas = {
             "a1":"jose",
             "a2":"pedro",
             "a3":"jose"
             } #DICT

personas = ("JOSE","PEDRO","JUAN") #TUPLE INMUTABLE

personas = {"JOSE","PEDRO","JUAN"} #SETS

personas = ["JOSE","PEDRO","JUAN"] #LIST MUTABLE
personas[0]="JOSE ARTURO" #Modificar un Elemento de la lista

"""
AÑADIR ELEMENTO A UNA LISTA

*APPEND .-AÑADE UN ELEMENTO AL FINAL DE LA LISTA
*INSERT .-AÑADE EN CUALQUIER POSICION

personas.append("ARMANDO")
personas.insert(2,"MIGUEL")

ELIMINAR ELEMENTOS DE DE LISTA
*POP.-Eliminar por el Indice
*REMOVE.-Eliminar por su valor

personas.pop(2)
personas.remove("PEDRO")

"""
frutas = ["manzana", "banana", "naranja", "kiwi"]
#Susbtraer o Rebanar
fruta1 = frutas[2:] #['naranja', 'kiwi']
fruta2 = frutas[1:3] #['banana', 'naranja']
fruta3 = frutas[-2:]#['naranja', 'kiwi'] 

frutas.sort() #asce
frutas.reverse() #desc
size = len(frutas) #cantidad de elementos de una Lista
#print(f"La Cantidad de elementos de una Lista {size}")
#print(frutas)

"""
Realizar un script que me permita ingresar un elemento a la lista
si no existe añadirlo ,si existiera me indique en que posicion esta

while True:
    nueva_fruta=input("Ingresar el elemento:")
    if nueva_fruta in frutas:
        posicion=frutas.index(nueva_fruta)
        print(f"La Fruta ya existe y se encuentra en la posicion {posicion}")
        rpta=input("Desea Continuar :")
        if rpta.lower() == "n":
            break
    else:
        frutas.append(nueva_fruta)    
        print(frutas)
"""

"""
enumerate - Me permite colocar un indice a cada elemento de 
mi lista , si se utiliza el argumento start le indico de que
posicion empezar
"""

frutas = ["manzana", "banana", "naranja", "kiwi"]
for index,nombre in enumerate(frutas,start=1):
    print(f" {index} {nombre}")




