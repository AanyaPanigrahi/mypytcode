#if STATEMENT
#syntax
#if condition:
       #if true then the code will run
age=input("enter your age: ")
age=int(age)
if age>=18:
    print("hey")
    print("you are above 18")

#pass STATEMENT
x=18
if x>18:
       pass #won't show error then

#if-else STATEMENT
age=input("enter your age: ")
age=int(age)
if age>=14:
       print("you are above 14")
else:
       print("sorry you can't play")
