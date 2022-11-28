
#PYTHON AS A CALCULATOR

# + addition
# - subtraction
# * multiplication
# / float division
# // integer division
# % modulo - gives remainder
# ** exponent

print(2/4) #0.5 float division
print(4/2) #2.0
print(4//2) #2 integer division
print(2//4) #0
print(2**3) #2 power 3 -> 8 exponent
print(2**0.5) #root 2 -> 1.414....
#to round off use round function
#round(number, ndigits)
print(round(2**0.5,4)) #to round off till 4 digits ->1.4142

print(4%2) #0 i.e remainder, modulo

#just like bodmas in maths in python we use -
#PERCEDENCE AND ASSOCIATIVITY RULE
# 1. Parenthese -> highest
# 2. Exponent -> right to left
# 3. (*,/,//,%) -> left to  right
# 4. (+,-) -> left to right

print((2+3)/2) #5/2=2.5 parenthese, highest percedence
print((2+3)*5/2%6) #5*5/2%6 = 25/2%6 = 12.5%6 = 0.5 , left  to right
print(2**3**2) #2**9 = 512 , right  to left