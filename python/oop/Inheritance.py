class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

# Creating an object
my_dog = Dog()

my_dog.eat()   # Inherited method
my_dog.bark()  # Child class method