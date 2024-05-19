#Tuple-curved bracket,immutable

tup=(1,5,6,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

tup1=(1,2,67,342,32,"green") 
if 342 in tup1:
    print("Yes")

# elem get copy in tup2 new tuple name tup2 will be created 
tup2=tup1[1:4]
print(tup2)    