'''racist, self-organising dots. Move randomly with each iteration to happier places according to a happiness rule, iterating until all are happy'''
import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot as plt
import numpy as np

class dot(object):
    '''a dot is an agent in Schellings model. Dots are big if unhappy and small if happy'''
    def __init__(self, colour, location, racism=5, closeness=2):
        ''', low closeness is ok with loneliness'''
        if colour in ["red", "blue"]:
            self.colour = colour
        elif colour == 1:
            self.colour = "red"
        elif colour == 2:
            self.colour = "blue"
        else:
            raise AttributeError('red or blue only')
        self.location = location
        self.search_space = 10
        self.racism = self.search_space-racism
        self.closeness = closeness

    def dist(self, dot):
        return np.sqrt((self.location[0]-dot.location[0])**2+(self.location[1]-dot.location[1])**2)

    def nearest(self, number, field):
        def get_key(item):
            return item[0]
        return np.array(sorted(np.array([[self.dist(dot), dot] for dot in field.dots]), key=get_key))[:number, 1]

    def happy(self, field, closeness_tol=0.7):
        '''dots are colour_happy if their nearest self.search_space neighbours are similar enough to them. Dots are close_happy if there are enough close dots where closeness is an arg'''
        closest_ten_dots = self.nearest(self.search_space, field)
        # length of list of dots amongst the self.search_space closest with different colours is less than dot racism
        colour_happy = len(list(filter(None, [dot.colour != self.colour for dot in closest_ten_dots]))) < self.racism
        # length of list of dots amongst the ten closest that are very close is greater than dot closeness
        close_happy = len(list(filter(None, [self.dist(dot) < closeness_tol for dot in closest_ten_dots]))) > self.closeness
        return close_happy and colour_happy

    def move(self, location):
        self.location = location

class Field(object):
    '''a field is a frame of n dots of chosen colour and location'''
    def __init__(self, n_dots):
        self.dots = [dot(random.randint(1, 2), self.randloc()) for i in range(n_dots)]

    def randloc(self):
        '''different distributions give different behaviours'''
        return [10*np.random.rand(), 10*np.random.rand()]

    def show(self):
        x = [self.dots[i].location[0] for i in range(len(self.dots))]
        y = [self.dots[i].location[1] for i in range(len(self.dots))]
        if self.dots[0].racism != self.dots[0].search_space:
            colours = [self.dots[i].colour for i in range(len(self.dots))]
        else:
            colours = ["black" for i in range(len(self.dots))]
        sizes = [7**2 if dot.happy(self) else 10**2 for dot in self.dots]
        plt.scatter(x, y, c=colours, s=sizes)
        plt.show()

    def scramble(self):
        for dot in self.dots:
            while not dot.happy(self):
                dot.move(self.randloc())

    def segregate(self, max_iters=10):
        for i in range(max_iters):
            field.show()
            if np.all([[dot.happy(self) for dot in self.dots]]):
                return 0
            else:
                field.scramble()
        raise IndexError('List has not converged after iterations')


field = Field(500)
field.segregate()
