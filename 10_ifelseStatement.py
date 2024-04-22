# If-Else Statement
# Ex -1
a=int(input("Enter your age:"))
print("Your age is:",a)
if(a>18):
    print("You can Drive!")
    print("Yes")
else:
    print("You cannot Drive!")
    print("No")

#Conditional Operators : > ,< ,>=,<= ,==,!=
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)
 
# Ex-2 
applePrice=210
budget=200
if(applePrice<=budget):
    print("Alexa,add 1 kg Apples to the cart.")
else:
    print("Alexa,do not add Apples to the cart.")



#If-Elif Statement
# Example1
applePrice=10
budget=200
if(budget-applePrice>50):
   print("Alexa,add 1 kg Apples to the cart.")
elif(budget-applePrice>70):
    print("Its okay you can buy")   
else:
    print("Alexa,do not add Apples to the cart.")
#Example2
num=int(input("Enter num:"))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is Zero")
elif(num==999):
    print("Number is special")
else:
    print("Number is Positive")



# Nested If Statement (If inside If)
num=18
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



