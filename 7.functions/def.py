#FUNCTIONS

#name='aanya'
#print(len(name)) --> length / in-built function

#to make own function
#def func --> define
def add_two(a,b):
    return a+b
#z=add_two(2,3)
#print(z) or
print(add_two(2,3))

a=int(input("enter first number : "))
b=int(input("enter second number : "))
total=add_two(a,b)
print(total)

first_name='Aanya '
last_name='Panigrahi'
print(add_two(first_name,last_name))

#return vs print
def addkar(x,y):
    print(x+y)

addkar(2,8) #no need to command print again

def last_char(name):
    return name[-1]

print(last_char("aanchal"))
#print(last_char(9)) error --> pass a string while using index

def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(odd_even(9))

def is_even(numb):
    if numb%2==0:
        return True
    else:
        return False
print(is_even(7))