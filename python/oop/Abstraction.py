from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts using an ignition system.")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle starts using a starter button.")

# Creating objects
car = Car()
motorcycle = Motorcycle()

car.start()
motorcycle.start()