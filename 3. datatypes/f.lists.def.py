nums=list(range(1,6))

def negativelist(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negativelist(nums))

def square_list(q):
    square=[]
    for i in q:
        square.append(i**2)
    return square
print(list(range(1,11)))

def reverse_list(m):
    m.reverse()
    return m
print(reverse_list(nums))

#def reverselist(l):
#     return l[::-1]

l=['abc','def','tuv']
def rev(k):
    ele=[]
    for i in k:
        ele.append(i[::-1])
    return ele[::-1]
print(rev(l))

def filter_odd_even(k):
    odd=[]
    even=[]
    for i in k:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output

nums=[1,2,3,4,5]
print(filter_odd_even(nums))

def common(l,k):
    output=[]
    for i in l:
        if i in k:
            output.append(i)
    return output
nom=[3,4,5,6]
print(common(nums,nom))

def lists(l):
    total=0
    for i in l:
        if type(i)==list:
            total+=1
    return total
z=[7,7,9,[1,2,3],[2,3]]
print(lists(z))
