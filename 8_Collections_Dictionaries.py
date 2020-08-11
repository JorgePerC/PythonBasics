# DICCIONARIES
# Its similar to JSON
# It stores values as
# pairs by key/value
# The items order is not guaratee*

dic = {"primero": "Christopher"}
# To add:
dic["last"] = "Harrison"

#To delete: 
#del dic['last']

print(dic)
print(dic["primero"])

# Returns a list of all keys in a dict
print(dic.keys())

# Returns a list of all stored values in a dict
print(dic.values())

# Returns a set of all keys and values
print(dic.items())