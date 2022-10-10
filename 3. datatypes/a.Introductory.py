#DATA TYPES are just the type of data that a variable can store/hold

x = "hey" # str for string or texts
y = 40 # int for integers
z = 2.568 # float for decimal values

#to get the class type printed use:
print(type(x))

a = 20 + 6j #class type complex for  complex numbers
print(type(a))

x = [10,20,30] #list type #has same data types i.e int
print(type(x))

y = (10,20,30) #tuple
print(type(y))

x = [10, "hello",50] #list type # has different data types i.e int and str
print(type(x))
print(x[0]) #10
print(x[1]) #hello
print(x[2]) #50
#print(x[3]) out of range

#ARRAYs
#arrays store data in a contiguous memory location i.e. consecutive blocks / ordered collection
#ex   [10,20,30]
#index 0 ,1 ,2  