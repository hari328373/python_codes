import word_order.core.core as w
import unittest

class testcase(unittest.TestCase):
    def test_word(self):
        n=4
        i = ['bcdef','abcdefg','bcde','bcdef']
        o=[2,1,1]
        result= w.word_order(n,i)
        self.assertEqual(result,o)

if __name__ == '__main__':
    unittest.main()