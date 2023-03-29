#SETS IN PYTHON
#collection of non repetitive elements

a={}
print(type(a))
#this will create 
#dict not empty set

b=set()
print(type(b))

#adding values to empty set
b.add(3)
b.add(4)
b.add(5)
b.add(5) #will be counted once -> no duplicacy
b.add((6,7))

#list, dict (unhashable/mutable) cannot be added but tuple can be
#b.add([2,7]) / b.add({7,8})

print((b))
#sets are unordered, unindexed

#length of set
print(len(b))

#removal of element
b.remove(4)
print(b)
#b.remove(6) which is not in set -> error

print(b.pop()) # random deletion or removal
print(b)

b.clear()
#empties the set
print(b) #set()

c={3,7,9} #can make this way when not empty
print(c) #set
