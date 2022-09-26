
import second_max_num.core.core as num
import unittest

class testcase(unittest.TestCase):
    def test_sec_max(self):
        k=[2,3,6,6,5]
        result= num.sec_max(k)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()