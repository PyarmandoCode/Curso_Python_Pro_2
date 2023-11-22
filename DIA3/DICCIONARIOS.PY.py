
mi_diccionario = {} # todo Crear un Diccionario Vacio
mi_diccionario = dict() # todo Diccionario Vacio


mi_diccionario = {
    "nombre":"Juan",
    "edad":30,
    "ciudad":"New York"
}

#print(mi_diccionario['nombre']) #todo acceder a un valor usando la clave
#print(mi_diccionario['edad']) #todo acceder a un valor usando la clave
#print(mi_diccionario['ciudad']) #todo acceder a un valor usando la clave

mi_diccionario['profesion'] ='Developer' #todo agregar un nuevo elemento al diccionario
mi_diccionario['nombre'] ='Oscar'

del mi_diccionario['profesion']#todo elimina un elemento por la clave

claves = mi_diccionario.keys() #todo obtener todas las claves del diccionario
valores = mi_diccionario.values() #todo obtener todas los valores del diccionario
claves_valores = mi_diccionario.items() #todo obtener todas los valores y claves del diccionario

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f"La Clave {k} y Su Valor {v}")

#print (claves_valores)