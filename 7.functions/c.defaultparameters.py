#DEFAULT PARAMETERS

def user_info(first_name,last_name,age):
    print(f'your first name is {first_name}')
    print(f'your last name is {last_name}')
    print(f'your age is {age}')

user_info('aanya','panigrahi',18)
#user_info('aanya','panigrahi') --> missing one required positional argument

#we can add a default age n over write it later
def user_info(first_name,last_name,age=26):
    print(f'your first name is {first_name}')
    print(f'your last name is {last_name}')
    print(f'your age is {age}')

user_info('aanya','panigrahi') #your age is 26
user_info('aanya','panigrahi',18) #your age is 18 --> can over write
#None can also be a default parameter

#only end parameters can be default parameter not in between non default argument
# def user_info(first_name,last_name='unknown',age=None):
#     print(f'your first name is {first_name}')
#     print(f'your last name is {last_name}')
#     print(f'your age is {age}')