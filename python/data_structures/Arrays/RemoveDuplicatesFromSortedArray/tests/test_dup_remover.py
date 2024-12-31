""" Unit test script. """

from unittest import TestCase

from src.dup_remover import DupRemover


class TestDupRemover(TestCase):

    def setUp(
        self,
    ):
        self.case1_arr = [1, 1, 2]
        self.case2_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    def test_remove_duplicates(
        self,
    ) -> None:

        result1 = DupRemover.remove_duplicates(nums=self.case1_arr)
        result2 = DupRemover.remove_duplicates(nums=self.case2_arr)

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 5)
