x= int(input("Mete un número"))
y= int(input("Mete otro número"))
try:
    print(x/y)
except ZeroDivisionError as identifier:
    print("You can't devide by 0")
else:
    print("Something weird happened")
finally:
    pass
    #This will be executed after the try
    print("This is our clean up code")
    #Pass does nothing