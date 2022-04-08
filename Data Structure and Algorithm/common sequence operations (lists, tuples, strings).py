# string
x = 'frog'
print(x[3])

# list
y = ['pig', 'cow', 'horse']
print(x[1])

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig")
print(x[0])


# Slicing
x = 'computer'

print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])


# adding/ concatenating

# string
x = 'horse + 'shoe'
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

#tuple
z = ('kevin',) + ('Crig',)
print(z)

#Multiplying

# string
x = 'frog' * 3
print(x)

# list
y = ['pig', 'cow', 'horse'] * 3
print(y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") * 3
print(z)

# checking membership

# string
x = 'frog'
print('r' in x)

# list
y = ['pig', 'cow', 'horse']
print('cow' not in y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print('Niklas' in z)

# iterating

x = [7, 8, 3]
for item in x:
  print(item)
  
y= [7,8,3]
for index, item in enumerate(y):
  print(index, item)


# Number of items

# string
x = 'frog'
print(len(x))

# list
y = ['pig', 'cow', 'horse']
print(len(y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(len(z))
      
# Minimum
      
# string
x = 'frog'
print(min(x))

# list
y = ['pig', 'cow', 'horse']
print(min(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(min(z))
      
      
# Maximum
      
# string
x = 'frog'
print(max(x))

# list
y = ['pig', 'cow', 'horse']
print(max(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(max(z))

# Sum
#list
x = [7, 8, 3]

#tuple
print(sum(x))
print(sum(x[-2:]))
      
z = (50, 4, 7, 19)
print(sum(z))
      
# Sorting
      
      
# string
x = 'frog'
print(sorted(x))

# list
y = ['pig', 'cow', 'horse']
print(sorted(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(sorted(z))
      
# sort by second letter
 
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(sorted(z, key = lamda k: k[1])
      
      
# Count
      
#string
x = 'hippo'
print(x.count('p'))

#list
y = ['pig' , 'cow', 'horse', 'cow']
print(y.count('cow'))

#tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(z.count('Kevin'))

      
# Index(item)

x = 'hippo'
print(x.index('p'))

#list
y = ['pig' , 'cow', 'horse', 'cow']
print(y.index('cow'))

#tuple
z = ('Kevin', 'Niklas', 'Jenny', "Craig") 
print(z.index('Kevin'))
   
# Unpacking
      
x = ['pig', 'cow', 'horse']
      
a, b , c = x

print(a, b, c)
      

      
      
      
      
      
      
      
 


