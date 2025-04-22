from CHIVAS_conexion import conexion
import sqlite3

def agregar_tarea():
    try:
        connection = conexion()
        if not connection:
            print("no se pudo conectar a la base de datos...")
            return
        description = input("Agregue una descripcion de la tarea: ")
        query = ('''INSERT INTO tareas (DESCRIPCION, ESTATUS) VALUES (?, 0)''')
        connection.execute(query, (description,))
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Error al agregar la tarea: {e}")
    finally:
        connection.close()
