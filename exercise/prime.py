num=input("enter number : ")
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print('prime')
else:
    print('not prime')