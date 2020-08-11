#Básicos para manejar con archivos de texto

#Always open it with "with"
with open("file.txt", "a") as listaDePrimos:  #"a", to work as a list
    #To write on a file
    listaDePrimos.write("{}\n".format(10))
    #If you want to read an write on the same file, I recommend you to
    #First open the file with "r", then close and reopen with "a" 
#Remember to close it!
listaDePrimos.close()



#Also to read all the code, but more memory efficient        
with open("file.txt", "r") as archivo:
    for renglon in archivo:
        print(renglon)
    
    SIZE = 0
    #To read the entire documment --
    output= archivo.read(SIZE) #Remove size, unless you want to read from character LeftOff-SIZE
    print(output)

    #To read the a certain # of lines --
    output= archivo.readlines()
    print(output)

    #This reads the one line
    output = archivo.readline() 
    #It starts at line 0, and if we call it again, it will
    #read the second
    print(output)

    #To know wich character we are reading:
    position = archivo.tell()
    print(position)

    archivo.seek(position) #postition, changes the value of my pointer


