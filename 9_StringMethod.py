#Strings are immutable - strings can not be changed ,string methods operats on your 
#string and provide new string

a="Ritika"
print(len(a))

#UPPER CASE -upper()
print(a.upper())

# Lower case -lower()
print(a.lower())

#To remove trailing charater(**not starting char(Eg.!!hello)) -rstrip("")
b="Hello!!!!"
print(b.rstrip("!"))

#replace()- Replace all string by another string
c="John"
print(c.replace("J","d"))
print(c.replace("John","Sliver"))

#split() - split the string into list where ever space is there.
d="Today is the silver Moon."
print(d.split(" "))

#Capitalize()
# The capitalize() method turns only the first character of the string to uppercase 
# and the rest other characters of the string are turned to lowercase
heading="introduction to js"
print(heading.capitalize())
heading2="intro tO pD" #by mistake capital - O & D
print(heading2.capitalize())

#center()
str1="Welcome to terminal!!"
print(str1.center(50))
# We can also provide padding character. It will fill the rest of the fill 
# characters provided by the user.
str1="Welcome to terminal!!"
print(str1.center(50,"."))

#count()
e="Let's play a game with a bat."
print(e.count("a"))

#endswith()-return True/False
str2="Bornhill star light cause happiness!!!"
print(str2.endswith("!!!"))
str3="Welcome to console!!!"
print(str3.endswith("to",4,10))

#find()-return index of first occurance of given value
str4="He's name is Dan. He is an honest man."
print(str4.find("is"))