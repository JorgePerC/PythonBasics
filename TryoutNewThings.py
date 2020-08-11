def myfunc (string: str):
    string_as_list = []
    is_even = False
    for letter in string:
        if is_even:
            string_as_list.append(letter.upper())
        else:
            string_as_list.append(letter.lower()) 
        is_even = not (is_even)
    string = ""
    return string.join(string_as_list)

print(myfunc("Hola"))