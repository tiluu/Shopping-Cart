import unittest

from shopping_cart import shopping_cart, shop_items

class test_shop_items(unittest.TestCase):

	def setUp(self):
		self.shopItems= shop_items()
		self.name ='banana'
		self.total = 5.2
		self.number = 2

	def test_item_final_amount(self):
		grandTotal = self.shopItems.addTotalAmount(self.total, self.number)
		self.assertEqual(10.4, grandTotal) 

	def test_item_is_string(self):
		self.assertIsInstance(self.name, str)

