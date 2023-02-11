#TUPLES

#tuples are  used to store multiple items in a single variable
#tuple is ordered
#tuples can have duplicates
#tuples are immutable/unchangeable
#i.e.we cannot add, change, remove the items after it is created
#they are writtten with rounded brackets ()

tuple = (10,20,30,40)
#tuple[1]=80 not supported as it is unchangeable
print(tuple) #(10,20,30,40)
print(tuple[0]) #10
print(len(tuple)) #4

#tuple  with one element
my_tuple=(10)
print(my_tuple) #10
print(type(my_tuple)) # <class 'int'>

my_tuple=(10,) #always add comma after element
print(my_tuple) # (10,)
print(type(my_tuple)) # <class 'tuple'>

#can store items of any data type
mytuple=(10,'apples',True,100)
print(mytuple) #(10,'apples',True,100)

#TUPLE CONSTRUCTOR
#myTuple=tuple((10,20,30,40))
#print(myTuple)

#ACCESS THE ELEMENTS OF  TUPLE
mytuple2=(10,20,30,40)
print(mytuple2[3]) #40
print(mytuple2[-1]) #40

#can also  use range of indexes
print(mytuple2[2:4]) #(30,40)
print(mytuple2[:4]) #(10,20,30,40)
print(mytuple2[1:]) #(20,30,40)
print(mytuple2[-3:-1]) #(20,30)

#CHANGE TUPLE ELEMENTS
#tuples are unchangeable or immutable
#no append no insert no add no pop no remove
#why tuples? -> tuples are faster than lists
#we can use methods like count, index, len func, slicing