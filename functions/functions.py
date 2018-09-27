#!/usr/bin/env python3

#zad1
def fun1(nazwa, n):
    with open(nazwa) as f:
        linie = f.readlines()
        size = len(linie)
        #1
        for i in linie[:n]: print(i)
        #2
        for i in linie[-n:]: print(i)
        #3
        for i in linie[::n]: print(i)
        #4
        for i in linie: print(i.split()[n])
        #5
        for i in linie: print(i[n])

#fun1('plik0.in',1)
#zad2
def fun2(nazwa, str1, str2):
    f = open(nazwa)
    p = open('wynik2.out','w')
    linie = f.readlines()
    wyniki = []
    count = 0
    for i in linie:
        if i.find(str1) == 0: 
            count+=1
            i=i.replace(str1,str2,1)
        wyniki.append(i)
    p.writelines(wyniki)
    f.close()
    p.close()
    return count

print(fun2('plik0.in','1','a'))

#zad3
from glob import glob
def fun3(nazwy):
    s = {}
    for i in nazwy:
        with open(i) as p:
            for line in p:
                x = line.split()[0]
                y = float(line.split()[1])
                if s.get(x,0): 
                    s[x][0]+=y
                    if s[x][1] > y: s[x][1] = y
                    if s[x][2] < y: s[x][2] = y
                else: s[x] = [y,y,y]
    lista = list(s.keys())
    lista = [int(x) for x in lista]
    lista.sort()
    lista = [str(x) for x in lista]
    p = open('wynik3.out','w')
    for k in lista:
        p.write(k+' '+ str(s[k][0]/len(nazwy)) + ' ' + str(s[k][2] - s[k][1]) + '\n')
    p.close()

fun3(glob('*in'))

#zad4
def fun4(nazwy):
    p = open('plot.p','w')
    p.write("""set term jpeg\n
    set out 'wynik.jpg'\n
    set xlabel 'x'\n
    set ylabel 'y'\n
    plot """)
    for i in nazwy:
        p.write("'"+str(i)+"' u 1:2 w l t '"+str(i)+"', ")
    p.write("'wynik3.out' u 1:2 w l t 'wynik'")
    p.close()

fun4(glob('*in'))

#zad5
def fun5(nazwy):
    slowa = open(nazwy[0]).read()
    inne = ''
    for i in nazwy[1:]:
        with open(i) as p:
            inne+=p.read()
    slowa = slowa.split()
    inne = inne.split()
    temp = slowa
    wynik = []
    for i in range(len(slowa)):
        if slowa[i] in inne:
            if not slowa[i] in wynik: wynik.append(slowa[i])
    return wynik

fun5(glob('*py'))
