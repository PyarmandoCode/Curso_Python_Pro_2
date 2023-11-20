nom_clie = "Armando" # str
ape_clie = 'Ruiz' # str
edad_clie = 49 # int
pago_clie = 1200.3445454 # float
tien_des = True # bool

nombre_completo_1 = nom_clie + ape_clie  + str(edad_clie)# todo uniendo strings 1
nombre_completo_2 = nom_clie , ape_clie , edad_clie # todo uniendo strings 2
nombre_completo_3 = f" El Nombre Completo es {nom_clie}  y apellido {ape_clie} y su edad {edad_clie}"

#print(nombre_completo_1)
#print(nombre_completo_2)
#print(nombre_completo_3)

#todo formateo de decimales
formateo_dec_1 = f"{pago_clie:.4f}"
formateo_dec_2 = "{:.2f}".format(pago_clie)
print(formateo_dec_1)
print(formateo_dec_2)




