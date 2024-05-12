# Break
'''The break statement enables a program to skip over a part 
of the code. A break statement terminates the very loop it lies within.'''

for i in range(12):
    print("5 X",i+1,"=",5*(i+1))
    if(i+1 == 10):
        break
print("Loop ko chod kar nikal gaya")    



# Continue
'''The continue statement skips the rest of the loop 
statements and causes the next iteration to occur.'''
for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X",i,"=",5*(i))
 