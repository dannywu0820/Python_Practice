import unittest
from employee import Employee

#cmd: python -m unittest employee_test
class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    
    #set up before each test
    def setUp(self):
        print('setUp')
        self.emp1 = Employee('Danny', 'Wu', 1000)
        self.emp2 = Employee('Henry', 'Huang', 2000)
    
    #tear down after each test
    def tearDown(self):
        print('tearDown')
    
    @unittest.skip("Don't run this case")
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Danny Wu')
        self.assertEqual(self.emp2.fullname, 'Henry Huang')
    
    def test_applyRaise(self):
        self.emp1.applyRaise()
        self.emp2.applyRaise()
        self.assertEqual(self.emp1.pay, 1050)
        self.assertEqual(self.emp2.pay, 2100)
        
    def test_pos(self):
        self.emp1.setPos('CTO')
        self.assertEqual(self.emp1.getPos(), 'CTO')
        
        with self.assertRaises(ValueError):
            self.emp1.setPos(123)
        