
###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

from plane import Plane
from environment import Environment
from multiprocessing import Process

if __name__ == "__main__":
    boeing_737=Plane('Seattle','San Diego')
    airbus_A380=Plane('El Paso','Phoenix')
    airbus_A330=Plane('Detroit','Washington')
    env=Environment()
    env.add_plane(boeing_737,'Boeing 737')
    env.add_plane(airbus_A380,'Airbus A380')
    env.add_plane(airbus_A330,'Airbus A330')
    for k in env.planes.keys():
        env.plane_orientation(k)
    print("\n\n")
    for k in env.planes.keys():
        p=Process(target = env.show_info,args=(k,))
        p.start()
        p.join()

