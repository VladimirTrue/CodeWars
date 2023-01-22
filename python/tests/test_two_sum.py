from unittest import TestCase
from python.scripts import two_sum as ts


class Test(TestCase):
    def test_two_sum(self):
        self.assertEqual(sorted(ts.two_sum([1, 2, 3], 4)), [0, 2])
        self.assertEqual(sorted(ts.two_sum([1234, 5678, 9012], 14690)), [1, 2])
        self.assertEqual(sorted(ts.two_sum([2, 2, 3], 4)), [0, 1])
        self.assertEqual(sorted(ts.two_sum([3, 2, 2], 4)), [1, 2])
