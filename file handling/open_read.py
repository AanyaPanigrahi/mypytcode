#Opening a File
#open() func -> 2 parameters
#open('file name','mode')

f=open('sample.t','r')
#f=open('sample.t') by default it is in r mode / read mode
data=f.read()
#to control number of characters to be read
#data=f.read(5) -> reads first 5 char from file i.e. hello
print(data)
f.close()