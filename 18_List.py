l=[3,5,6]
print(l)
print(type(l))


marks=[4,5,6]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])


# Different datatype in a list
List1=[3,4,6,'ritika',True]

# Index
color=["red","green","blue","yello"]
print(color[0])
print(color[1])
print(color[2])
print(color[3])
print(color[-2])

print(color[3][2])

# Check whether item present in list?
marks=[3,4,6,'ritika',True]

if 7 in marks:
    print("YES")
else:
    print("No")    


if "ritika"in marks:
    print("YES")
else:
    print("No")    

print(marks)
print(marks[1:-1])
print(marks[1:4:2])  #start:end:jump    

# List Comprehension
list2=[i for i in range(4)]
print(list2)
list2=[i*i for i in range(4)]
print(list2)
list2=[i*i for i in range(10) if i%2==0]
print(list2)
