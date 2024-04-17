# In python, we can take user input directly by using input() function.
# This input function gives a return value as string/character .

a=input()
print(a) 

x=input("enter first num:")
y=input("enter second num:")
print(x+y)   #Output : x=3,y=3 ,x+y=33 (not 6)
# WHY?
# Input function returns the value as string. 
# Hence we have to typecast them whenever required to another datatype.
print(int(x)+int(y))  # Output:x=3,y=3 ,x+y=6

var1=int(input())
var2=float(input())
print(var1)
print(var2)