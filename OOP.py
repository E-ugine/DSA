"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The employee is {self.name} and he's {self.age} years young"    

emp1 = Employee("Madmax", 30)
emp2 = Employee("King", 40)

print(emp1)
"""

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
    