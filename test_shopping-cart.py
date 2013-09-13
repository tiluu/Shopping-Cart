import unittest

from shopping_cart import Cart, Items

class test_shop_items(unittest.TestCase):

	def setUp(self):
		self.shopItems = Items('bananasdfa',3)
		
		self.name ='banana'
		self.total = 5.2

	def test_add_item_to_cart(self):
		self.shopItems.addItem()
		print self.shopItems.items_in_cart
		self.assertIsInstance(self.name, self.shopItems.items_in_cart)
	#def test_item_final_amount(self):
	#	grandTotal = self.shopItems.addTotalAmount(self.total, self.number)
	#	self.assertEqual(10.4, grandTotal) 

	#def test_item_is_string(self):
	#	self.assertIsInstance(self.name, str)

	#class test_shopping_cart(unittest.TestCase):
	#def test_add_items_to_cart(self):




