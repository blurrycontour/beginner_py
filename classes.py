class Car:
    'This is my class'
    carCount = 0

    def __init__(self,name,color):
        self.name = name
        self.color = color
        Car.carCount += 1
    
    def getCount(self):
        print("Total number of cars : %d"%(Car.carCount))
    
    def getInfo(self):
        print("Name : ",self.name,"\nColor : ",self.color)

car1 = Car("Ford","Red")    #create an instance
car1.year = 1995    #create new attribute

if hasattr(car1,'year') :
    print(getattr(car1,'color'))

print("###################################################################")

class Point:
    def  __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name , "destroyed")

pt1 = Point(1,2)    #reference of an object Point(1,2)
pt1 = Point(4,8)
pt1 = Point(3,7)
pt2 = Point(2,1)
pt3 = pt2

print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

print("###################################################################")

class Parent:
    parentAttr = 100
    
    def __init__(self):
        print("Parent Constructor !")
    def Method(self,attr):
        print("Parent Method !")
    def setAttr(self,attr):
        self.parentAttr = attr
    def getAttr(self):
        print("Parent Attribute : ",self.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Child Constructor !")
    def Method(self):   #Method Overriding
        print("Child Method !")

child = Child()
child.setAttr(150)
child.getAttr()
child.Method()
print(child)    #depends on __str__ method in class
#issubclass() or isinstance()

print("###################################################################")

#Operator Overloading & Private Members
class Vector:
    __secretData = 10

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return "Vector (%d, %d, %d)"%(self.a,self.b,self.c)
    def __add__(self,other):    #Operator Overloading
        return Vector(self.a+other.a,self.b+other.b,self.c+other.c)
    def getSecret(self):
        return self.__secretData
 
v1 = Vector(1,2,3)
v2 = Vector(-2,1,7)

print(v1 + v2)
print(v1.getSecret())