from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("Dog barks!") 
        
class Cat(Animal):

    def sound(self):
        print("Cat meows!")
        
    def cat_sound(self):
        print("Cat meows!")
        

# d = Dog()   
# d.sound()

# c = Cat()
# c.cat_sound() 

# abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2
    
    def circumference(self):
        return 3.14 * 2 * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)

print(f"Circle Area: {c.area()}")
print(f"Rectangle Area: {r.area()}")
print(f"Circumference of circle: {c.circumference()}")
    