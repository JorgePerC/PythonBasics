#Python can display with either one or two quotes
print("Hello World")
print('Hello World')

print("Hola, los breaks sí funcionan \no no?")

#How to recieve an input
num= int(input("Inserta edad: "))
nom= str (input("Pon tu nombre: "))
apePaterno= str (input("Pon tu apellido paterno: "))
apeMaterno= str (input("Pon tu apellido materno: "))
#     The imput function returns a String by default

print("Eres " + nom + " " + apePaterno + " " + apeMaterno +
      " " + ", tienes " + str(num) + " años")
