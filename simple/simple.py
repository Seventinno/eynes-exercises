import random


def simple_list():
    # Lista a donde se almacenaran los diccionarios
    lista = []
    diccionario = []

    for i in range(1, 11):
        # numero aleatorio para la edad
        edad = random.randint(1, 100)
        diccionario = {"id": i, "age": edad}
        lista.append(diccionario)

    return lista


def sort_list(lista):
    lista_arreglada = sorted(lista, key=lambda x: x['age'])
    return lista_arreglada


print(sort_list(simple_list()))
