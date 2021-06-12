import unittest
from fibonacci import  Fibonacci 

class TestFibo(unittest.TestCase):
    def test_series(self) :
        print('\nTest Series 8')
        result_expected = [0,1,1,2,3,5,8,13]
        result_obj = Fibonacci(8)
        result_obj.create_fibonacci()
        test_result = result_obj.get_output()
        self.assertEqual(result_expected,test_result)

if __name__ == '__main__' : unittest.main()    

