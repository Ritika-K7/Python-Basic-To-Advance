#append()
l=[1,2,3,4]
print(l)
l.append(7)   #append() add element to the end of list.
print(l)

#sort
l2=[11,45,1,4,3,2,6]
l2.sort()   # sort the list in acessending order
print(l2)
l2.sort(reverse=True)   # sort in deceding order 
print(l2)

#reverse()
l2.reverse()
print(l2)

#index() 
l2=[1,2,3,4,6,11,45] 
print(l2.index(1))

#count() - count the courance of element
print(l2.count(45))

#copy()
#not recemmended
l=[11,45,1,2,4,6,1,1]
m=l
m[0]=0
print(l) # original list l is got changed
# recammended
l=[11,45,1,2,4,6,1,1]
m=l.copy()
m[0]=0
print(m)
print(l) # original list l not changed

#insert()
l.insert(1,899)
print(l)

#extend()
l=[11,45,1,2,4,6,1,1]
m=[900,1000,1100]
l.extend(m)
print(l)

#concatenate
l=[11,45,1,2,4,6,1,1]
m=[900,1000,1100]
k=l+m
print(k)