import min_max.core.core as m
import unittest

class testsample(unittest.TestCase):
    def test_mutations(self):
        k=[[4,2],[2,5],[3,7],[1,3],[4,0]]
        result= m.min_max(k)
        self.assertEqual(result,3)

if __name__ == '__main__':
    unittest.main()
