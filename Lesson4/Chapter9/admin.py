from user import User
from privileges import Privileges

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


