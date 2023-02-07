#LOOPING THROUGH LISTS
mylist4 = [10,20,30,40]
for x in mylist4:
       print(x) #10 next line 20 next line 30...
print(len(mylist4)) #4
print(range(len(mylist4))) #range (0,4)

length = len(mylist4)
rangeOfMyList = range(length)
for x in rangeOfMyList:
    #print(x) #0 next line 1 nl 2 nl 3
    print(mylist4[x]) #you will get values as per index

#LIST SORTING
#sorts in alpha numeric order by default (ascending order)

my_list = ['banana', 'orange','apple','guava']
my_list.sort()
print(my_list) #apple, banana, guava, orange

listA = [90,400,200,20,10]
listA.sort()
print(listA) #10,20,90,200,400

#to sort in descending order
listA.sort(reverse = True)
print(listA) #400,200,90,20,10

#CASE SENSITIVE SORTING
#by deault sort() is case sensitive
#all the capital letters will be sorted before lowercase letters

my_list2 = ['banana', 'Orange','Apple','guava']
my_list2.sort()
print(my_list2) #A O b g - sequence

my_list2.sort(key = str.lower)
print(my_list2) #A b g O

#TO SIMPLY  REVERSE THE ORDER OF LIST
my_list3 = ['banana', 'orange','apple','guava']
my_list3.reverse()
print(my_list3)

#COPYING THE LIST

list1 = [10,20,30,40]
list2 = list1
print(list2) #[10,20,30,40] as output but this is the same list not a copied one

list2.pop()
print(list2) #[10,20,30]
print(list1)#[10,20,30]
#but original list should not be affected i.e they are thus the same lists
#so to make a copied file :

listA = [10,40,60,90]
listB = listA.copy()
#or  listB=list(listA)
print(listB) #[10,40,60,90]
listB.pop()
print(listB) #[10,40,60]
print(listA)#[10,40,60,90] i.e . original list isn't changed

numbers=[1,4,7,2]
#sort method --> numbers.sort()
#to print sorted list without making any change to the original list
print(sorted(numbers))
print(numbers)

#clear method --> to turn the list empty
numbers.clear()
print(numbers)

#is vs equals
list1=[2,5,6]
list2=[2,5,6]
list3=[2,3,9]
print(list1==list3) #false
print(list1==list2) #true
print(list1 is list2) #false
list2=list1
print(list1 is list2) #true
# == values are same
# is tells if its the same object

#string to list --> split method
info='hello, world'
print(info.split(','))
#list to string --> join method
listA=['hey','hi']
print(','.join(listA))

#lists are mutable unlike strings

#looping in lists
fruits=['apple','banana','mango','kiwi']

for i in fruits:
    print(i)

i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

#list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]] #2d list
print(matrix[0]) #[1,2,3]

for j in matrix:
    for i in j:
        print(i)

print(matrix[1][2]) #6
print(type(matrix)) #list

#list generate
nums=list(range(1,6))
print(nums)
print(nums.pop())
print(nums.index(3)) #2

def negativelist(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negativelist(nums))

def square_list(q):
    square=[]
    for i in q:
        square.append(i**2)
    return square
print(list(range(1,11)))

def reverse_list(m):
    m.reverse()
    return m
print(reverse_list(nums))

# def reverselist(l):
#     return l[::-1]
