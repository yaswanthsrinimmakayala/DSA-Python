#OOPS
#OOPS is a programming language that deals with objects and classes
# The main aim of OOPS is to bind the data and functions that 
# work on each other as a single unit so that no other part of code can access it

#class
#a class is a blue print for the objects 
# class is a user defined data type
# example :
# takw cars, there are different car brands and various properties
class Dog:
    pass
# the above is a example of Class of python in OOPS
# self always represent the instance
#self is not a keyword it is pointer to current object
class Cars:
    def __init__(self,name,year,color):# constructor it works at the instance of object
        self.name = name
        self.year = year
        self.color=color
        self.speed=0 # instance specific attribute
    def getinfo(self):#methods
        print("Name:",self.name)
        print("Year:",self.year)
        print("Color:",self.color)
        print("Speed:",self.speed)
    def setspeed(self,miles):
        self.speed = miles # updation in the constructor value

mycar = Cars("NissanGTR","2023","Blue") # this is the object(mycar)
mycar.getinfo() # here speed is not updated
mycar.setspeed(240) # this updates the speed
mycar.getinfo() # this shows the updation
# mc = Cars() another object
# mc.getinfo()
# results in error because the arguments are missing
# we can access the data using object.
print("What you drive? Ah...its",mycar.name,mycar.year,"Model")

class Dogs:
    attr = "mammal" # class level attribute
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("I am a ",self.name)
    def setattr(self,x):
        Dogs.attr = x  # Here updation takes place by syntax Classname.attribute
d = Dogs("GD")
d.speak()
d.setattr("It is a mammal")
print(d.attr)




# how to declare default data types for constructors
class Dogs:
    attr = "mammal" # class level attribute shared by instances
    def __init__(self,name:int):# here name is set to string these are just hints,but they are not strictly applied
        self.name = name
    def speak(self):
        print("I am a ",self.name)
    def setattr(self,x):
        Dogs.attr = x  # Here updation takes place by syntax Classname.attribute
d = Dogs("GD")
d.speak()
d.setattr("It is a mammal")
print(d.attr)
d1 = Dogs(1)  # this won't result in error because dynamic typing system at runtime
d1.speak()

################################################
# we can create methods outside of class and add it to class 

class A:
    def __init__(self,side:int):
        self.side=side

def square(self):
    print("The area of Square:",self.side*self.side)

A.square = square
# classname.Method_name=Method_name

o = A(12)
o.square()