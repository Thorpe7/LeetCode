from unittest import TestCase

from src.best_time_buy_sell_stock import StockBuySell


class TestStocks(TestCase):
    def setUp(
        self,
    ):
        self.case1_solution = 5
        self.case2_solution = 0
        self.case3_solution = 1

    def test_case_one(
        self,
    ):
        myStockClass1 = StockBuySell()
        result1 = myStockClass1.maxProfit(
            prices=[7, 1, 5, 3, 6, 4],
        )
        self.assertEqual(self.case1_solution, result1)

    def test_case_two(
        self,
    ):
        myStockClass2 = StockBuySell()
        output2 = myStockClass2.maxProfit(prices=[7, 6, 4, 3, 1])
        self.assertEqual(self.case2_solution, output2)

    def test_case_three(
        self,
    ):
        myStockClass3 = StockBuySell()
        output3 = myStockClass3.maxProfit(prices=[1, 2])
        self.assertEqual(self.case3_solution, output3)
