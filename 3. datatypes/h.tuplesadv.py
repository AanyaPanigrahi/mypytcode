#Looping in tuples
mixed=(1,2,'a','b',4)
for i in mixed:
    print(i)
#can also use while loop

#tuple with one element
nums=(1)
numo=(1,)
print(type(nums)) # class int
print(type(numo)) # class tuple

#tuple wihout parenthesis
singers = 'kk', 'arijit', 'zaeden', 'armaan'
print(type(singers)) # class tuple

#tuple unpacking
food = 'cheesecake','pizza','fries','noodles'
food1, food2, food3, food4 = (food)
print(food1)

#list inside tuples
places = ('France','Singapore',['Bali','Maldives'])
places[2].pop()
print(places)
places[2].append('Italy')
print(places)

# min(), max(), sum
numb=(1.0,4,5,2)
print(min(numb))
print(max(numb))
