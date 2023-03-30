with open("samplelogfile.t",'r') as f:
    content=f.read()
if 'python' in content.lower():
    print('python is present')