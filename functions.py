"""
def my_function(param):
    print("Running my_function")
    return param + 1

def greet_programmer():
    return "Hello Programmer"

print(greet_programmer())

def greet(name):
    return f"Hello {name}"
print(greet("Eugine"))

def greet_with_default(name=None):
    if name:
        return f"Hello {name}!"
    else:
        return "Hello programmer!"

print(greet_with_default())

def add(a,b):
    return a + b
print(add(2,3))


def add(a,b):
    return f"{a} + {b} = {a+b}"

print(add(2,3))

def add(*args): # *args packs the arguments into a tuple(also known as arbitrary arguments)
    return sum(args)
print(add(20,30,40))

    
"""











   
     