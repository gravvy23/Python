#!/usr/bin/env python3
import sys
sys.path.append('build/lib.linux-x86_64-3.5/')
import mod
print(mod.met(1,1))

#zad1
from random import randint
zakres = 1000

def BubbleSortPy(tab,n):
    while n > 1:
        for j in range(n-1):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1],tab[j]
        n=n-1

from time import time
from random import randint

def test(testFunction1, testFunction2 ,size):
    lista = []
    for i in range(size):
        lista.append(randint(0,size))
    list1 = lista[:]
    list2 = lista[:]
    t1 = time()
    testFunction1(list1)
    t2 = time()
    print('C: {}'.format(t2-t1))
    t1 = time()
    testFunction2(list2,size)
    t2 = time()
    print('python: {}'.format(t2-t1))

test(mod.BubbleSortC,BubbleSortPy,1000)

#zad2
my_dict = {}

for i in range(10,1000):
    my_dict[i] = randint(10,1000)

a = mod.zad2(my_dict)
print(a)