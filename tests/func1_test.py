from unittest import TestCase, main
import func1



class Func1Test(TestCase):
    def test1_s_sum(self):
        self.assertEqual(func1.s_sum([2, 3, 5, 6]), 16, "Should be 16")

    def test2_s_sum(self):
        self.assertEqual(func1.s_sum([]), None, "Should be None")

if __name__ == '__main__':
    main()
