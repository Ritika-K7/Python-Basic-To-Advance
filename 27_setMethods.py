
# Union and Update
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))  #union
print(s1,s2)
s1.update(s2) #update
print(s1,s2)

# intersection and intersection_update()
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","kabul","Madrid"}
cities3=cities.intersection(cities2) #intersection
print(cities3)
cities.intersection_update(cities2) #intersection_update
print(cities)
cities4=cities.symmetric_difference(cities2) #symmetric_diff
print(cities4)

# difference and difference_update
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Seoul","kabul","Delhi"}
cities5=cities.difference(cities2)
print(cities5)

# isdisjoint()
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","kabul","Madrid"}
print(cities.isdisjoint(cities2))

# issuperset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# issubset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add() -add single element to set
cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add('Helsinki')
print(cities)

# update()-to add more than one item

# remove()/discard()
cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove('Tokyo')
print(cities)

# pop()-remove last item from set
cities= {"Tokyo", "Madrid", "Berlin", "Delhi"}
item=cities.pop()
print(item)
print(cities)

# del-deletes the set entirely
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) #error-'cities'not define (trying to print deleted set)

# clear()-clear all items of set ans return empty set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")