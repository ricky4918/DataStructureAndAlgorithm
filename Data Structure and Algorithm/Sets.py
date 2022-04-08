#Store non-duplicates items
#Very fast access vs Lists
#Math Set ops(union, intersect)
#Sets are Unordered


#Constructors
x = {3,4,3,5}
print(x)

y = set()
print(y)

list1 = [2,3,4]
z = set(list1)
print(z)

#Set Operations


x = {3,8,5}
x.add(7)
print(x)

x.remove(3)
print(x)


#get length of set x
print(len(x))


# check membership in x
print(5 in x)


# pop random item from the set x
print(x.pop(),x)


x.clear()
print(x)


#Mathmatical set operations


s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)

