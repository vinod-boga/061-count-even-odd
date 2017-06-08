from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution([1, 2, 3, 5, 8, 9])

        self.assertEqual(res['ODD'], 4)
        self.assertEqual(res['EVEN'], 2)
