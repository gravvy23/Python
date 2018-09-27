#!/usr/bin/env python3

class NotSortedExc(Exception): pass

#zad1
def fun1(*param):
    if isinstance(param[0],list) or isinstance(param[0],tuple):
        if len(param) > 1: raise TypeError("TypeError: nie wszystkie parametry sa liczbami")
        param = param[0]
    for i in param:
        if not isinstance(i,int) and not isinstance(i,float): raise TypeError("TypeError: nie wszystkie parametry sa liczbami")
    if not list(param) == sorted(param): raise NotSortedExc("NotSorted: nie posortowane")
    return param[len(param)//2]

try:
    val = fun1([1, 2, 3, 4])
except TypeError as myerr:
    print(myerr)
except NotSortedExc as myerr:
    print(myerr)
else: print(val)


#zad2

def fun2(fun,a,b,n):
    if b <= a: raise TypeError("TypeError: zle podane granice calkowania")
    if n <= 0: raise TypeError("TypeError: liczba przedzialow mniejsza od '0'")
    step = (b-a)/n
    suma = 0
    x = a
    while x < b:
        temp = eval(fun)
        x += step
        temp+= eval(fun)
        temp /= 2
        temp *= step
        suma += temp
    return suma
funkcja = 'x'
try:
    calka = fun2(funkcja,0,1,12)
except TypeError as myerr:
    print(myerr)
except NameError as myerr:
    print(myerr)
else: print(calka)

#zad3
l1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l4=(3,4,5,5,13,12,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
class NotLargest(Exception): pass

def fun3(lista):
    trojki = []
    trojki_count = 0
    if (len(lista)%3 and len(lista)%4 ): raise TypeError("Typerror: niepoprawna dlugosc listy")
    if not len(lista)%3:
        for i in range(0,len(lista)-2,3):
            parzyste = 0
            nieparzyste = 0
            if lista[i+2] <= lista[i] or lista[i+2] <= lista[i+1]: raise NotLargest("ostatnia liczba w trojce nie jest najwieksza: index {}".format(i))
            elif (lista[i+2]**2 - lista[i]**2 - lista[i+1]**2) == 0: 
                trojki_count+=1
                for j in range(i,i+3):
                    if lista[j]%2: nieparzyste+=1
                    else: parzyste+=1
                print("parzyste {}, nieparzyste {}".format(parzyste,nieparzyste))
        print("znaleziono {} trojek".format(trojki_count))
        if trojki: raise 
    if not len(lista)%4:
        for i in range(0,len(lista)-3,4):
            parzyste = 0
            nieparzyste = 0
            if lista[i+3] <= lista[i] or lista[i+3] <= lista[i+1] or lista[i+3] <= lista[i+2]: raise NotLargest("ostatnia liczba w czworce nie jest najwieksza: index {}".format(i))
            elif (lista[i+3]**2 - lista[i+2]**2 - lista[i]**2 - lista[i+1]**2) == 0: 
                trojki_count+=1
                for j in range(i,i+4):
                    if lista[j]%2: nieparzyste+=1
                    else: parzyste+=1
                print("parzyste {}, nieparzyste {}".format(parzyste,nieparzyste))
        print("znaleziono {} czworek".format(trojki_count))
        if trojki: raise 
try:
    print("lista 1")
    fun3(l1)
except TypeError as myerr:
    print(myerr)
except NotLargest as myerr:
    print(myerr)
try:
    print("lista 2")
    fun3(l2)
except TypeError as myerr:
    print(myerr)
except NotLargest as myerr:
    print(myerr)
try:
    print("lista 3")
    fun3(l3)
except TypeError as myerr:
    print(myerr)
except NotLargest as myerr:
    print(myerr)
try:
    print("lista 4")
    fun3(l4)
except TypeError as myerr:
    print(myerr)
except NotLargest as myerr:
    print(myerr)

#zad4
import os
def aver(nazwa):
    suma = 0
    if os.access(nazwa,os.R_OK):
        with open(nazwa) as file:
            linie = file.readlines()
            if not len(linie): raise ArithmeticError("Liczba linii w pliku wynosi 0")
            for (i,wiersz) in enumerate(linie):
                wiersz = wiersz.split()
                if len(wiersz) != 2: raise ArithmeticError("wiersz {} nie zawiera dwoch kolumn".format(i))
                wiersz = wiersz[:2]
                for kolumna in wiersz:
                    if not kolumna.isdigit(): raise ArithmeticError("wiersz {} nie zawiera danych liczbowych".format(i))
                    suma+=int(kolumna)
            srednia = suma / (2*len(linie))
            with open(nazwa+':'+str(srednia),'w') as outfile:
                outfile.write(str(srednia))

from glob import glob
pliki = glob('*dat')
for plik in pliki:
    try:
        print(plik)
        aver(plik)
    except ArithmeticError as myerr:
        print(myerr)