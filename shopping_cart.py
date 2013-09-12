class shop_items(object):
	def _init_(self, name, total, number_items):
		self.name = name
		self.total = total
		self.number_items = number_items

	def addTotalAmount(self, total, number):
		totalAmount = total*number
		return totalAmount
		

class shopping_cart(shop_items):
	pass
	

		