# String-In python, anything that you enclose between single or 
# double quotation marks is considered a string .

name="Ritika"
friend="Rohan"

# apple="he said,"he wants to eat apple""  # Error :double quotas inside double quotas .
apple="he said,'he wants to eat apple'"    # double quotas inside single quotas or vice-versa.
print(apple)

# ''' ''':triple quotation for multiline string
a='''Hi,
nice to meet you.
I also want to eat apple.'''
print(a)

#Index
# We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.
name1="Narayan"
print(name1[0])
print(name1[1])
print(name1[3])
print(name1[5])
# print(name1[9])   #error : IndexError: string index out of range

#Looping through a String
print("Lets use a for loop")
for characters in name1:
    print(characters)

for characters in a:
    print(characters)    

