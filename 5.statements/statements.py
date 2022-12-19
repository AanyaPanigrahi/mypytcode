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

#AND 
name='ankita'
age=20
if name=='ankita' and age==20:
       print('condition True')
else:
       print('condition False')
#both conditions need to match for it to be true

#OR
name='adyasa'
age=19
if name=='adyasa'or age==18:
       print('YASS TRUE')
else:
       print('NOPE FALSE')
#atleast one condition needs to be true for the outcome to come true

#exercise - shinchan movie
name=input('your name: ')
age=int(input('your age: '))
if (name[0]=='a' or name[0]=='A') and age>=10:
       print('you can watch dark tama tama')
else:
       print('you cannot watch dark tama tama')


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
