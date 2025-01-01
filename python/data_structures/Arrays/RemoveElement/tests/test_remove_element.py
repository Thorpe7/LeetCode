from unittest import TestCase
from src.remove_element import ElementRemover


class TestRemover(TestCase):
    def setUp(
        self,
    ):
        self.case1_solution = 2
        self.case2_solution = 5

    def test_case_one(self):
        tmpRemover = ElementRemover()
        result1 = tmpRemover.remove_element(nums=[3, 2, 2, 3], val=3)
        self.assertEqual(self.case1_solution, result1)

    def test_case_two(self):
        tmpRemover = ElementRemover()
        result2 = tmpRemover.remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
        self.assertEqual(self.case2_solution, result2)
