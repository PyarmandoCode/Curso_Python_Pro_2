"""
Lectura de un Archivo CSV
"""
import csv as MI_CSV
with open('factura_34454.csv',newline='')  as archivo_csv:
    lector_csv =MI_CSV.reader(archivo_csv)

    #iterar sobre las filas del archivo
    for fila in lector_csv:
        print(fila)