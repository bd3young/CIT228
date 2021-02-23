class Employee:
    def __init__(self, fName, lName, salary):
        self.fName = fName
        self.lName = lName
        self.salary = salary

    def giveRaise(self, raiseAmount = ''):
        if raiseAmount:
            self.salary += raiseAmount
        else:
            self.salary += 5000