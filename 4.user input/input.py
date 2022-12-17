#USER INPUT

#input function
name=input("type your name:")
print("hello",name)
age=input("what is your age? ") #input-str "18"
print("your age is " + age)
number1=input('input first number: ')
number2=input('input second number: ')
total = number1 + number2
print(total) #23
#str input by default
#'2'+'3'= 23
num1=int(input('first num: '))
num2=int(input('second num: '))
total=num1+num2
print('sum:', total) #or print('sum: ' + str(total))
# 2+3=5 output
num3=int(input('int: '))
num4=float(input('float: '))
sum=num3 + num4
print('sum: ', sum) #ans will be in float -> 5.0

#name=input('enter your name: ')
#age=input('enter your age: ')
name, age= input("enter your name and age: ").split() #or .split(",")
print(name)
print(age)

name="aanya"
age=18
print("hello " + name + " your age is " + str(age)) # hello aanya your age is 18

#string formatting
#python3
print('hello {} your age is {} '.format(name,age-2)) # same output better syntax -> 16
#python3.6
print(f"hello {name} your age is {age+2}") #same output {-}placeholders -> 20

# num1=int(input('enter first number: ')) #3
# num2=int(input('enter second number: ')) #3
# num3=int(input('enter third number: ')) #3
num1,num2,num3 = input('enter three numbers comma seperated: ').split(',') #3,3,3
print(f"the average is {(int(num1)+int(num2)+int(num3))/3}") #3.0



