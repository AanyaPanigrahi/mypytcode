
#Assigning Values To Variables
# 1) assigning multiple values to multiple variables

x=10
y=20
z=40
print (x)
print (y)
print (z)

#can also be done as
x,y,z = 10,20,40
print (x)
print (y)
print (z)
print (x,y,z) #will give lateral values

# 2) assigning same values to multiple variables
x=y=z=20
print(x,y,z)

#Output Variables

x = "my name is john"
print(x)
#can also be done as
x="my"
y="name"
z="is"
print(x,y,z) #gives same output i.e. printing multiple strings as my name is
#but print (x+y+z) will not give same output
print (x+y+z) #combines it to a single string as mynameis

#concatenation of str - adding str datatypes
x='hey '
y='guys'
z=x+y
print(z) #hey guys
#str can only be  added to str i.e we can't add int to it
#but an int can be multiplied -
print('hey'*3) #heyheyhey
