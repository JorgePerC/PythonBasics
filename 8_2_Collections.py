JP = {}
JP ["First"] = "Jorge"
JP ["Second"] = "Pérez"

DP = {"First": "Daniela", "Last": "Pérez"}
print(JP)
print(DP)
#You CAN insert diccinaries in a list.!!!!! :)

family = [JP, DP]
print(family)

family.append({"First": "Karina", "Last": "Pérez"})
print(family)

show = family[0:2] #This accually returns a new list
print(show)
family.sort()
print(family)