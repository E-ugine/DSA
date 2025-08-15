"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The employee is {self.name} and he's {self.age} years young"    

emp1 = Employee("Madmax", 30)
emp2 = Employee("King", 40)

class Dog:
    species = "Canis familiaris" #class attribute, shared by all dogs

    def __init__(self,name,age):
        self.name = name
        self.age = age

        #This is the instance method
    def description(self):
            return f"{self.name} is {self.age}"
        
        #Another instance method
    def speak(self,sound):
            return f"{self.name} says {self.sound} "
#instantiating the dog class        
Scooby = Dog("Scooby", 12)
print(Scooby.description())

print(emp1)

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        print(f"The {self.color} car has {self.mileage} miles")    

blueCar = Car("blue", 20000)  
redCar = Car("red",30000)
blueCar.description()
redCar.description() 




# Polymorphism ~ Existing in many forms
# You have a universal command(method) that works on many forms. 
#For instance, here dog and cat both have a .speak() method but returns different sounds

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Real-World Analogy. Think about the “pay” action at checkout:
#Credit Card → swipes card
#Mobile Pay → scans QR
#Cash → hands over notes
#The action name ("pay") is the same, but each method is implemented differently.
# Polymorphism with Inheritance

class Car():
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class PetrolCar(Car):
    def start_engine(self):
        return "Staring petrol engine....Vrroom!!!" 

class ElectricCar(Car):
    def start_engine(self):
        return "Starting Electric engine ....Whirrr!!!1"

cars = [PetrolCar(), ElectricCar()]
for car in cars:
    print(car.start_engine())             

    
# Abstraction ~ Hiding unnecessary details and showing only what's important
# Likw driving a car without having to know how the engine  combusts fuel

#A smartphone is a great real-life example of data abstraction 
#you can make calls or take photos without knowing how signals or storage work. 
#Only essential features are shown, complex details are hidden.

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass # abstract method

class English(Greet):
    def say_hello(self):
        return "Hello" 

greeting = English()
print(greeting.say_hello())           
"""






    




 


    