import numpy as np

import mean_var_std.core.core as m
import unittest
import numpy as np


class test_sample(unittest.TestCase):

    def test_mean(self):
        arr=np.array([[1,2],[3,4]])
        result=m.arr_mean(arr)
        p = np.array([1.5,3.5])
        self.assertIsNone(np.testing.assert_almost_equal(result,p,1)) #it returns None if the arrays are equal

    def test_var(self):
        arr=np.array([[1,2],[3,4]])
        q=np.array([1.,1.])
        result=m.arr_var(arr)
        self.assertIsNone(np.testing.assert_almost_equal(result,q,1))


    def test_std(self):
        arr=np.array([[1,2],[3,4]])
        result=m.arr_std(arr)
        self.assertEqual(result,1.11803398875)

if __name__ == '__main__':
    unittest.main()