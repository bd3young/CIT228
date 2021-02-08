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