
with open("sample.t","r") as f:
    f1=f.read()
with open("samplecopy.t","r") as f:
    f2=f.read()

if f1==f2:
    print('identical')
else:
    print('not identical')