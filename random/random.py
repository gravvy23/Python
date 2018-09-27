#!/usr/bin/env python3
from sys import argv
import random

#zad1
def palindrom(a):
    return (a == a[-1::-1])


val = palindrom(argv[1])
print(val)
#zad2

s={}
while len(s) < 100:
    k = random.randint(100,1000)
    if not s.get(k,0) : s[k] = palindrom(str(k))

print(s)
#zad3
l=[random.randrange(0,20) for _ in range(100)]
s1={}
s2={}
for _ in enumerate(l):
    if not _[1]%2:
        s1.setdefault(_[1],[]).append(_[0])

for k in s1:
    lista = s1[k]
    mediana = lista[len(lista)//2]
    rozstep = lista[-1]-lista[0]
    s2[k]=(mediana,rozstep)

print(s1)
print(s2)
#zad4
s3={k:random.randrange(2,15) for k in range(int(argv[1]))}
l = list(s3.items())
s4={s3[k]:k for k in s3.keys()}

print(s3)
#zad5
l=[random.randrange(0,11) for _ in range(100)]
s={}

for x in l:
    s.setdefault(x,[]).append(l.index(x,s[x][-1]+1) if s[x] else l.index(x))

print(s)
#zad6
s1={x:random.randrange(1,100) for x in range(10)}
s2={x:random.randrange(1,100) for x in range(10)}
s1={s1[k]:k for k in s1.keys()}
s2={s2[k]:k for k in s2.keys()}
s3={k:(s1[k],s2[k]) for k in s1.keys() if s2.get(k,False)}

print(s1)
print(s2)
print(s3)