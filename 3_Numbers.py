#How to declare them
var = 3.5
var2 = 10

#Operations
print(var+var2)
print(var-var2)
print(var*var2)
print(var/var2)
print(var%var2)
print(var**var2) #For power
print(var//var2) #For integer only

#Tho, you can't concatenate Strings with errors. Therefore
print ("Number: " + str(var2))

#When asking for inputs, you can do this:
var3 = input("Dame un número: ")
var4 = input("Dame otro número: ")
#   That returns two strings, so you can't do math with them
print("Me diste el número ")
print(int(var3)+int(var4))
print(float(var3)+float(var4))
