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
"""



 


    