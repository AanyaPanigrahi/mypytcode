content=True
i=1
with open("samplelogfile.t",'r') as f:
    while content:
        content=f.readline()

        if 'python' in content.lower():
            print(content)
            print('python is present')
            print(i)
        i+=1