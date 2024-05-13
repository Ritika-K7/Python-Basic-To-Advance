#function Arguments
def average(a,b):
    print("The average is",(a+b)/2)
average(4,6)    

# There are four types of arguments in a function:
# 1.Default Arguments
# 2.Keyword Arguments
# 3.Variable length Arguments
# 4.Required Arguments

# Default - Function assumes a default value even if a value is 
#           not provided in the function call for that argument.
#           "parameter passed in order"
def average(a=1,b=9):
    print("The average is",(a+b)/2)

average() 
average(1,7)  #python will ignore the 1,9
average(5)    # a=5 ,b=9 default
average(b=9)  # b=9 ,a=1 default

# Keyword Arguments - arguments with key = value pair
#                     The the order in which the arguments are passed does not matter.
average(b=6,a=7)

# Required Arguments
# def average(a,b=9): -> average(a=5) necessary to pass the arguments in function call

# Variable length Arguments
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/len(numbers)
    
c=avg(5,6,7,1)
print(c)  
  
#   print("Average is:",sum/len(numbers))  
# avg(3,4)      