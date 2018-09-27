#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr1.py
#
#Delete these comments before commit!
#Good luck.

from matrix import Matrix

if __name__ == "__main__":

    matrix_square_ascending = Matrix(1,2,3,4)
    matrix_square = Matrix(2,2,2,2)
    matrix_cubic_ascending = Matrix(1,2,3,4,5,6,7,8,9)
    matrix_cubic = Matrix(1,1,1,1,1,1,1,1,1)

    print("Add:")
    print(matrix_cubic_ascending)
    print(matrix_cubic)
    print("Result:")
    matrix_added = matrix_cubic_ascending.add(matrix_cubic)
    print(matrix_added)
    print("------------------------\n")

    print("Subtract:")
    print(matrix_square_ascending)
    print(matrix_square)
    print("Result:")
    matrix_subtracted = matrix_square_ascending.subtract(matrix_square)
    print(matrix_subtracted)
    print("------------------------\n")

    print("Dummy multiply:")
    print(matrix_square_ascending)
    print(matrix_square)
    print("Result:")
    matrix_dummy_multiplied = matrix_square_ascending.dummy_multiply(matrix_square)
    print(matrix_dummy_multiplied)
    print("------------------------\n")

    print("Multiply:")
    print(matrix_square_ascending)
    print(matrix_square)
    print("Result:")
    matrix_multiplied = matrix_square_ascending.multiply(matrix_square)
    print(matrix_multiplied)
    print("------------------------\n")

    print("Add 1:")
    print(matrix_cubic_ascending)
    print("Result:")
    matrix_cubic_ascending.add_one()
    print(matrix_cubic_ascending)
    print("------------------------\n")

    print("Subtract 1:")
    print(matrix_cubic)
    print("Result:")
    matrix_cubic.subtract_one()
    print(matrix_cubic)
    print("------------------------\n")
    
    print("Double:")
    print(matrix_square_ascending)
    print("Result:")
    matrix_square_ascending.double_matrix()
    print(matrix_square_ascending)
    print("------------------------\n")
