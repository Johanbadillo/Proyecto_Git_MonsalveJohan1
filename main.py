# #########################
#   Proyecto git Prueba
# #########################

from Funciones.funcionesJson import *
from Funciones.funciones import *

lista=abrirJSON()
salida=True

while(salida):
    lista=abrirJSON()
    print("\nBienvenido a nuestro programa de empanadas Doña Pepa\
        \n=====================================\
        \n           Menu Principal             \
        \n======================================\
        \nGestion de Datos:\
        \n1. Agregar dato nuevo\
        \n2. Editar dato\
        \n3. Eliminar dato\
        \n4. Salir")
    Opcion=int(input("Ingrese una opcion numerica\n"))
    if(Opcion==1):
        Nombre=str(input("Ingrese el nombre de la empanada: "))
        precio=int(input("Ingrese el precio de la empanada sin puntos ni comas: "))
        Caningredientes=int(input("Ingrese la cantidad de ingredientes que tiene la empanada: "))
        diccionarioNuevo={
            "id": (lista[len(lista)-1]["id"])+1,
            "nombre":Nombre,
            "precio":precio,
            "ingredientes":[]
        }
        for i in range (Caningredientes):
            nomIngrediente=str(input("Ingrese el nombre del ingrediente: "))
            disponibilidad=int(input("¿El ingrediente esta disponible?\n1. Si\n2. No\nIngrese una opcion numerica "))
            if(disponibilidad==1):
                disponible=str('si')
            else:
                disponible=str('no')
            data_Ingredientes={
                'nomIngrediente':nomIngrediente,
                'disponibilidad':disponible
            }
            diccionarioNuevo["ingredientes"].append(data_Ingredientes)
        lista.append(diccionarioNuevo)
        guardarJSON(lista)
    elif(Opcion==2):
        print("Bienvenido a nuestro programa de empanadas Doña Pepa\
        \n\
        \n=====================================\
        \n           Actualizar Dato           \
        \n=====================================")
        opcionActu=int(input('Ingrese el ID del dato que deseas editar: '))
        VerDato(lista,opcionActu)

        


















# prueba de conflito inicial menu inicial
# Creador por Johan Styben Monsalve Badillo 