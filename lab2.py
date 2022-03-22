import numpy

#zad2
def ispermutation(l1,l2):
    if sorted(l1) == sorted(l2):
        return True
    return False

#zad3
def zad3(songs):
    for key,value in songs.items():
        if value > 5:
            print(key)


def zad4(d,v,e):
    for key,value in d.items():
        if value == v:
            d[key] = e

#zad5
def related_values(d,v):
    return [k for k in d.keys() if d[k] == v]

def invert(d):
    return {v:related_values(d,v) for v in set(d.values())}

#zad6


#zad7


#zad8
def zad8(text):
    return {letter:text.count(letter) for letter in text}

#zad9
def zad9(text):
    count = zad8(text)
    return sorted(count.keys(),key= lambda x: count[x])[-2:]

#zad10

def zad10(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return f"Element occurs at index :{mid}"
    return "Element doesn't occur in given array"


def zad11(l1,l2,l3):
    for element in l1:
        if element in l2 and element in l3:
            print(element)

def zad12(matrix):
    result = sorted(matrix, key=lambda x: x.count(1))[-1]
    if result == 0:
        return -1
    return result


def zad13(matrix):
    result = max(matrix,key=lambda x: x.count(1))
    if result.count(1) == 0:
        return -1
    return result

def zad14():
    tuple1 = ("Apple", [10, 20, 30], (15, 25, 35))
    print(tuple1[1][1])

def zad15():
    tuple1 = (1,2,3,4)
    a,b,c,d = tuple1[0],tuple1[1],tuple1[2],tuple1[3]


#Zad16
def zad16(tuple1,tuple2):
    tuple1,tuple2 = tuple2,tuple1

def zad17(tup):
    return tup.count(1)
