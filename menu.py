from consulta import agregar_tarea
from CHIVAS_listar import tareas_pendientes
from complete import complete
from eliminar import eliminar_tareas
def menu():
    print("Ingrese una opcion: \n1-Agregar tarea \n2-Ver tareas pendientes \n3-Marcar tarea completada \n4-Eliminar tarea \n5-Salir")
    opc = input()
    while opc != '5':
        if opc == '1':
            agregar_tarea()
        if opc == '2':
            tareas_pendientes()
        if opc == '3':
            complete()
        if opc == '4':
            eliminar_tareas()
        if opc == '5':
            print("Hasta luego")
        else:
            print("Elija una opcion valida...")
            return menu()
menu()