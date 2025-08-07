"""string = "I enjoy programming in Python."
print("programming" in string)

fruit = "Banana"
for x in fruit:
    print(x)

    #Python slicing
Greeting = "Good Morning"
print(Greeting[3:5])

text = "WE're the so called \"AI\" programmers"
print(text)

text = "eugine is dope"
print(text.capitalize())

myList = ["apple", "banana", "cherry"]
myList.insert(2,"pie")
print(myList)

myList = ["apple", "banana", "cherry"]
myList.append("pie")
print(myList)

myList = ["apple", "banana", "cherry"]
hisList = ["orange", "kiwi", "melon"]
myList.extend(hisList)
print(myList)

myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
for i in range(len(myList)):
    print(myList[i])

#List Comprehensio
Teams = ["Man Utd", "Chelsea", "Arsenal", "Liverpool", "Tottenham"]
newTeams = [x for x in Teams if "l" in x]
print(newTeams) 

myList = ["Eugine", "Owuor", "Agolla"]
myList.sort()
print(myList)
myList = [10,3,45,8,56]
myList.sort(reverse=True) # sorts in descending order
print(myList)

fruits = ["Orange", "Mango","banana","pie"]
fruits.sort(key=str.lower) # This is because sort function is case sensitive
print(fruits)

thisList = ["Football", "Rugby", "F1","Handball", "Kabadii"]
myList= thisList.copy()
print(myList)

thisList = ["Football", "Rugby", "F1","Handball", "Kabadii"]
myList = ["F1"]
for x in thisList:
    myList.append(x) #
print(myList)

thisList = ["Football", "Rugby", "F1","Handball", "Kabadii"]
myList = ["F1"]
myList.extend(thisList)
print(myList)

#Sets
myset = set(("This","That","Those"))
print(myset)

mySet = {1,2,3}
hisSet = {4,5,6}
ourSet = mySet.union(hisSet)
print(ourSet)

mySet = {1,2,3}
hisSet = {4,5,6}
ourSet = mySet | hisSet
print(ourSet)

# dictionaries
myDict = {
    "make": "Audi",
    "model": "Audi Q3",
    "price": 2377999
}

print(myDict)
print(myDict["model"])

myDict = {
    "make": "Audi",
    "model": "Audi Q3",
    "price": 2377999
}

for x in myDict:
    print(x)
    print(myDict[x])

myDict = {
    "make": "Audi",
    "model": "Audi Q3",
    "price": 2377999
}

for x,y in myDict.items():
    print(x,y) 
car1 = {
     "make": "Audi",
    "model": "Audi Q3",
    "price": 2377999
}

car2 = {
     "make": "Audi",
    "model": "Audi A5",
    "price": 1377999
}

car3 = {
     "make": "Audi",
    "model": "Audi Q5",
    "price": 3377999
}

myCars = {
    "car1": car1,
    "car2": car2,
    "car3": car3
}

#print(myCars)
#print(myCars["car2"] ["model"])

#Loop through

for key, value in myCars.items():
    print(key)
    for key, value in value.items():
        print(f" {key}: {value} ")       

"""








   

