#General Purpose
#Most widely used data structure
#sortable
#Grow and shrink size as needed
#Sequence type


#Constructors

x = list()
y = ['a', 5, 'y', 8.43]
tuple1 = (10,20)
z = list(tuple1)

# list comprehension

a = [m for m in range(8)] #0 ~ 7
print(a)

b = [i**2 for i in range(10) if i> 4]
print(b)


# Delete

x = [5,3,8,6]
del(x[1])
print(x)
del(x) # delete entire list
print(x)

# Append

x = [5,3,8,6]
x.append(7)
print(x)

# extend

x = [5,3,8,6]
y = [12, 13]
x.extend(y)
print(x)

# insert

x = [5,3,8,6]
x.insert(1,7) #(index, value)
print(x)
x.insert(1, ['a', 'b'])
print(x)

# pop

x = [5,3,8,6]
x.pop()
print(x)
print(x.pop())

# remove

x = [5,3,8,6,3]
x.remove(3)
print(x)

# reverse

x = [5,3,8,6]
x.reverse()
print(x)

# sort
x = [5,3,8,6]
x.sort()
print(x)


# reverse sort
x = [5,3,8,6]
x.sort(reverse=True)
print(x)











