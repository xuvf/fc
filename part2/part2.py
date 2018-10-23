""" This module contains classes that form the basis for part 2 of the assignment

    Refer the the coursework assignment for instructions on how to complete this part.
"""
import math

class Point:
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, point):
        return math.sqrt((point.x - self.x)^2 + (point.y - self.y)^2)

class Shape:
    """This class is a convenient place to store the tolerance variable"""
    TOLERANCE = 1.0e-6

class Circle:

    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return

    def compare(self,shape):
        pass #your code here

    def envelops(self,shape):
        pass #your code here

    def equals(self, circle):
        pass #your code here

class Square:

    def __init__(self,top_left,length):
        pass #your code here

    def area(self):
        pass #your code here

    def compare(self,shape):
        pass #your code here

    def envelops(self,shape):
        pass #your code here

    def equals(self, square):
        pass #your code here

class Assignment:

    def analyse(self, filename):
        """ Process the file here """
        pass #your code here

    def shape_count(self):
        pass #your code here

    def circle_count(self):
        pass #your code here

    def square_count(self):
        pass #your code here

    def max_circle_area(self):
        pass #your code here

    def min_circle_area(self):
        pass #your code here

    def max_square_area(self):
        pass #your code here

    def min_square_area(self):
        pass #your code here

    def mean_circle_area(self):
        pass #your code here

    def mean_square_area(self):
        pass #your code here

    def std_dev_circle_area(self):
        pass #your code here

    def std_dev_square_area(self):
        pass #your code here

    def median_circle_area(self):
        pass #your code here

    def median_square_area(self):
        pass #your code here


if __name__ == "__main__":
    #You should add your own code heere to test your work
    print "=== Testing Part 2 ==="
    assignment = Assignment()
    assignment.analyse("SmallShapeTest.data")
    print(assignment.shape_count())
