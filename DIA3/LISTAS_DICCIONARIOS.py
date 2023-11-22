lista_diccionarios = [
    {'nombre':'juan','edad':30},
    {'nombre':'Maria','edad':25},
    {'nombre':'Carlos','edad':35},
    {'nombre':'Gustavo','edad':31},
    {'nombre':'Charles','edad':21},
]


#todo acceder a un diccionario especificio en la lista
primer_diccionario=lista_diccionarios[2]

#todo acceder a un valor especifico dentro de un diccionario de lista
nombre = lista_diccionarios[1]['edad']

#todo modificar un valor en un diccionario dentro de una lista
nombre = lista_diccionarios[1]['edad']=18


#todo Agregar un nuevo diccionario a la lista
nuevo_diccionario={'nombre':'Armando','edad':48}
lista_diccionarios.append(nuevo_diccionario)
#print(lista_diccionarios)

#todo filtrar elementos basados en una condicion usando comprension de listas
mayores_30=[persona for persona in lista_diccionarios if persona['edad']>30]
#print(mayores_30)

for persona in lista_diccionarios:
    if persona['edad']>30:
        pass
    #print(persona)

#todo generar un diccionario a partir de dos listas
claves = ['nombre', 'edad', 'ciudad']
valores = ['Juan', 30, 'Madrid']

diccionario = {clave:valor for clave,valor in zip(claves,valores)}
print(diccionario)