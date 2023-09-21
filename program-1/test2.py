import unittest
from code2 import max_stock_profit

class TestMaxStockProfit(unittest.TestCase):
    def test_empty_prices(self):
        # Test that the function returns -1 for an empty list of prices
        self.assertEqual(max_stock_profit([]), -1)
        
    def test_single_price(self):
        # Test that the function returns -1 for a list of prices with only one element
        self.assertEqual(max_stock_profit([100]), -1)
        
    def test_no_profit(self):
        # Test that the function returns -1 when no profit can be made
        self.assertEqual(max_stock_profit([100, 90, 80, 70, 60]), -1)
        
    def test_max_profit(self):
        # Test that the function returns the correct result for a list of prices with a maximum profit
        self.assertEqual(max_stock_profit([100, 180, 260, 310, 40, 535, 695]), "Buy on day 5 at price 40\nSell on day 7 at price 695\nMax profit: 655")
        
    def test_duplicate_prices(self):
        # Test that the function returns the correct result for a list of prices with duplicate values
        self.assertEqual(max_stock_profit([100, 180, 260, 310, 310, 535, 695]), "Buy on day 1 at price 100\nSell on day 7 at price 695\nMax profit: 595")
