from unittest import TestCase, main
import func1

def s_sum(lst):
    return sum(lst)

class TestSum(unittest.TestCase):
    def test_list_sum(self):
        self.assertEqual(main.s_sum([2, 3, 5, 6]), 16, "Should be 16")

if __name__ == '__main__':
    unittest.main()
