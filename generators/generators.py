from random import randint
#################################
#zad1

def gen1():
    a,b = 0,1
    while True:
        yield a+b
        a,b = b,a+b

def gen2(sekw, parametr = 1):
    i=0
    for x in sekw:
        if parametr:
            if not i%2:
                yield x
        else:
            if i%2:
                yield x
        i=i+1

def gen3(sekw, parametr):
    for x in sekw:
        if x<=parametr: yield x
        else: break

print(sum(list(gen3(gen2(gen1()),100))))
print(sum(list(gen3(gen2(gen1(),0),100))))
#################################
#zad2

def my_rrange(stop, start = 0, step = 0.1):
    x = start
    while x<stop:
        yield x
        x=x+step

#for i in my_rrange(2):
#    print(i)

#################################
#zad3
def gen4(value):
    tmp = value
    yield tmp
    while tmp > 0.1:
        my_rand = randint(-100,100)/100
        if abs(my_rand) > 0.4:
            tmp = tmp + my_rand
            yield tmp


#for i in gen4(2):
#    print('{:.2f}'.format(i))

#################################
#zad4
binary = [randint(0,1) for i in range(30)]
print(binary)

def gen5(sekwencja):
    flag = True
    for i in range(len(sekwencja)):
        if sekwencja[i]:
            count = 0
            for j in sekwencja[i+1:]:
                if not j: count=count+1
                else:
                    yield count
                    break

l=[i for i in gen5(binary)]
print(sum(l)/len(l))

#################################
#zad5
def gen6(kwota, nom):
    C = [_ for _ in range(kwota+1)]
    for i in range(len(nom)):
        for j in range(kwota+1):
            if nom[i]>j:
                C[j] = C[j]
            else:
                C[j] = min(C[j], 1+C[j-nom[i]])
        yield C[kwota]

nominaly = [2,5,10,20,50,100]
for i in gen6(234,nominaly):
    print(i)