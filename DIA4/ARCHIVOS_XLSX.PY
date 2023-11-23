"""
MODULO - PAQUETE  - BIBLIOTECA
OPENPYXL
"""
import openpyxl

#Cargando el libro de trabajo
archivo_xlsx = openpyxl.load_workbook('factura_34454.xlsx')

#Seleccione la hoja de trabajo por su nombre
hoja_trabajo = archivo_xlsx['FACTURA']

#Obtener los valores de las celdas 
for fila in hoja_trabajo.iter_rows(values_only=True):
    print(fila)




