import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        fName='John'
        lName = 'Doe'
        salary = 40000
        self.employee = Employee(fName, lName, salary)

    def testGiveDefaultRaise(self):
        self.employee.giveRaise()
        self.assertEqual(self.employee.salary,45000)

    def testGiveCustomRaise(self):
        customRaise=10000
        self.employee.giveRaise(customRaise)
        self.assertEqual(self.employee.salary,50000)  

if __name__ == '__main__':
    unittest.main()