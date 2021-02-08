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