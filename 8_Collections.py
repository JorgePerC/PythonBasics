#List, Arrays, Diccionaries

#LISTS
#A list is a collection of items
#Store different types of data values
#Store any kind of data type
#Has an index
#Storage order guaranteed
lista = ["Chris", "Susan"]
print(lista)
#Empty lists
listas = []
listas.append(98) #Add new item
listas.append(100)
print(listas)
print(listas[0])

#ARRAYS
#All data must be of the same kind
#You can only sotre simple types of data
#Has an index
#Storage order guaranteed
from array import array
scores = array("d") #What does "d" means???. It means Diggits
scores.append(97) #Add new item
scores.append(109)
print(scores)
print(scores[1])


#Common methods
print(len(scores))#How to get the LENGTH 
scores.insert(0, 10) #Inssert before Index
print(scores)
lista.insert(0, "Jorge")
print(lista)
lista.sort() 
print(lista)
print(scores)

#Retrieve ranges
names = ["Susan", "Chris", "Bill"]
present = names[0:2] #Returns two items. 
#The first parramter tells you where to start. The second one how many items to show
print(names)
print(present)


#DICCIONARIES
#Its similar to JSON7
#Pairs by key/value
#The items order is not guaratee
dic = {"primero": "Christopher"}
dic["last"] = "Harrison"
print(dic)
print(dic["primero"])

