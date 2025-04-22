from createTables import conexion
import sqlite3

def complete():
    try:
        connection = conexion()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tareas WHERE ESTATUS = 0")
        pendientes = cursor.fetchall()
        for tareas in pendientes:
            print(tareas)
        tarea_completada = int(input("Ingrese el ID de la tarea que completo: "))
        query = "UPDATE tareas SET ESTATUS = 1 WHERE ID = ?"
        connection.execute(query, (tarea_completada, ))
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error inesperado: {e}")
    finally:
        connection.close()
