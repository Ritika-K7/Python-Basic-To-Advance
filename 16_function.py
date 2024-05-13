# Geometric mean
 # a=9
 # b=8
 # gmean1=(a*b)/(a+b)
 # print(gmean1)
 # c=8
 # d=8
 # gmean2=(c*d)/(c+d)
 # print(gmean2)
# we have to calculate again and again

# Function
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)   

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal") 


# I dont want to give function body now ->pass-> it means do noting python i will come and complete it.
def isLesser(a,b):
    pass

a=7 
b=6  
isGreater(a,b)
calculateGmean(a,b)
c=3
d=9
isGreater(c,d)
calculateGmean(c,d)

# function
# 1.Built-in function - min(),max(),sum() etc
# 2.User define  - using def keyword 