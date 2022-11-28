#STRINGS
#strings in python can be used in single as well as double quotes

#SINGLE LINE str
x = "okie dokie" #or as 'okie dokie'
print(x)

#MULTILINE str
y = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
     when an unknown printer took a galley of type and scrambled it to make a type specimen book"""

print(y)
#for multiline str use either ("""  """) or ('''  ''')

#strings are Arrays i.e. sequence of characters
a = "hello, world"
print(a[1]) #e
print(a[8]) #o

#to Print Whole Array
for x in "hello":
    print(x) #prints out all characters one by one

#len() gives out the LENGTH OF STRING
print(len(a)) #i.e. 12

#Presence Check (True/False)
#to check if a phrase or character is present in a string
x = "my name is aanya"
print("my" in x) #will give true as output
print("our" in x) #will give out false

#SLICING of string
a = "hello, world"

#get the characters from position 2 to 5
print(a[2:5]) #output comes out to be llo i.e 5/end part mentioned isn't included

#to slice from start
print(a[:5]) #just leave left side empty and it'll start from 0 0r mention 0

#to slice till end
print(a[2:]) #either leave right side empty or put last index

#syntax - [start argument : stop argument : step argument]
print("panigrahi"[2:6]) #nigr
print("panigrahi"[1:8:1]) #anigrah
print("panigrahi"[1:8:2]) #airh
print("panigrahi"[1:8:3]) #agh
print("panigrahi"[7::-2]) #hria backwards
print("panigrahi"[-1::-1]) #iharginap
print("panigrahi"[::-1]) #iharginap - trick to reverse

#negative index
#[10,20,30,40]
# 0, 1, 2, 3 from start
#-4,-3,-2,-1 if we want to index name it from the end
print(a[-4:-1]) #right side will not be compiled here too i.e -1 = d

#MODIFY STRINGS using built in methods

#UPPERCASE and LOWERCASE
x = "Hi Everyone"
print(x.upper()) #gives all caps i.e. HI EVERYONE
print(x.lower()) #gives all letters in lowercase i.e. hi everyone

x = "  let's study python"
print(x) #will have the space
#to REMOVE the not required SPACE
print(x.strip())

#to REPLACE
x = "hello world"
print (x.replace("h","a")) #will give output as aello world

#SPLITTING
x = 'hello guys'
print(x.split()) #gives output ['hello', 'guys'] i.e. an array of two
print(x.split()[0]) #will give the first element of array i.e. hello
print(x.split()[1]) #guys

#can also be done by taking another variable
x = "hi bye" #str
y = x.split() #array
print(y) # ['hi','bye']
print(y[0]) #hi
print(y[1]) #bye
print(x[0], y[0]) # h hi

#STRING CONCATENATION
x = "hello"
y = "world"
z = x + " " + y
print(z) #hello world

