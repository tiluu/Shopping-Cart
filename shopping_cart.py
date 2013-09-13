class Cart(object):
	items_in_cart = {}
	total = 0
	def __init__(self, customer_name):
		self.customer_name = customer_name
	
	def grandTotal(self):
		for i in self.items_in_cart:
			self.total += self.items_in_cart[i]
		print "The total is %s" %(str(self.total))

class Items(Cart):
	def __init__(self, item, price):
		self.items = item
		self.price = price
	def addItem(self):
		self.items_in_cart[self.items] = self.price
		print "Added %s in cart" %(self.items)

my_cart = Cart('tina')
things = Items('tina', 3)
things.addItem()
things2 = Items('banana', 3)
things2.addItem()
my_cart.grandTotal()








