#Dictionary Methods

myDict={
    "Why don't we" : "Chills",
    "Taylor" : "Cardigan",
    "sales" : [0,1,2],
    "anotherDict" : {"Charlie" : "That's Hilarious"},
    1 : 2
}

print(myDict.keys()) #dict_keys(["Why don't we", 'Taylor', 'sales', 'anotherDict', 1])
print(type(myDict)) # <class 'dict'>

#typecasting -> changing it  to list here
print(list(myDict.keys())) #temporary

# myDict=list(myDict.keys()) #permanent
# print(type(myDict)) -> list

print(myDict.values())
#dict_values(['Chills', 'Cardigan', [0, 1, 2], {'Charlie': "That's Hilarious"}, 2])
print(myDict.items())
#prints (key,value) for all contents  of  the dictionary in tuple inside list form

''' multiline comment
dict_items([("Why don't we", 'Chills'), ('Taylor', 'Cardigan'),
('sales', [0, 1, 2]), ('anotherDict', {'Charlie': "That's Hilarious"}), (1, 2)])
'''

#updating dictionary
new={
    "Miley" : "flowers",
    "Taylor" : "bejeweled"
    }
myDict.update(new)
print(myDict)

#difference between .get and [] method
#print(myDict["aanya"]) -> throws an error as aanya is not present
print(myDict.get("aanya")) #gives none as output i.e no key error otherwise same output
