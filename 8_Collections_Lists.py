# LISTS
# A list is a collection of items
# Store different types of data values
# Store any kind of data type
# Has an index
# Storage order guaranteed
lista = ["Chris", "Susan"]
print(lista)
# Empty lists
listas = []

listas.append(98) # Add new item
listas.append(100)
print(listas)
print(listas[0])
print(len(listas))# How to get the LENGTH 

# You can also give values to variables
nombre1, nombre2 = lista

lista.insert(0, "Jorge")
print(lista)

lista.sort() # This doesn't has a return type
print(lista)

lista.reverse() #Tampoco tiene un return type
print(lista)

# Retrieve ranges
# Aka SLICING
names = ["Susan", "Chris", "Bill"]
present = names[0:2] # Returns two items. 
# The first parramter tells you where to start. The second one how many items to show
# Actually that's not exactly correct. rather is (begin: end), where end is exclusive
# You can also do:
present2 = names[3:] # From 3 to end
present3 = names[:3] # From beggining to 3 (exclusive)
#Not only that, but you can and a stel [beging:end:step]
print(names)
print(present)
print(present2)
print(present3)

# You can also use negatives index
present4 = names[-1] # This is the last item
print(present4)
# However, you can only use its negative length as the max
# mininum value -1, 'cause 0


# Lists comprenhensions:
lista2 = []
for letra in "LoveUrSelf":
    lista2.append(letra)

    # That can be converted into: 
lista3 = [letra for letra in "HolaMundo"]
        # Element to be inserted. 
        # We can actually modify this element on the run
print(lista3)
        # Even if statements!!!
lista4 = [x for x in range (11) if x%2 == 0]
print(lista4)

lista5 = [number**2 for number in lista4]
print(lista5)

        # God, event nested loops
lista6 = [ x*y for x in lista4 for y in lista5]
print(lista6)