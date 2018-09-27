import sys

class Environment:

    def __init__(self):
        self.planes = {}
        self.number_of_planes = 0

    def add_plane(self,plane,name):
        self.planes[name]=plane

    def turbulations(self,name):
        temp = self.planes[name].get_angle()
        self.planes[name].random_angle()
        if self.planes[name].get_angle() > self.planes[name].max_angle:
            print('Crash Alert! Tilt correction needed immediately! :: angle = {} deg'.format(self.planes[name].max_angle))
            self.planes[name].tilt_correction()
        elif self.planes[name].get_angle() < self.planes[name].min_angle:
            print('Crash Alert! Tilt correction needed immediately!:: angle = {} deg'.format(self.planes[name].min_angle))
            self.planes[name].tilt_correction()

    def get_angle(self,name):
        return self.planes[name].get_angle()


    def plane_orientation(self,name):
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print("\n\nPlane {} takes off".format(name))
        print("Press 'q' to quit")
        for i in self.planes[name]:
            self.turbulations(name)
            self.planes[name].stop_iteration = input()
            print('\t\t{0}{1}Currenct orientation is: {2:03.2f}'.format(CURSOR_UP_ONE,ERASE_LINE,i),end='\r')

    def show_info(self,name):
        print("Plane '{}'".format(name))
        print("::from {}\n::to {}".format(self.planes[name].origin,self.planes[name].destination))
        print(":::current orientation: {0:02.3f} deg".format(self.planes[name].get_angle()))
        print(":::Number of tilt corrections: {}\n".format(self.planes[name].tilt_corr_counter))