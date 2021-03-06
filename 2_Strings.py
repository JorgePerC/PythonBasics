string ='Hello World' # This also works, either way
string2 = "Hello Jorge"
string3 = """ In Python, you 
can have multiple lines string
"""

print (string, string2, string3)

#  funtions to modify Strings
print(string.upper())
print(string.lower())
print(string.capitalize()) # This only caputalizes first String Letter
print(string.count("ll")) # As you may see, the count funcion can aplly to string sections

#  How to format Strings
output = "Hello World?" + " "+ string
output2 = "Hello, {} {}".format(string, string2)
output3 = "Hello, {0} {1}".format(string, string2)
output4 = f"Hello, {string} {string2}" #Formated string literal
output5 = "Hello, {1} {0}".format(string, string2)
# As you may seem, this prints the same thing. 
#  Its's worth noting that you need to space the brackets for the space to show up
    # If you put something else in between, it will also be shown
# The f example on ly works in Python 3
print(output)
print(output2)
print(output3)
print(output4)
print(output5)
# Otra manera de formatear el output3 es:
plantilla = "{0:.2f} {1:s} mucho más texto {2:d}" #El primer numero es la ubicación
            # {float con dos decimales} {string} {int}
print(plantilla.format(4.65515, "Mexico", 1))

letter = "e"
# Print 10 times e
print(letter*10)

#To get a list from the string:
# Defatult is " " (space), but you can pass any other caracter
print(string3.split())

#Formating floating values: 
floatNumber = 1/3
                    # {value: width.decimals f}
print("The result is: {:.3f}".format(floatNumber)) 