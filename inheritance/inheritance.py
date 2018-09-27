#!/usr/bin/env python3
#zad1

class B:
    def __init__(self,start,stop):
        self.x = start
        self.stop =stop

    def __next__(self):
        flag = True
        while flag is True:
            self.x+=1
            for _ in range(2,self.x):
                if self.x % _ == 0:
                    flag = False
                    break
            if flag:
                if self.x > self.stop: raise StopIteration
                return self.x






class A:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return B(self.start, self.stop)




a = A(2,10)
for i in a:
    for j in a:
        print(i,j)


#zad2

class Pascal:  
    def __init__(self,liczba_wierszy):
        self.wiersze = liczba_wierszy
        self.obecny = 1
        self.prev = [0]

    def __iter__(self):
        return self

    def __next__(self):
        current = []
        current.append(1)
        for j in range(len(self.prev) - 1):
            current.append(self.prev[j] + self.prev[j + 1])
        if (self.obecny is not 1): current.append(1)
        self.prev = current
        if self.obecny > self.wiersze: raise StopIteration
        self.obecny+=1
        return self.prev

for i in Pascal(5):
    print(i)

#zad3
from math import sin, fabs

class my_random:
    def __init__(self):
        self.step = 1
        self.a = 44485709377909
        self.c = 0
        self.x = 1
        self.m = pow(2,48)

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a*self.x+self.c)%self.m
        return self.x/self.m



def integral(fun,x1,x2,d,expected):
    c = 0
    n = 0
    y1 = fun(x1)
    y2 = fun(x2)
    m_min = y1
    zakres = fabs(y2 - y1)
    if m_min > y2: m_min=y2
    for i in my_random():
        kr = (i*(x2-x1)+x1,i*2-1)
        print(kr)
        if kr[1] > 0 and kr[1] < fun(kr[0]):
            c += 1
        elif kr[1] < 0 and kr[1] > fun(kr[0]):
            c -= 1
        n += 1
        val = (x2-x1)*zakres*c/n
        if fabs(val-expected) < d: break
    return n

def foo(x):
    return sin(x)

#print(integral(foo,0,5,1e-3,0.71634))
