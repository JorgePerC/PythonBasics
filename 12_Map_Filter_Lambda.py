

# map is a reserved keyword that aplies a function to
# all of the elements of a list, or in the form of *args

#If we ant to use it, we would need to converte it into a list, or 
# Just use its iterable form

def multiply_by_2(num : int):
    return num*2
def multiply_by_3(num : int):
    return num*3

numbers_1_to_10 = range(1,11)

#Note we dont put parenthesis on the function
table_2 = list(map(multiply_by_3,numbers_1_to_10))

print(table_2)

#Filter function is like a map, but the function must return a bool
#If the condition is met, then is added to the final list
def is_odd(num : int):
    return not num %2 == 0

filtered = list(filter(is_odd,table_2))
print(filtered)

# Lambda is NOT A MATHETICAL function, but rather
# an easier way to define a funciton 
# in a shorter way

# For example, the following is like the
# multiply_by_3 method, but shorter
# However, if we want to call it from another place,
# We need to asing it
lambda value : value*3

times_two = lambda value :value*2
table_2 = list(map(times_two, numbers_1_to_10))
print(table_2)