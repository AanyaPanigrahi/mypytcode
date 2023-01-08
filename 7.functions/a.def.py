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

#can also be coded as
def is_it_even(numo):
    return numo%2==0 #boolean value
print(is_it_even(10))

#can also pass no parameter
def band():
    return "One Direction"
print(band())

#EXERCISE- GREATER NUMBER
def greater(a,b):
    if a>b:
        return a
    return b
x=int(input('enter first number: '))
y=int(input('enter second number: '))
print('greater number is',greater(x,y)) #print(greater(x,y))

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
print(greatest(4,5,6))

#can also be done using greater func() --> we can call a func inside another
def new_greatest(p,q,r):
    bigger=greater(p,q)
    return greater(bigger,r) #or greater(greater(p,q),r)
print(new_greatest(10,40,30))

#EXERCISE 2

#define a is_palindrome function that take one word in string as input
#and if it is palindrome return true else return false
#example - is_palindrome("madam") --> True
#example - is_palindrome("hello") --> False

#logic(algorithm)
#step1 - reverse the string
#step2 - compare the reversed string with the original one

def is_palindrome(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    else:
        return False
print(is_palindrome('aanya'))
print(is_palindrome('madam'))

#way 2
# def is_palindrome(word):
#     if word==word[::-1]:
#         return True
#     return False

#way 3
# def is_palindrome(word):
#     return word==word[::-1]
