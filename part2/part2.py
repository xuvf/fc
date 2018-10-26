""" This module contains classes that form the basis for part 2 of the assignment

    Refer the the coursework assignment for instructions on how to complete this part.
"""
import math

class Point:
    __x = 0.0
    __y = 0.0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def equals(self,point):
        return self.__x == point.getX() and self.__y == point.getY()

    def distance(self, point):
        return math.sqrt((point.getX() - self.__x)**2 + (point.getY() - self.__y)**2)

class Shape:
    """This class is a convenient place to store the tolerance variable"""
    TOLERANCE = 1.0e-6

class Circle:
    __centre = Point(0,0)
    __radius = 0

    def __init__(self,centre,radius):
        self.__centre = centre
        self.__radius = radius

    def __str__(self):
        return "This circle has its centre at (%s,%s) and a radius of %s." % (self.__centre.getX(),self.__centre.getY(),self.__radius)

    def setCentre(self,centre):
        self.__centre = centre

    def setRadius(self,radius):
        self.__radius = radius

    def getCentre(self):
        return self.__centre

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi*(self.__radius**2)

    def compare(self,shape):
        if self.area() < shape.area() :
            return -1
        elif self.area() == shape.area() :
            return 0
        elif self.area() > shape.area() :
            return 1

    def envelops(self,shape):
        if type(shape) == Circle :
            if  self.__radius - shape.getRadius() >= self.__centre.distance(shape.getCentre()):
                return True
            else :
                return False
        else:
            top_leftX = shape.getTopLeft().getX()
            top_leftY = shape.getTopLeft().getY()
            length = shape.getLength()
            disList = [shape.getTopLeft(),Point(top_leftX + length, top_leftY),Point(top_leftX,top_leftY-length),Point(top_leftX+length,top_leftY-length)]
            disList = list(map(lambda x : x.distance(self.__centre) >= self.__radius, disList))
            if True in disList:
                return False
            else:
                return True

    def equals(self, circle):
        return self.__centre == circle.getCentre() and self.__radius == circle.getRadius()

class Square:
    __top_left = Point(0,0)
    __length = 0

    def __init__(self,top_left,length):
        self.__top_left = top_left
        self.__length = length

    def __str__(self):
        return "This square’s top left corner is at (%s,%s) and the side length is %s ." % (self.__top_left.getX(),self.__top_left.getY(),self.__length)

    def setTopLeft(self,top_left):
        self.__top_left = top_left

    def setLength(self,length):
        self.__length = length

    def getTopLeft(self):
        return self.__top_left

    def getLength(self):
        return self.__length

    def area(self):
        return self.__length**2

    def compare(self,shape):
        if self.area() < shape.area() :
            return -1
        elif self.area() == shape.area() :
            return 0
        elif self.area() > shape.area() :
            return 1

    def envelops(self,shape):
        top_leftX = self.__top_left.getX()
        top_leftY = self.__top_left.getY()
        length = self.__length

        if type(shape) == Circle:
            disList = [self.__top_left,Point(top_leftX + length, top_leftY),Point(top_leftX,top_leftY-length),Point(top_leftX+length,top_leftY-length)]
            disList = list(map(lambda x : x.distance(shape.getCentre()) >= shape.getRadius(), disList))
            if False in disList:
                return False
            else:
                return True
        else:
            return top_leftX <= shape.getTopLeft().getX() and top_leftY >= shape.getTopLeft().getY() and top_leftX + length >= shape.getTopLeft().getX() + shape.getLength() and top_leftY <= shape.getTopLeft().getY() + shape.getLength()


    def equals(self, square):
        return self.__top_left == square.getTopLeft() and self.__length == square.getLength()

class Assignment:
    __circleList = []
    __squareList = []

    def analyse(self, filename):
        f = open(filename,"r")
        data = []
        for line in f :
            data = line.replace("\n","").split(" ")
            if (data[0] == "circle" and data[3] != 0):
                self.__circleList.append(Circle(Point(float(data[1]),float(data[2])),float(data[3])))
            elif (data[0] == "square" and data[3] != 0):
                self.__squareList.append(Square(Point(float(data[1]),float(data[2])),float(data[3])))

    def shape_count(self):
        return len(self.__circleList)+len(self.__squareList)

    def circle_count(self):
        return len(self.__circleList)

    def square_count(self):
        return len(self.__squareList)

    def max_circle_area(self):
        return max(map(lambda x : x.area(), self.__circleList))

    def min_circle_area(self):
        return min(map(lambda x : x.area(), self.__circleList))

    def max_square_area(self):
        return max(map(lambda x : x.area(), self.__squareList))

    def min_square_area(self):
        return min(map(lambda x : x.area(), self.__squareList))

    def mean_circle_area(self):
        return sum(map(lambda x : x.area(), self.__circleList))/len(self.__circleList)

    def mean_square_area(self):
        return sum(map(lambda x : x.area(), self.__squareList))/len(self.__squareList)

    def std_dev_circle_area(self):
        return math.sqrt(sum(map(lambda x : (x.area() - self.mean_circle_area())**2, self.__circleList))/self.circle_count())

    def std_dev_square_area(self):
        return math.sqrt(sum(map(lambda x : (x.area() - self.mean_square_area())**2, self.__squareList))/self.square_count())

    def median_circle_area(self):
        circleList = list(map(lambda x : x.area(), self.__circleList))
        circleList.sort()
        if len(circleList) % 2:
            return circleList[int((len(circleList)-1)/2)]
        else:
            return (circleList[int(len(circleList)/2 - 1)] + circleList[int(len(circleList)/2)])/2

    def median_square_area(self):
        squareList = list(map(lambda x : x.area(), self.__squareList))
        squareList.sort()
        if len(squareList) % 2:
            return squareList[int((len(squareList)-1)/2)]
        else:
            return (squareList[int(len(squareList)/2 - 1)] + squareList[int(len(squareList)/2)])/2


if __name__ == "__main__":
    #You should add your own code heere to test your work
    print ("=== Testing Part 2 ===")
    #centre = Point(2,1)
    #top_left = Point(-1,1)
    #square1 = Square(centre,1)
    #square2 = Square(top_left,2)
    #print(square2.envelops(square1))
    #print(circle1.area())
    assignment = Assignment()
    #assignment.analyse("1000shapetest.data")
    assignment.analyse("smallshapetest.data")
    #assignment.analyse("test.data")
    print(assignment.std_dev_circle_area())
