words=['khopdi','babuchak','pagal']
with open('sample2.t','r') as f:
    content=f.read()
for word in words:
    content=content.replace(word,'#%@&^%')
with open('sample2.t','w') as f:
    f.write(content)