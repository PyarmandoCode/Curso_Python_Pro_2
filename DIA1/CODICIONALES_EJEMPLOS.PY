"""
Escribir un Script que pida al usuario una nota y muestre la categoria de la nota segun uns escala predefinidad
0 -- 10 = Rango
  <5 = INSUFICIENTE
  5-<7 = APROBO
  7-<=9 = NOTABLE
  CASO CONTRARIO =SOBRESALIENTE

nota = float(input("Ingrese la Nota:"))
if 0 <= nota <=10:
    if nota <5:
        print("Insuficiente")
    elif 5 <=nota <7:
        print("Aprobo")
    elif 7 <=nota <9:
        print("Notable")
    else:
        print("Sobresaliente")    
else:
    print("Nota Fuera de Rango")
"""
"""
Escribir un Script que solcite al usario ingresar un Numero 1 al 7
y luego muestre el dai de la semana correspondiente.
considera que 1 es Lunes 2 es Martes y asi sucesivamente

dia = int(input("Ingrese dia de la semana:"))
if dia == 1:
    print("Lunes")
elif dia ==2:
    print("Martes")
elif dia ==3:
    print("Miercoles")
elif dia ==4:
    print("Jueves")    
elif dia ==5:
    print("Viernes")    
elif dia ==6:
    print("Sabado")    
elif dia ==7:
    print("Domingo")    
else:
    print("Dia Invalido")  
"""
  

dia = int(input("Ingrese dia de la semana:"))
if dia == 1:
    print("Lunes")
elif dia ==2:
    print("Martes")
elif dia ==3:
    print("Miercoles")
elif dia ==4:
    print("Jueves")    
elif dia ==5:
    print("Viernes")    
elif dia ==6:
    print("Sabado")    
elif dia ==7:
    print("Domingo")    
else:
    print("Dia Invalido")  

#Listas
dia = int(input("Ingrese dia de la semana:"))
if 1 <= dia <=7:
    dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print(f"El Dia {dia} corresponde al dia {dias_semana[dia-1]} ")
else:
    print("Dia Invalido")    



