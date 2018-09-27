# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
import statistics
import json

def diary_import(name):
    diary = json.load(open(name))
    return diary

def diary_show(diary):
    print('********show info********')
    for _ in diary['students']:
        print('name: {}\t surname: {}'.format(_['name'],_['surname']))
        print('{:<10}{:>15}{:>30}'.format('[class]','[attendance]','[grades]'))
        for k in _['classes']:
            print('{:<10}:{:>15}{:>30}'.format(k,_['classes'][k]['attendance'],str(_['classes'][k]['grade'])))
        print()

def diary_total_average(diary):
    print('********total average score********')
    temp = {}
    for _ in diary['students']:
        print('name: {}\t surname: {}'.format(_['name'],_['surname']))
        print('{:>10}'.format('[average score]'))
        l = []
        for k in _['classes']:
            l.append(statistics.mean(_['classes'][k]['grade']))
        print('{:<10.2f}'.format(statistics.mean(l)))
        tmp_name = _['name'] +' '+ _['surname']
        temp[tmp_name] = eval('{:.2f}'.format(statistics.mean(l)))
        print()
    return temp

def diary_average(diary):
    print('********average score in class********')
    temp = {}
    for _ in diary['students']:
        print('name: {}\t surname: {}'.format(_['name'],_['surname']))
        print('{:<10}{:>10}'.format('[class]','[average score]'))
        tmp_name = _['name'] +' '+ _['surname']
        temp[tmp_name] = {}
        for k in _['classes']:
            print('{:<10}{:>10.2f}'.format(k,statistics.mean(_['classes'][k]['grade'])))
            temp[tmp_name][k] = eval('{:.2f}'.format(statistics.mean(_['classes'][k]['grade'])))
        print()
    return temp

def diary_total_attendance(diary):
    print('********total attendance********')
    temp = {}
    for _ in diary['students']:
        print('name: {}\t surname: {}'.format(_['name'],_['surname']))
        print('{:<10}'.format('[attendance]'))
        l = []
        for k in _['classes']:
            l.append(_['classes'][k]['attendance'])
        print('{:<10}'.format(sum(l)))
        tmp_name = _['name'] +' '+ _['surname']
        temp[tmp_name] = sum(l)
        print()
    return temp

def diary_get_students_list(diary):
    print('********list of students********')
    temp = []
    for _ in diary['students']:
        print('name: {}\t surname: {}'.format(_['name'],_['surname']))
        tmp_name = _['name'] +' '+ _['surname']
        temp.append(tmp_name)
        print()
    return temp

def diary_get_subject(name,diary):
    print('********makig subject diary********')
    print('\n{:>30}\n'.format(name.upper()))
    print('{:<15}{:>15}{:>30}'.format('[student]','[attendance]','[grades]'))
    temp = {}
    for _ in diary['students']:
        if name in _['classes']:
            tmp_name = _['name'] +' '+ _['surname']
            temp[tmp_name]={}
            temp[tmp_name]['attendance'] = _['classes'][name]['attendance']
            temp[tmp_name]['grade'] = _['classes'][name]['grade'][:]
            print('{:<15}{:>15}{:>30}'.format(tmp_name,temp[tmp_name]['attendance'],str(temp[tmp_name]['grade'])))
    return temp

if __name__ == '__main__':
    diary = diary_import('diary.json')
    diary_show(diary)
    average_dict = diary_average(diary)
    tot_average_dict = diary_total_average(diary)
    attendance_dict = diary_total_attendance(diary)
    students_list = diary_get_students_list(diary)
    maths_diary = diary_get_subject('maths',diary)
    ######you get dictionaries/lists for interpreter interaction
    print('******************dictionaries for interpreter interaction*****************')
    print(average_dict)
    print(tot_average_dict)
    print(attendance_dict)
    print(students_list)
    print(maths_diary)