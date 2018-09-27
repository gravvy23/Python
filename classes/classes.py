#!/usr/bin/env python3
import abc


#zad 1
class Calka(abc.ABC):
    def __init__(self,start,stop,steps,fun):
        if start > stop or steps < 0:
            raise ValueError

        self.start = start
        self.stop = stop
        self.steps = steps
        self.fun = fun

    @abc.abstractmethod
    def calculate(self):
        '''metoda abstrakcyjna obliczajaca calke roznymi metodami'''
        pass

class CalkaTrapez(Calka):
    def __init__(self,start,stop,steps,fun):
        super().__init__(start,stop,steps,fun)

    def calculate(self):
        suma = 0
        h = ( self.stop - self.start)/self.steps
        for i in range(self.steps):
            suma+=self.fun(self.start + i*h)
            suma+=self.fun(self.start + (i+1)*h)
        return suma*h/2


class CalkaSimpson(Calka):
    def __init__(self,start,stop,steps,fun):
        super().__init__(start,stop,steps,fun)

    def calculate(self):
        suma_parzysta = 0
        suma_nieparzysta = 0
        h = (self.stop - self.start)/(2*self.steps)
        for i in range(1,2*self.steps):
            if i%2:
                suma_nieparzysta+=self.fun(self.start+i*h)
            else:
                suma_parzysta+=self.fun(self.start + i*h)
        suma = self.fun(self.start) + 4*suma_nieparzysta + 2*suma_parzysta + self.fun(self.stop)
        return suma*h/3

def fun(x):
    return x**3

try:
    trapez = CalkaTrapez(0,10,1000,fun)
    simpson = CalkaSimpson(0,10,1000,fun)
except:
    print('zle argumenty')
print(trapez.calculate())
print(simpson.calculate())


#zad 2
class MyStack:
    def __init__(self, other = None):
        self.stack = []
        if other:
            self.stack += other.stack

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop(-1)

    def push_stack(self, other):
        self.stack += other.stack

    def len(self):
        return len(self.stack)

    def __str__(self):
        my_string = ''
        for i in self.stack[:-1]:
            my_string += str(i) + ' -> '
        my_string += str(self.stack[-1])
        return my_string

class MySortedStack(MyStack):
    def __init__(self, other = None):
        super().__init__(other)
        self.stack.sort()

    def push(self, val):
        if self.stack:
            if val > self.stack[-1]:
                self.stack.append(val)
        else:
            self.stack.append(val)

    def push_stack(self, other):
        if self.stack:
            if sorted(other.stack) == other.stack and other.stack[0] > self.stack[-1]:
                self.stack += other.stack
        else:
            self.stack = other.stack[:]


mystack = MyStack()
mystack.push(1)
mystack.push(-23)
mystack.push(4)
mystack.push(12)
mystack.push(3)
print(mystack)
sortedstack = MySortedStack(mystack)
print(sortedstack)
sortedstack.push(2)
print(sortedstack)
sortedstack.push(100)
print(sortedstack)

from random import randint

suma = 0
print('*************sredni rozmiar stosu****************')
for i in range(100):
    tempstack = MySortedStack()
    for j in range(100):
        tempstack.push(randint(0,100))
    suma += tempstack.len()
print(suma/100)
print('*************************************************')
#zad 3
class FileCounter:
    data = {}

    def __init__(self, name):
        self.name = name

    def count(self):
        file = open(self.name,'r')
        lines = file.readlines()
        self.lines = len(lines)
        self.words = 0
        self.chars = 0
        for line in lines:
            words = line.split(' ')
            self.words += len(words)
            for word in words:
                self.chars+= len(word)
            self.chars -= 2
        FileCounter.data[self.name] = {
            'lines' : self.lines,
            'words' : self.words,
            'chars' : self.chars
        }
        print('{} {} {} {}'.format(self.lines, self.words, self.chars, self.name))

    @staticmethod
    def static_count():
        total_lines = 0
        total_words = 0
        total_chars = 0
        for key in FileCounter.data :
            total_lines += FileCounter.data[key]['lines']
            total_words += FileCounter.data[key]['words']
            total_chars += FileCounter.data[key]['chars']
            print('{0:5} {1:5} {2:5} {3:}'.format(FileCounter.data[key]['lines'],FileCounter.data[key]['words'],FileCounter.data[key]['chars'],key))
        print('{0:5} {1:5} {2:5} {3:}'.format(total_lines , total_words , total_chars , 'total'))

fc1 = FileCounter('p1.txt')
fc1.count()
fc2 = FileCounter('p2.txt')
fc2.count()
print('***************static_function********************')
FileCounter.static_count()
