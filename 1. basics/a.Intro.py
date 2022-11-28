#PRINT FUNCTION
print ("hello world")

#double quotes can have single quotation within and vice versa
print("Hello 'my' world") #hello 'my' world
print('hello "my" world') #hello "my" world
#print("hello "my" world") -> syntax error also for single quotation

# ESCAPE SEQUENCES
# \' single quote
# \" double quote
# \\ backslash
# \n new line
# \t tab
# \b backspace
print("hello \"my\" world") #hello "my" world
print('I\'m Aanya')
print("line A") #line A
print("line B") #line B
print("line A \nline B") #same output
print("name\taanya") #name   aanya (tab - space)
print("this is backslash\\") #this is  backslash\
#\\ -> \ backslash
#\\\\ -> \\ double backslash
print("hell\blo") #hello
#also use double quotes for using escape sequence

if 6>4:
   print ('6 is greter than 4')
   print ("hey")
   
   #100 lines of code but with no indentation/space error (while block creation)
#hashtag is to comment it i.e the comment won't be compiled
#organised
x = 10 #number
y = "hey" #string
print (x)
print(y)
#for string or text we can use either single or double quotations

#later value will print out i.e. latest
x = 10
x = "bye"
print (x)

#to print both do:
x = 10
print (x)
x = "bye"
print (x)

#python is a case sensitive language
a=60
A="hi"
print(a) #A will not overwrite

#get the type of variable printed i.e class type
x = 50 #int for integers
y = "aanya" #str for string/text
z = 1.546 #float for decimal values
print (type(x))
print (type(y))
print (type(z))

#casting

#to specify the data type of a variable using casting

x=int(10)
y=str(10)
z=float(10)
print (x,y,z) #will give 10 10 10.0
#print (x+y) will give error as int can't be added to str
#same with y and z
print(x+z) #comes out 20.0 as it's int+float (no. + decimal value)
