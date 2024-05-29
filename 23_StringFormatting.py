
letter="Hey my name is {} and I am from {}"
name='ritika'
country='India'
print(letter.format(name,country))
# Using Index
letter="Hey my name is {1} and I am from {0}"
print(letter.format(country,name))

# ------------------OR--------------------
# f-string in Python
name='RAHUL'
country='Japan'
print(f"Hey my name is {name} and I am from {country} ")

txt="For only {price: .2f} dollars!"
print(txt.format(price=49.099))

# Print raw fstring
print(f"We use f-string like this :hey my name is {{name}} and I am from {{country}}")