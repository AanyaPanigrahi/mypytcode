#LOOPS

#while loop
#to print zoobie doobie 10 times
i=1
while i<=10:
    print(f'zoobie doobie {i}')
    i=i+1

#sum of numbers: 1 to 20
total=0
i=1
while i<=20:
    total=total+i #or total += i
    i=i+1
print(total) #1+2+3+...+20=210

#sum of n natural numbers
user_input=int(input('n: '))
total=0
i=1
while i <= user_input:
    total += i
    i += 1
print(total)

#example=1234
#output-sum=1+2+3+4

number=input('enter a number: ')
#1256 --> len/range=4 , last index=3
#int(number[i])

total=0
i=0
while i<len(number):
    total += int(number[i])
    i += 1
print(total)

#ask for user name input - Chris Hemsworth
#print count of each word
#output:
        #C - 1
        #h - 2
        #r - 2
        #i - 1
        #s - 2
        #H - 1
        #e - 1
        #m - 1
        #w - 1
        #o - 1
        #t - 1

name=input('enter your name: ')
#kashish
#name.count('k')=1 --> name.count(name[0])
#name.count('a')=1 --> name.count(name[1])
#name.count('s')=2 --> name.count(name[2])
#name.count('h')=2 --> name.count(name[3])
#name.count('i')=1 --> name.count(name[4])
#name.count('s')=2 --> name.count(name[5])
#name.count('h')=2 --> name.count(name[6])

temp_var=''
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f'{name[i]}: {name.count(name[i])}')
    i+=1
