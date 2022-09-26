import disjoints_sets.core.core as dj
import unittest
#create a class for testing

class test_disjoints(unittest.TestCase):
    def test_sample(self):
        result=dj.disjoint([1,5,3],[3,1],[5,7])
        self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()
