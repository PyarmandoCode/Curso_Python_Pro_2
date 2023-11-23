import sqlite3
import matplotlib.pyplot as plt
"""
Debes instalar la libreria de pandas utilizando
pip install pandas -Especificamente los Dataframes
"""
import pandas as pd
#Conectarse a la base de datos (Crear un Archivo si no existe)
conn = sqlite3.connect('bdejemplo.db')

#Crear un Cursor para interactuar con la BD
cursor = conn.cursor()

#Crear una Tabla para interactuar con la BD
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY,
               nombre TEXT,
               edad INTEGER,
               email TEXT,
               ventas DECIMAL(7,3)
               
              )''')

#Funcion para insertar Datos
def insertar_usuario(nombre,edad,email,ventas):
    try:
        cursor.execute('''INSERT INTO usuarios (nombre,edad,email,ventas) VALUES(?,?,?,?)''',(nombre,edad,email,ventas))
        conn.commit() #los Registro se inserten fisicamente en la tabla
        print("Usuario insertado correctamente")
    except Exception as error:
        print(f"Ocurrio un error {error}")
    finally:
        pass
        #conn.close()

def obtener_usuarios():
    try:
        cursor.execute('''SELECT * FROM usuarios''')
        usuarios=cursor.fetchall() #todos los registros
        for usuario in usuarios:
            print(usuario)
    except Exception as error:
        print(f"ocurrio un error {error}")
    finally:
        conn.close

#todo se debe instalar pandas antes de ejecutar esta Funcion
def obtener_usuarios_df():
    try:
        query="SELECT * FROM usuarios"
        df = pd.read_sql_query(query,conn)
        print(df)
        generar_grafico_ventas(df)
    except Exception as error:
        print(f"ocurrio un error {error}")
    finally:
        conn.close

def generar_grafico_ventas(df):
    usuarios = df['nombre']
    ventas = df['ventas']
    plt.pie(ventas, labels=usuarios, autopct='%1.1f%%')
    plt.show()

def consulta_usuarios_codigo(codigo):
    try:
        cursor.execute('''SELECT * FROM usuarios where id = ?''',(codigo,))
        usuario = cursor.fetchone()#cuando la consulta te devuelve un solo registro
        print(usuario)
    except Exception as error:
        print(f"ocurrio un error {error}")    
    finally:
        pass


obtener_usuarios_df()
#consulta_usuarios_codigo(3)

# insertar_usuario('MARIA',28,'maria@gmail.com',1700.00)
# insertar_usuario('PEDRO',18,'pedro@gmail.com',1900.50)
# insertar_usuario('PILAR',25,'pilar@gmail.com',1700.00)
# insertar_usuario('GUSTAVO',33,'gustavo@gmail.com',500.20)
# insertar_usuario('MANUEL',19,'manuel@gmail.com',900.20)



