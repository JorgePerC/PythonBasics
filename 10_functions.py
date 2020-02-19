from datetime import datetime

#La función te permite repetir código sin volverlo a escribir
#There is no need to indicate the parameter type
def print_time():
    print("Your time is: ")
    print(datetime.now()) #datetime.datetime.now() --> Means yo import from library datetime, object datetime
                          #There's no need if we use from lib import class
    print()

#We can spacify a default value for our parameter:
    #If you do'nt specify the value for upperCase, it will automatically place it 
def print_nombre (nombre, upperCase=True):
    if(upperCase==True):
        print(nombre.upper())
    else:
        print(nombre.lower())

n = input("Dame tu nombre: ")
print_nombre(n,True)
print_nombre(n)
print_nombre(n, False)


#Named notation: This allows you to place parameters in an UNORDERED manner
#This in only viable when you call the function
#It's really helpful when reading your code
print_nombre(upperCase=False,nombre=n)
