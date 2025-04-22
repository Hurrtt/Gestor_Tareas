from CHIVAS_conexion import conexion
import sqlite3

def eliminar_tareas():
    try:
        connection = conexion()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tareas")
        all_tareas = cursor.fetchall()
        for tareas in all_tareas:
            print(tareas)
        delete = int(input("Ingrese el ID de la tarea que desea eliminar: "))
        query = "DELETE FROM tareas WHERE ID = ?"
        connection.execute(query, (delete,))
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error inesperado: {e}")
    finally:
        connection.close()
