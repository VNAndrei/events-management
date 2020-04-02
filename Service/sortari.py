"""
Created on Jan 7, 2019

@author: Andrei
"""


def selection_sort(lista, key=lambda x: x, invers=False):
    if invers == True:
        for i in range(0, len(lista) - 1):
            for j in range(i, len(lista)):
                if key(lista[i]) < key(lista[j]):
                    lista[i], lista[j] = lista[j], lista[i]
        return lista
    else:
        for i in range(0, len(lista) - 1):
            for j in range(i, len(lista)):
                if key(lista[i]) > key(lista[j]):
                    lista[i], lista[j] = lista[j], lista[i]
        return lista


def shaker_sort(lista, key=lambda x: x, invers=False):
    if len(lista) == 1:
        return [lista[0]]
    if len(lista) == 2:
        if key(lista[0]) < key(lista[1]):
            return lista
        else:
            return [lista[1], lista[0]]

    if invers == False:
        for i in range(0, len(lista) - 1):
            if key(lista[i]) > key(lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

        for i in range(len(lista) - 2, 0, -1):
            if key(lista[i]) < key(lista[i - 1]):
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        return [lista[0]] + shaker_sort(lista[1:len(lista) - 1], key, invers) + [lista[len(lista) - 1]]
    else:
        for i in range(0, len(lista) - 1):
            if key(lista[i]) < key(lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

        for i in range(len(lista) - 1, 0, -1):
            if key(lista[i]) > key(lista[i - 1]):
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        return [lista[0]] + shaker_sort(lista[1:len(lista) - 1], key, invers) + [lista[len(lista) - 1]]
