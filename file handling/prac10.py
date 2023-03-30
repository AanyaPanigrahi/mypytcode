import os
old_name = 'sample3.t'
new_name = 'sample4.t'
with open(old_name,'r') as f:
    content=f.read()
with open(new_name,'w') as f:
    f.write(content)
os.remove(old_name) #will delete the older file
#only way to rename