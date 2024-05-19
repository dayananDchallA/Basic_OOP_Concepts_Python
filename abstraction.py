'''
Abstraction is the concept of showing only the necessary information to the outside world while hiding unnecessary details.

Abstraction helps to simplify complex systems and focus on the essential features.

In Python, you can achieve abstraction using abstract base classes (ABC) and abstract methods.

Let’s say we have an abstract base class called Shape. The Shape class is marked as an abstract class by inheriting from the ABC class (Abstract Base Class).

Inside the Shape class, we define an abstract method called area() using the @abstractmethod decorator.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self)-> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self)-> float:
        return 3.14 * (self.radius ** 2)
    

# The Rectangle and Circle classes inherit from the Shape class.
# They provide their own implementations of the area() method specific to their shapes. 
# Note that the implementation details are hidden from the outside world, and only the interface defined by the abstract class is exposed.