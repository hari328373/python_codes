import unittest
import timedelta.core.core as td
#class for unittesting
class testsample(unittest.TestCase):
    def test_time(self):
        result=td.time_delta('Sun 10 May 2015 13:54:36 -0700','Sun 10 May 2015 13:54:36 -0000')
        self.assertEqual(result,'25200')

if __name__=='__main__':
    unittest.main()