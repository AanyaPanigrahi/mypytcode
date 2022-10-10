#LIST DATA TYPE

listitems1 = [10,20,30,40]
print(listitems1)
print(type(listitems1)) #list type

listitems2 = [10,"apples",40,50,"oranges"]
print(type(listitems2))  #also of list type

listitems3 = [10,20,20,30,40,30]
print(listitems3) #output [10,20,20,30,40,30]
#therefore list can take multiple data types as well as duplicate values

print(listitems1[2]) #index works here too so 30
print(listitems2[4]) #oranges
print(listitems3[0]) #10
#print(listitems1[4]) #index out of range

listOne = ["abcd", 40, True, 60, "apples"] #valid by boolean rules

#creating a list through CONSTRUCTOR METHOD

listOne = [10,20,30,40] #BRACKET METHOD
print(listOne)
listTwo = list((10,20,30,40)) #CONSTRUTCOR METHOD
print(listTwo) #both will give same output [10,20,30,40]

#ACCESS ITEMS OF A LIST

listOne = 10,20,30,40,50
print(listOne[-2]) #40
print(listOne[2:5]) #20,30,40,50 -> 5th not included still if
print(listOne[2:6]) #20,30,40,50 output will be same it doesn't have anymore elements
#i.e. no output but also no error

print(listOne[:4]) #10,20,30,40 not including 4th
print(listOne[2:]) #30,40,50

#CHANGE LIST ITEMS
listA = [10 , 60, 20, 80]
listA[0] = 90
listA[2] = "hey"
print(listA) #90,60,hey,80

#CHANGE A RANGE OF LIST ITEMS

listA[1:3]=["hi","bye"]
print(listA) #90,hi,bye,80

#insert more items than replace then new items will be inserted at the provided index
listB = [10,20,30]
listB[1:2]=["yo","bro"]
print(listB) #10,yo,bro,30

#adding the list items

#INSERT ITEMS
#to add items in between the list
list1 = [10,20,30]
list1.insert(2,40) #need to mention index at which u wish to insert
print(list1) #[10,20,40,30] i.e. 40 gets inserted at index 2

#APPEND ITEMS
#to add items at the end of list
list2 = [30,40,50]
list2.append(60)
list2.append(70)
print(list2) #[30,40,50,60,70] i.e. 60,70 gets added at the very end of list

#EXTEND LIST
#to append or add elements from another list into the current one
list1 = [10,20,30]
list2 = [40,50,60]
list2.extend(list1)
print(list2) #[40,50,60,10,20,30]
print(list1) #[10,20,30]
tuple=(80,90)
list1.extend(tuple)
print(list1) #[10,20,30,80,90] i.e. extend func works for tuple and other data types also

#REMOVING ITEMS FROM LIST

#remving specified item from a list
mylist = ["john", "peter", "raj"]
mylist.remove("raj")
print(mylist) #["john","peter"]

#remove item from specified index
list=["hi","hello","bye"]
list.pop(1) #hello
print(list) #["hi","bye"]

listB = [10,20,30,40]
listB.pop() #if index not mentioned it'll consider removing one from end i.e 40
print(listB) #[10,20,30]
listB.pop() #30
listB.pop() #20
print(listB) #output [10]

#DEL KEYWORD
LIST = ["aanya","riya","anie"]
del LIST[2] #anie will be removed
print(LIST)
#if index is not mentioned it'll delete whole list
#del LIST
#print(LIST) #output -> list not defined / deletes whole list

#EMPTY LIST
LIST2 = ["aanya","riya","anie"]
LIST2.clear()
print(LIST2) #output is [] i.e. empty list

#LOOPING THROUGH LIST
mylist4 = [10,20,30,40]
for x in mylist4:
       print(x) #10 next  line 20 next line 30...
print(len(mylist4)) #4
print(range(len(mylist4))) #range (0,4)

length = len(mylist4)
rangeOfMyList = range(length)
for x in rangeOfMyList:
    #print(x) #0 next line 1 nl 2 nl 3
    print(mylist4[x]) #you will get values as per index

