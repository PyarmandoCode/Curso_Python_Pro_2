
def calcular_edad(nac):
    edad = 2023 - nac
    return edad

def mensaje_bienvenida(user,passw,nom=None):
    if user=="Admin" and passw=="123":
        return f"Bienvenido {nom} QUE BUENO tenerte por aca"
    else:
        return f"Usuario {nom} Invalido"

def cambiar_pesos_dolares(pesos):
    valor_dolar=3.7
    dolares= pesos / valor_dolar
    return dolares

def contar_vocales(frase):
    frase = frase.lower() #convierte a minuscula
    vocales='aeiou'
    contador= 0

    for letra in frase:
        if letra in vocales:
            contador +=1
    return contador   

#calcular_edad()
#print(mensaje_bienvenida("Admin123","123","Armando"))
#print(cambiar_pesos_dolares(1000))