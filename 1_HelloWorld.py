# Puedes definir el unicode al inico del documento con:
# El proósito es elimiar errores por simbolos raros
# -*-coding:utf-8-*-
# Aunque realmente no es necesario 
print("Niño mekü")
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

# Esto no es exclusivo de Python, pero:
      # TODO: es algo que se necesita hacer
      # FIXME: es algo que se necesita reparar
      # XXX: es algo que se necesita corregir
