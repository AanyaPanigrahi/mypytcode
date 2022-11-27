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

#is instance to check data type - true or false
print(isinstance("aanya",str)) #true
print(isinstance("aanya",int)) #false
print(isinstance("aanya",object)) #true
print(isinstance(1,object)) #true
#everything in python is an instance of object - only primitive class to be considered

#id-gives memory address
a=100
print(id(a)) #id address
print(hex(id(a))) #hexadecimal id address

#end and sep format
print(1,2,3,'riya',4) #1 2 3 riya 4 -> that is an in-built command to execute it with space
#but we can overcome this by using sep
print(1,2,3,'riya',4 , sep=',') #1,2,3,riya,4

#in-built new line character
print('hello') #hello
print('world') #world in the next line
#to break this new line character
print('hello',end=' ') #space within
print('world') #prints hello world in one line
# but world will still have new line character
