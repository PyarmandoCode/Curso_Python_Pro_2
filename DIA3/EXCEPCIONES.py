"""
try:
    #todo codigo que podria generar la excepcion
    numero = int(input("Ingrese un Numero:"))
    resultado = numero / 0
except ZeroDivisionError as error:
    #todo manejo de la excepcion = ERROR
    print(f"Error {error}")
else:
    #todo se ejecuta si NO hay excepciones en el bloque try
    print("La Divion se realizo correctamente")
finally:
    #todo Se ejecuta siempre , haya excepcion o no
    print("Finalizando el proceso")
"""


"""
Realizar un script que me permita automatizar el pago de la planilla de un personal
"""
planilla_nov = [
    {"cod":"A100","AREA":"SISTEMAS","HT":10,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A200","AREA":"SISTEMAS","HT":20,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A300","AREA":"CONTABILIDAD","HT":40,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A400","AREA":"CONTABILIDAD","HT":50,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A500","AREA":"RH","HT":23,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A600","AREA":"RH","HT":81,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A700","AREA":"RH","HT":12,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A800","AREA":"MARKETING","HT":1,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A900","AREA":"MARKETING","HT":7,"BON":"","SUSBT":"","NETO":""},
    {"cod":"A000","AREA":"SISTEMAS","HT":120,"BON":"","SUSBT":"","NETO":""},
]

def generar_txt(data):
    nombre_archivo="Planilla_NOV.txt"
    with open(nombre_archivo,'w') as archivo:
        for items  in data:
            archivo.write(f"{items}:\n")
        print(f"Los Resultados se hab guardado en el archivo {nombre_archivo}")    
try:
    for items in planilla_nov:
        items["SUSBT"]=items["HT"]*30
        if items["HT"]>100:
            items["BON"]=10
        else:
            items["BON"]=0    
        items["NETO"] =  items["SUSBT"] + items["BON"]
    generar_txt(planilla_nov)    
except Exception as error:
    print(f"El Error es el siguiente {error}")
finally:
    print("Finalizado el Proceso")













