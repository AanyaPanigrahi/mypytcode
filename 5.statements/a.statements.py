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

       
#NESTED if-else STATEMENT
winning_number=26
user_input=int(input("Guess a number between 1 and 100 : "))
if user_input == winning_number:
       print("You win!!")
else:
       if user_input < winning_number:
              print("Too low")
       else:
              print("Too high")
       #in place of else we can put other if condition as
       #if user_input > winning_number  
       
       
# AND / OR --> check two conditions at once

#if-elif-else STATEMENT
age=int(input('enter your age: '))
if age==0 or age<0:
       print("you can't watch")
elif 0<age<=3:
       print('ticket price: free')
elif 3<age<10:
       print('ticket price: 150')
elif 10<age<60:
       print('ticket price: 250')
else:
       print('ticket price: 100')
