
#GLOBAL AND LOCAL VARIABLES

#variables that are created outside of functiom
#they can be used inside as well as outside of function

x = "harry" #GLOBAL variable
y = "edward"

def myfunc():
    y = "styles" #LOCAL variable
    z = "guys"
    print ("my name is " + x,y,z)
    #as local variable x is not present it will go for global one

print(x)
#print(z) invalid as z is notdefined as a global variable

myfunc()

print(y)

#output will be :
#harry
#my name is harry styles
#edward
#1)global variables inside func things gets compiled first then local
#i.e print(x) before print ("my name is " + x,y,z)
#2)also outside func stuffs gets compiled later as we are working on func first i.e print(y)
