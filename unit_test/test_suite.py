import unittest
from employee_test import TestEmployee

if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    tests = [TestEmployee('test_applyRaise'), TestEmployee('test_pos'), TestEmployee('test_fullname')]
    suite.addTests(tests)
    
    '''
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    '''
    
    file_name = 'test_log.txt'
    with open(file_name, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)