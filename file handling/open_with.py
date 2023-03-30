#context manager
with open("sample2.t","r") as f:
    a=f.read()
print(a)
#best way to open and close file automatically
#no need to write f.close()