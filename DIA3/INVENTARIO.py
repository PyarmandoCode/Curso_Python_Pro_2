datos = [
    {"variedad":"ipa","precio":1.4,"stock":10},
    {"variedad":"pills","precio":1.2,"stock":50},
    {"variedad":"amber","precio":1.1,"stock":100}
]

#print(datos[0])

total=0
def disminuir_stock(variedad,cantidad,datos):
    global total
    for items in datos:
        if items['variedad'] == variedad:
            items['stock'] -= cantidad
            total += items['precio'] * cantidad
            print(f"El Stock Actual es {items['stock']}")
while True:
    for items in datos:
        variedad_buscar=input("Ingrese la Variedad:")
        if  not variedad_buscar in items['variedad']:
            break
        else:
            cantidad=int(input("Ingrese la Cantidad:"))
            disminuir_stock(variedad_buscar,cantidad,datos)
    print(f"Total = $ {round(total)} ")
    break




