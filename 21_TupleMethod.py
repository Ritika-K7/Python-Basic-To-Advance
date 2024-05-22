'''Tuples are immutable, hence if you want to add, remove or 
change tuple items, then first you must convert the tuple to a list.'''

# tuple -> list ->(add,change ,remove etc)->tuple
countries=("Spain","Italy","England","Germany") #tuple
temp=list(countries) #tuple->list
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)  #list->tuple
print(countries)

# Concatebate tuple
countries =("Pakistan","Afghanistan","Bangladesh","ShirLanka")
countries2=("Vietnam","India","china")
southEastAsia=countries+countries2
print(southEastAsia)

# Tuple Methods
# Count()-The count() method of Tuple returns the number of times the given element appears in the tuple.
# Syntax : tuple.count(element)
tuple1=(0,1,2,3,2,3,1,3,2)
res=tuple1.count(3)
print("count of 3 in tuple is:",res)

# index() -The Index() method returns the first occurrence of the given element from the tuple
# Syntax : tuple.index(element, start, end)
tuple2=(0,1,2,3,2,31 ,1,3,2)
res=tuple2.index(3)
print("the index of 3 is :",res)

res1=tuple2.index(3,4,8)  # slicing the tuple 4-8 and find ocuurance of 3
print(res1)

# len()
res3=len(tuple2)
print(res3)