# There is only two types, for and whiles
# IT IS NOT A GOOD IDEA TO:
# Modify a list while iteratin on it

lista = ["Chris", "Susan", "Jorge", "Daniela", "Karina"]

# This is to have a variable
for y in range (0,10,+1):
    print(y)
print()

# In this case, item represent the value on the list
for item in lista:
    print(item)

    
print()
i = 0
while i<len(lista):
    print(lista[i])
    i+=1