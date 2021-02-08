from user import User
from privileges import Privileges
from admin import Admin

myselfOne = User('Beau', 'DeYoung', 'Breauseph', '231-366-8871', 'breauseph@gmail.com', '231 Sandy Ln, FL 54321', 0)
myselfTwo = User('John', 'Doe', 'JoDo', '546-300-8000', 'jodo@gmail.com', '630 Hello Dr, OH 47832', 0)
myselfThree = User('Jane', 'Doe', 'JaDo', '546-370-8070', 'jado@gmail.com', '630 Hello Dr, OH 47832', 0)
myselfOne.greetUser()
myselfOne.describeUser()
print()
myselfTwo.greetUser()
myselfTwo.describeUser()
print()
myselfThree.greetUser()
myselfThree.describeUser()
print()

print('Exercise 9-5')
print('=================================================================')

while(myselfOne.loginAttempts <= 2):
    myselfOne.incrementLoginAttempts()
    print(f'{myselfOne.firstName} has triend to login {myselfOne.loginAttempts} times!')
myselfOne.resetLoginAttempts()
print(f'Reset attempts - {myselfOne.loginAttempts}')

print('Exercise 9-7 and 9-8')
print('=================================================================')
myselfAdmin = Admin('Beau', 'DeYoung', 'Breauseph', '231-366-8871', 'breauseph@gmail.com', '231 Sandy Ln, FL 54321', 0 )
myselfAdmin.describeAdmin()