'''
A class is a blueprint or template that defines the properties and behavior of an object. An Object is an instances of a class, created using the class definition.

Here's an example of a class definition in Python:

'''
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        print(f"The {self.make} {self.model}'s engine is starting")



# In this example, the Car class is a blueprint that defines the properties of a car.
toyota_car = Car("Toyota", "Corolla", 2020)
toyota_car.start_engine()

chevrolet_car = Car("Chevrolet", "Camaro", 2022)
chevrolet_car.start_engine()

# We create two objects, toyota_car and chevrolet_car which are instances of the Car class. 
# Both car objects can invoke start_engine() method using their own values for the make, model and year properties.