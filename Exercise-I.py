'''
Sanjay Chandrasekar
Exercise I
Spring 2021
'''

#Part One - Basic Inheritance - Circle & Cylinder
import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        area = self.radius * self.radius * math.pi
        return area

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
        
    def getVolume(self):
        volume = super().getArea() * self.height
        return volume

c1 = Circle(4)
area = c1.getArea()
print("Circle Area:", str("%.2f" % area))


c2 = Cylinder(2, 5)
volume = c2.getVolume()
print("Cylinder Volume:", str("%.2f" % volume))

'''
Execution Results:
Circle Area: 50.27
Cylinder Volume: 62.83
'''