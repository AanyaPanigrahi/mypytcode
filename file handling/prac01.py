f=open('samplepoem.t','r')
a=f.read()
if 'twinkle' in a:
    print('it is present')
else:
    print('not present')
f.close()