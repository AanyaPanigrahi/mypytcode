
# AND / OR --> check two conditions at once

#AND 
name='ankita'
age=20
if name=='ankita' and age==20:
       print('condition True')
else:
       print('condition False')
#both conditions need to match for the outcome to be true

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


# in KEYWORD
# if with in
name='Levi Ackerman'
if 'k' in name:
    print('k is present in name')
else:
    print('k is not present in name')

#check EMPTY OR NOT
name=input('enter your name: ')
if name:
    print(f'hello {name}, welcome to the site')
else:
    print('you didn\'t write your name')

#break & continue KEYWORD

for i in range(1,11):
       if i==5:
              break
       print(i)
#output --> 1,2,3,4

#print 1 to 10 but not 5
for i in range(1,11):
       if i==5:
              continue
       print(i)
