#for loop with range function

#i=0
#while i < 10:
    #print('taylor')
    #i+=1
for i in range(10): #i=0to9, 10 not included
    print(f'heyya : {i}')

for i in range(1,11): #i=1to10, starts from 1 & 11 not included
    print(f'yayy : {i}')

#example: sum from 1 to 10
total=0
for i in range(1,11):
    total+=i
print(total)

#for sum of n numbers
n=int(input('enter num: '))
total=0
for j in range(1,n+1):
    total+=j
print(total)

#1256 --> 1+2+5+6
total=0
n=input('input a number: ')
for i in range (0,len(n)):
    total+=int(n[i])
print(total)

#Aanya Panigrahi
#A : 1
#a : 4
#n : 2
#y : 1
#'' : 1
#P : 1
#i : 2
#g : 1
#r : 1
#h : 1
#name.count('a') or name.count(name[i])

temp_var=""
q=input('name:')
for i in range(0,len(q)):
    if q[i] not in temp_var:
        print(f'{q[i]} : {q.count(q[i])}')
        temp_var+=q[i]

#step argument
#odd numbers 1 to 10
for i in range(1,12,2):
    print(i) #1,3,5,7,9,11

#10,9,8,.. upto 0
for i in range(10,-1,-1):
    print(i)

name="aanya"
# for i in range(len(name)):
#     print(name[i])
for i in name:
    print(i)

#1256 --> 1+2+5+6
num=input()
total=0
for i in num:
    total+=int(i)
print(total)
