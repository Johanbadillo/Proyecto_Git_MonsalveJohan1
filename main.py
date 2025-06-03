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
        CanIngredientes=int(input("Ingrese la cantidad de ingredientes que tiene la empanada: "))
        diccionarioNuevo={
            "id": (lista[len(lista)-1]["id"])+1,
            "nombre":Nombre,
            "precio":precio,
            "ingredientes":[]
        }
        for i in range (CanIngredientes):
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
        print('=====================================\
            \n           Actualizar Dato            \
            \n=====================================')
        opcionActu=int(input('Ingrese el ID del dato que deseas editar: '))
        VerDato(lista,opcionActu)
        datoTemporal=lista[opcionActu - 1]
        nombreTemporal=str(input('¿Cual nombre deseas colocar?: '))
        precioTemporal=int(input('¿Que precio desear colocar?: '))
        CanIngredientes=int(input("Ingrese la cantidad de ingredientes que tiene la empanada: "))
        listaIngredientesTemporal=[]
        for i in range (CanIngredientes):
            nomIngrediente=str(input("Ingrese el nombre del ingrediente: "))
            disponibilidad=int(input("¿El ingrediente esta disponible?\n1. Si\n2. No\nIngrese una opcion numerica "))
            if(disponibilidad==1):
                diccionarioTemporal={
                    'nomIngrediente':nomIngrediente,
                    'disponibilidad':'si'
                }
            else:
                diccionarioTemporal={
                    'nomIngrediente':nomIngrediente,
                    'disponibilidad':'no'
                }
            listaIngredientesTemporal.append(diccionarioTemporal)
        diccionarioAgregar={
            "id": lista[opcionActu - 1]['id'],
            "nombre": nombreTemporal,
            "precio": precioTemporal,
            "ingredientes": listaIngredientesTemporal
            }
        lista[opcionActu - 1]=diccionarioAgregar
        guardarJSON(lista)
    elif(Opcion==3):
        print('=====================================\
            \n           Eliminar Dato            \
            \n=====================================')
        opcionActu=int(input('Ingrese el ID del dato que deseas eliminar: '))
        VerDato(lista,opcionActu)
        confirmacion=int(input('¿Estas seguro de eliminar este dato?\n1. Si\n2. No\nIngrese una opcion numerica: '))
        if (confirmacion==1):
            lista.pop(opcionActu-1)
            guardarJSON(lista)
            print("Usuario eliminado!")
        else:
            print("Gracias por confirmar!")


















# prueba de conflito inicial menu inicial
# Creador por Johan Styben Monsalve Badillo 