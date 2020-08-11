# In Python, there are not built in Arrays, 
# The default data type is Lists. Check more 
# On that. However, we can also use arrays
# Good old boi
# Tho, not exactly, the are different that in Java

# ARRAYS
# All data must be of the same kind
# You can only sotre simple types of data
# Has an index
# Storage order guaranteed
from array import array
scores = array("d") # What does "d" means???. It means Diggits
scores.append(97) # Add new item
scores.append(109)
print(scores)
print(scores[1])
# Common methods
print(len(scores))# How to get the LENGTH 
scores.insert(0, 10) # Inssert before Index (pos, val)
print(scores)

# TUPPLES
# Es una lista inmutable
tupple = (1,2,3,4)
print(tupple[0])

#Tupple unpacking
n1,n2,n3,n4 = tupple
print(n1)
print(n2)
print(n3)
print(n4)
# May raise "not enough values to unpack"


# zip (List1, list2)
# Is a Function that takes two lists and converts them into tupples