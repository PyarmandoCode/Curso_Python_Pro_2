"""
Hacer un Script que simule la reserva de pasajes usando listas en Python. En este caso, utilizaremos una lista para representar los asientos de un avión, donde cada elemento de la lista representa un asiento y su estado (ocupado o libre)
"""

#Crear una Lista de asientos inicialmente vacia
num_asientos=10
asientos = ['Libre'] * num_asientos


def mostrar_asientos():
    print("Estado de los asiento")
    for i ,estado in enumerate(asientos,start=1):
        print(f"Asiento {i}:{estado}")

def reservar_asiento():
    num_asiento=int(input("Ingrese el Numero de asiento que Desea Reservar:"))        
    if 1<= num_asiento <=num_asientos:
        if asientos[num_asiento -1] =='Libre':
            asientos[num_asiento -1]='Ocupado'
            print(f"Reserva exitosa para el asiento {num_asiento}")
        else:
            print("Lo Siento , este asiento esta ocupado")    
    else:
        print("Asiento invalido. Por Favor ingrese un asiento Valido")        

while True:
    print("Menu de Reserva de Pasajes")
    print("1.-Mostrar Asientos")
    print("2.-Reserva Asiento")
    print("3.-Cancelar Reserva")
    print("4.-Salir")
    opcion = input("Seleccione la opcion:")
    if opcion == "1":
        mostrar_asientos()
    elif opcion =="2":
        reservar_asiento()
    elif opcion =="4":
        print("Gracias por utilizar nuestro servicio de reservas!!")
        break
