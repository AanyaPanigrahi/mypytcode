#pattern 1

'''

*
**
***
****

'''

n=int(input('enter num : '))
for i in range(n+1):
    print('*'*i)
    i+=1

#pattern 2

'''

  *  
 ***
*****

'''

n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
