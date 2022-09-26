import unittest
import merge_the_tools.core.core as m


class Testsample_merge(unittest.TestCase):
    def test_mutations(self):
        result = m.merge_the_tools("AABCAAADA",3)

        self.assertEqual(result,None)
if __name__ == '__main__':
    unittest.main()
