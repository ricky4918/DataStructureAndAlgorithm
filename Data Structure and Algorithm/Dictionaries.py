#Key/Value pairs
#Associative array,like Java HashMap
#Dicts are Unordered


x = {'pork': 25.3, 'beef': 33.8, 'chcken': 22.7}
print(x)
x = dict([('pork', 25.3), ('beef',33.8), ('chicken', 22.7)])
print(x)
x = dict(pork = 25.3, beef=33.8, chicken = 22.7)
print(x)


#dic operations

x['shrimp'] = 38.2
print(x)

#delete
del(x['shrimp'])
print(x)

#get length of dict x

print(len(x))

# delete all items from dict x
x.clear()
print(x)

# delete dic
del(x)
#print(x)


# Acessing keys and clues in a dict

x = dict([('pork', 25.3), ('beef',33.8), ('chicken', 22.7)])

print(x.keys())
print(x.values())
print(x.items())


print('beef' in x)

print('clams' in x.values())

#iterating dict

for key in x:
    print(key, x[key])


for k, v in x.items():
    print(k,v)


