users = ['Ricky', 'Julian', 'Bubbles', 'Randy', 'Admin']

if users == []:
    print('We need to get some users!')

for user in users:
    if user == 'Admin':
        print(f'Hello {user} would you like to see a status report?')
    else:
       print(f'Hello {user} thank you for logging in again!') 