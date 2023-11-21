# contador=1
# while contador <=5:#Iterar la condicion sea Verdadera salir del bucle
#     print(contador)
#     contador +=1


"""
Desea Continuar
acum =0
while True:
    num = int(input("Ingrese un Numero a Acumular:"))
    acum +=num
    rpta = input("Desea Continuar:")
    if rpta.lower() =='n':
        break # Ejecuta True
print(f"La Suma total es: {acum}")
"""
    


"""
crear un script simple de login con tres intentos utilizando un bucle while en Python:
"""

#datos de usuario valido
usuario_valido="admin"
contraseña_valida="123456"

intentos =3
while intentos >0:
    usuario= input("Usuario:")
    contraseña= input("Contraseña:")
    if usuario ==usuario_valido and contraseña == contraseña_valida:
        print("Inicio de Sesion exitoso , Bienvenido")
        break
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos . Intentos restantes {intentos}")

if intentos ==0:
    print("Has agotado todos los intentos.Cuenta BLOQUEADA.")



