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

class Admin(User):
    def __init__(self, firstName, lastName, userName, phone, email, address, loginAttempts, *privileges):
        super().__init__(firstName, lastName, userName, phone, email, address, loginAttempts)
        self.privileges = Privileges()
    
    def describeAdmin(self):
        print(f'{self.firstName} {self.lastName}')
        print('----------------------------------')
        print(f'UserName = {self.userName}')
        print(f'Phone Number = {self.phone}')
        print(f'Email = {self.email}')
        print(f'Address = {self.address}')
        print()
        self.privileges.showPrivileges()

class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges

    def showPrivileges(self):
        print(f'Admin Privileges')
        print('-----------------------')
        print('can add posts')
        print('can delete posts')
        print('can edit posts')
        print('can add users')
        print('can delete users')
        print('can edit users')

print('Exercise 9-7 and 9-8')
print('=================================================================')
myselfAdmin = Admin('Beau', 'DeYoung', 'Breauseph', '231-366-8871', 'breauseph@gmail.com', '231 Sandy Ln, FL 54321', 0 )
myselfAdmin.describeAdmin()
