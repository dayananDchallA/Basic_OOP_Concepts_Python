'''
Inheritance is a mechanism that allows a class to inherit properties and methods from another class, called the superclass or parent class.

The class that inherits is called the subclass or child class.

The child class inherits all the fields and methods of the parent class and can also add new fields and methods or override the ones inherited from the parent class.

Inheritance promotes code reuse and helps create a hierarchical structure.

Let’s say we have a parent Vehicle class with a method named honk().
'''


# Define a parent class called vehicle
class Vehicle:
    def __init__(self, color: str) -> None:
        self.color = color

    def honk(self) -> None:
        print("Honk honk!")


# Define a child class called "Car" that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, color: str, speed: float) -> None:
        super().__init__(color)
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self) -> None:
        print("Accelerating...")
        self.speed += 10

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2020, "red", 60)
my_car.honk() # Output: Honk honk!
my_car.accelerate()


# The Car class inherits the color attribute and the honk method from the Vehicle class promoting code reuse. 
# The Car class also adds its own attributes and methods, such as speed and accelerate.