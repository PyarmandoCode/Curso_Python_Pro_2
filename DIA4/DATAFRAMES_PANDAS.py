import pandas as pd
#Crear un dataframe de ejemplo
data = {
    'Nombre': ['Ana', 'Juan', 'María', 'Pedro', 'Luis'],
    'Edad': [26, 30, 42, 35, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Bilbao']
}
df = pd.DataFrame(data)
"""
Algunos Ejmplos Especificos
"""
nombre = df['Nombre']
#print(nombre)
#todo  Filtrar personas mayores de 25 años
mayores_de_25 = df[df['Edad']>25]
#todo Filtrar personas mayores de 25 años y que vivan en Madrid
mayores_madrid = df[(df['Edad']>25) & (df['Ciudad']=='Madrid')]
#todo Filtrar personas que viven en Madrid o Barcelona
madrid_barcelona = df[df['Ciudad'].isin(['Madrid','Barcelona'])]
print(madrid_barcelona)