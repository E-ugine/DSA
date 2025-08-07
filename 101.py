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

"""
   

