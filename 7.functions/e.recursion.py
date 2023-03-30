# factorial
# n!=1x2x3x....x(n-1)xn
# n!=(n-1)!xn

# loop method
product=1
for i in range(5):
    product=product*(i+1)
print(product)

# function method
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

#function-recursion method
def factR(n):
    if n==1 or n==0:
        return 1
    return n*factR(n-1)

print(factorial(5))
print(factR(5))

#write code to print sum of n natural numbers using recursion
def sum(n):
    if n<=1:
        return n
    return n + sum(n-1)
print(sum(7))

# def recur_sum(n):
#   if n <= 1:
#       return n
#   else:
#       return n + recur_sum(n-1)
# print(recur_sum(5))
