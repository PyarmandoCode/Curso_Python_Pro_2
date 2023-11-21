"""
Hacer un Script que  simula un cajero automático

"""

saldo=1000

#Mostrar el Menu y realizar operaciones
def mostrar_menu():
    print("\nMenu de Opciones")
    print("1.-Consultar Saldo")
    print("2.-Retirar Dinero")
    print("3.-Depositar Dinero")
    print("4.-Salir")

def consultar_saldo():
    print(f"Tu Saldo actual es: {saldo}")

def retirar_saldo():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar:$"))    
    if cantidad > saldo:
        print("No Tienes Suficiente Saldo para retirar OYEEE!!")
    else:    
        saldo -= cantidad
        print(f"Retirastes: ${cantidad}\nTu Saldo restante es : ${saldo}")

def depositar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar:$"))    
    saldo += cantidad
    print(f"Despositastes: ${cantidad}\nTu Saldo actual es : ${saldo}")


#Blucle - LOOP principal del programa
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una Opcion:"))
    if opcion == 1:
        consultar_saldo()
    elif opcion ==2:
        retirar_saldo()    
    elif opcion ==3:
        depositar_dinero()        
    elif opcion == 4:
        break
    else:
        print("Opcion Invalida")





