#!/usr/bin/env python3
from time import time
from sys import version
import random
from math import sqrt 
from functools import reduce

powt=1000
N=10000

def forStatement():
    l = []
    for i in range(N):
        l.append(i)
    return l

def listComprehension():
    l = [i for i in range(N)]
    return l

def mapFunction():
    l = map((lambda x:x),range(N))
    return l

def generatorExpression():
    l = (i for i in range(N))

def tester(fun):
    start = time()
    for i in range(powt): fun()
    stop = time()
    return (stop - start)


print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
 print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

 #zad2
 l1 = [random.randint(0,20) for i in range(100)]
 l2 = [random.randint(0,20) for i in range(100)]
filter(lambda x,y:3<x+y<15,zip(l1,l2))

#zad3
def fun3(sx,sy):
    x_mean = sum(sx)/len(sx)
    y_mean = sum(sy)/len(sy)
    D = sum(map(lambda x:(x-x_mean)**2,sx))
    a = sum(map(lambda x,y:y*(x-x_mean),sx,sy))/D
    b = y_mean - a*x_mean
    delta_y = sqrt( sum(map((lambda x,y:(y-a*x+b)**2),sx,sy))/ (len(sx)+2) )
    delta_a = delta_y/sqrt(D)
    delta_b = delta_y*sqrt(1/len(sx)+(x_mean**2)/D)
    return (D,a,b,delta_y,delta_a,delta_b)
print(fun3([1,2,3],[1,2,3]))
#zad4
def myreduce(fun,seq):
    prev = seq[0]
    for x in seq[1:]:
        prev = fun(prev,x)
    return prev
l = [1 for _ in range(10)]
print("myreduce: {} reduce: {}".format(myreduce(lambda x,y:x+y,l),reduce(lambda x,y:x+y,l)))
print("myreduce: {} reduce: {}".format(myreduce(lambda x,y:x*y,l),reduce(lambda x,y:x*y,l)))
#zad5
my_list = [[1,1],[1,2],[1,3]]
