currentUsers = ['Ricky', 'Julian', 'Bubbles', 'Randy', 'Admin']
newUsers = ['Trevor', 'Jrock', 'Lucy', 'layhe', 'Ricky']

for user in newUsers:
    if user in currentUsers:
        print(f'{user} has been taken, please use something else.')
    else:
        print(f'{user} is available.')
        
