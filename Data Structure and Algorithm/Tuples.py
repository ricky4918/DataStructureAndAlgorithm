#immutable(can't add / change)
#Useful for fixed data
#fater than Lists
#Sequence type


#Constructors

x = ()
x = (1,2,3)
x = 1, 2, 3
x = 2, # the comma tells python it's a tuple
print(x, type(x))

list1 = [2,4,6]
x = tuple(list1)
print(x, type(x))

#Tuples are immutable

x = (1,2,3)
# del(x[1])
# x[1] = 8
print(x)


y = ([1,2], 3) # can delete value in list in tuple
del(y[0][1])
print(y)

y +=(4,) # concanating works
print(y)



