import numpy as np


def zad2():
    print("Hello World")


def zad3():
    print("""Miauczy kotek: miau!
            - Coś ty, kotku, miał?
            - Miałem ja miseczkę mleczka,
            Teraz pusta jest miseczka,
            A jeszcze bym chciał.
            
            Wzdycha kotek: o!
            - Co ci, kotku, co?
            - Śniła mi się wielka rzeka,
            Wielka rzeka, pełna mleka
            Aż po samo dno.
            
            Pisnął kotek: pii...
            - Pij, koteczku, pij!
            Skulił ogon, zmrużył ślipie,
            Śpi - i we śnie mleczko chlipie,
            Bo znów mu się śni.
            """)


def zad4(x, y):
    if x == y:
        return "TAK"
    return "NIE"


def zad5(x):
    if x % 2 == 0:
        return "Zmienna jest parzysta"
    return "Zmienna nie jest parzysta"


def zad6(x,y):
    if x > y:
        print(x)
    elif x == y:
        print("Liczby sa rowne")
    print(y)


def zad7(num):
    if len(str(num)) < 3:
        return "Zbyt krotka liczba"
    for i in range(-1,-4,-1):
        print(str(num)[i])


def zad8(lista):
    for i in range(0,len(lista)):
        if i % 2:
            print(lista[i])


def zad9(lista):
    return [(napis,len(napis)) for napis in lista]


def zad10(lista1,lista2):
    result = []
    while lista1 and lista2:
        if lista1[0] < lista2[0]:
            result.append(lista1.pop(0))
        else:
            result.append(lista2.pop(0))
    result += lista1 + lista2
    return result


def zad11(matrix):
    for n in matrix:
        for i in range(0,len(n),-1):
            print(n[i])

def zad12(macierz):
    i = 0
    sum = 0
    for row in macierz:
        sum += row[i]
        i = i + 1
    return sum

def zad13(macierz,skalar):
    for i in range(0,len(macierz)):
        for j in range(0,len(i)):
            macierz[i][j] = macierz[i][j] * skalar


def zad14():
    lista = [i for i in range(1,21)]
    return [lista, reversed(lista)]


def zad15(lista1,lista2):
    return lista1+lista2


def zad16(macierz):
    return max([wiersz for wiersz in macierz])


def zad17(macierz):
    return macierz.transpose()


def zad18(lista):
    return sorted(lista)[-2]

def zad19(lista,element):
    if element in lista:
        return "TAK"
    return "NIE"






