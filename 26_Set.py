# Sets are unordered collection of data items. 
# They store multiple items in a single variable.
# Set items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning you cannot change items of the set once created.
# Sets do not contain duplicate items.

s={2,4,2,6} #it will ignore one of the 2 & accept only one 2.
print(s)

info={"carls",19,False,5.9}
print(info)

#he items of set occur in random order and hence they cannot be accessed using index numbers.

# empty set
        #  h={} 
        #  print(type(h))     -> class'dict'
h=set()
print(type(h))        

# Accessing elements of set
info={"carls",19,False,5.9}
for value in info:
    print(value)

    