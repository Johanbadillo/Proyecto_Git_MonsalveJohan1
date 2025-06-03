# funciones para el codigo principal


#Aqui vamos a ver los ingredientes de una manera ordenada
def recorrerIngredientes(lista,posicion):
    posicion -=1
    for i in range(len(lista[posicion]['ingredientes'])):
        print('============================\
        \nIngrediente N.',i+1,':\
        \n--- Nombre del Ingrediente: ',lista[posicion]['ingredientes'][i]['nomIngrediente'],'\
        \n--- Disponibilidad: ',lista[posicion]['ingredientes'][i]['disponibilidad'],)

#Mostrar el dato que recae la accion 
def VerDato(lista,opcionActu):
    print('=============================')
    print('        Dato N.',opcionActu)
    print('=============================')
    print('ID:', lista[opcionActu - 1]['id'])
    print('Nombre:', lista[opcionActu - 1]['nombre'])
    print('Precio:', lista[opcionActu - 1]['precio'])
    recorrerIngredientes(lista,opcionActu)