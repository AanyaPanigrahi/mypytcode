#Dictionary

myDict={
    "python" : "a high level programmming language",
    "petrichor" : "a pleasant smell that accompanies the first rain after dry weather",
    "marks" : [0,1,2],
    "anotherDict" : {
    "python" : "a poisonous snake"
    } #nested dictionary
}

print(myDict["python"])
print(myDict["petrichor"])
print(myDict["marks"])
print(myDict["anotherDict"]["python"])

#unordered, mutable, indexed, can't have duplicate keys
myDict["marks"]=[6,7,8]
print(myDict["marks"]) #mutable -> values changed

#keys must be unique whereas values can be same