user_info = {'first_name': '', 'last_name': ''}
first_name = input('Enter your name: ')
user_info['first_name'] = first_name
last_name = input('Enter your last name: ')
user_info['last_name'] = last_name
print(user_info.values())