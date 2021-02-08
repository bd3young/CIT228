class User:
    def __init__(self, firstName, lastName, userName, phone, email, address, loginAttempts):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.phone = phone
        self.email = email
        self.address = address
        self.loginAttempts = 0

    def describeUser(self):
        print(f'{self.firstName} {self.lastName}')
        print('----------------------------------')
        print(f'UserName = {self.userName}')
        print(f'Phone Number = {self.phone}')
        print(f'Email = {self.email}')
        print(f'Address = {self.address}')

    def greetUser(self):
        print(f'Hello and Welcome! {self.firstName}')
    
    def incrementLoginAttempts(self):
        self.loginAttempts += 1

    def resetLoginAttempts(self):
        self.loginAttempts = 0

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



    