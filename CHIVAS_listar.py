from CHIVAS_conexion import conexion
import sqlite3

def tareas_pendientes():
    try:
        connection = conexion()
        cursor = connection.cursor()
        if not connection:
            print("No se pudo conectar a la base de datos")
            return
        query = "SELECT * FROM tareas WHERE ESTATUS = 0"
        cursor.execute(query)
        lista = cursor.fetchall()
        for i in lista:
            print(i)
    except sqlite3.Error as e:
        print(f"Error al consultar: {e}")
    finally:
        connection.close()