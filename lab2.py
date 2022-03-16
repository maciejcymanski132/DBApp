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


def zad10():
    pass


def zad11(l1,l2,l3):
    for element in l1:
        if element in l2 and element in l3:
            print(element)

