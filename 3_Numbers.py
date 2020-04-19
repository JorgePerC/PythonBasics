#How to declare them
var = 3.5
var2 = 10

# Para declarar dos variables en una misma linea
valor1, valor2 = 1,3
# Igual se pueden mezlar los tipos de datos:
num, string = 2, "hola"

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

# Otros valores:
binary = int('101001011', 2) # De Binario a Decimal
print(binary) # Resultado: 331
hexa = int('A47F2', 16) # De Hexadecimal a Decimal es base usada por el sistema hexadecimal
print(hexa) # Resultado: 673778
octal = int('731254', 8) # De octal a Decimal
print(octal) # Resultado: 242348
