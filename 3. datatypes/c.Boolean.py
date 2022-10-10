#BOOLEAN DATA TYPE

#here we don't have yes or no as outputs but true or false
print(5>2) #true
print(5==3) #false #also == stands for equals to as = is used to assign values
print(5<3) #false
#bool method that evaluates the values and return eiher true or false

print(bool('hello')) #true
print(bool(22)) #true

#values are true
#if value has a data it returns true
#any str will return true except empty str 
#any number returns true except zero
print(bool()) #false
print(bool(0)) #false
#any list, tuple, set, dictionary (data types) will return true except empty ones

#values that are false:
print(bool(False)) #writing false gives default output false
print(bool(None)) #writing none
print(bool()) #empty
print(bool(0)) #zero as value
print(bool(())) #empty tupil
print(bool([])) #empty list
print(bool({})) #empty dictionary
