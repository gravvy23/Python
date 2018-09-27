import random

class Plane:

    def __init__(self,origin = "Empty", destination = "Empty"):
        self.angle = 0.0
        self.tilt_corr_counter = 0
        self.origin = origin
        self.destination = destination
        self.stop_iteration = None
        self.max_angle = 15
        self.min_angle = -15

    def random_angle(self):
        self.angle += (random.random()*10-5)

    def tilt_correction(self):
        print("Tilt correction applied :: angle = 0 deg")
        self.angle = 0
        self.tilt_corr_counter+=1

    def get_angle(self):
        return self.angle

    def __iter__(self):
        return self


    def __next__(self):
        if self.stop_iteration == 'q':
            raise StopIteration
        return self.angle