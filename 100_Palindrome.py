num=int(input("Enter the Number:"))
num_str=str(num)
if num_str==num_str[::-1]:
    print("Palindrome")

else:
    print("Not palindrome")    