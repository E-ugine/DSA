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

What it hides: Implementation details.

Focus: What a class/object can do.

How it’s done: Using abstract classes, interfaces, or methods that only define behavior but don’t explain how it’s achieved.

Goal: To provide a clear, simple, high-level blueprint for interaction.

#Encapsulation
# Hiding internal data/details of a class and only exposing what's necessary.
# It helps protecting important data from being changed directly and keeps code secure and organized.
#What it hides: Internal state/data (variables).

#Focus: How data is accessed and modified.

#How it’s done: By making variables private or protected and controlling access through getter/setter methods or properties.

#Goal: To protect data from direct, unsafe manipulation.

#Public (name) → can be accessed from anywhere.

#Protected (_name) → should not be accessed directly outside the class (just a convention).

#Private (__name) → name-mangled by Python to make direct access harder.

class BankAccount():
    def __init__(self,owner, balance):
        self.owner = owner # public attribute
        self._balance = balance # protected attribute
        self.__pin = 1234 # private attribute
        
    def deposit(self,amount):
        self._balance += amount
        return f"Deposited {amount}. New balance {self._balance}"
    
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrew {amount}. Remaining balance is {self._balance}"
            else:
                return f"Insufficient funds"
        else:
            return f"Incorrect PIN"
        
account = BankAccount("Eugine", 135000)

print(account.deposit(500))
print(account.withdraw(20000,124))
print(account._balance)
print(account._BankAccount__pin)
"""










    




 


    