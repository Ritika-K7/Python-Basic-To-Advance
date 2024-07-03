# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and 
# enclosed within curly brackets {}.

dic={
    "Ritika":"Human being",
    "spoon":"Object",
    344:"Harry",
    56 : "Shubham",
    678:"Zakir"
}
print(dic["Ritika"])


info={'name':'karan','age':19,'eligible':True}
print(info)
print(info["name"])
#Print all values
print(info.values())
# Print all keys
print(info.keys())
    # or
for key in info.keys():
    print(info[key])
    # or
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key,value in info.items():
     print(f"The value corresponding to the key {key} is {value}")
