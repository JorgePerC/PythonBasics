day = input("¿Qué día es?: ")
if day=="lunes" or day == " martes"or day=="miercoles"or day=="jueves"or day=="viernes":
    print("Es un día de trabajo")
else:
    print("fin de semana, descansa")
#We can do the following:
if day.lower() in ("lunes", "martes", "miercoles", "jueves", "viernes"):
    print("Es un día de trabajo")
#Boolean statements
boolean = True
boolean = False
if boolean: #There's no need for you to put == True
    print("Boolean value is true")

    