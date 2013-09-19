class Cart(object):
	items_in_cart = {}
	total = 0
	def __init__(self, customer_name):
		self.customer_name = customer_name
	
	def grandTotal(self):
		for i in self.items_in_cart:
			self.total += self.items_in_cart[i]
		print "The total is %s" %(str(self.total))

	def addItem(self, items,price):
		self.items_in_cart[items] = price
		print "Added %s in cart" %(items)

	def clearCart(self):
		self.items_in_cart = {}
		print self.items_in_cart

class Items(object):
	def __init__(self, item, price):
		self.items = item
		self.price = price

class Fruit(Items):
	IamAFruit = True

class Vegetables(Items):
	IamAVeggie = True

print Cart.items_in_cart

banana = Fruit('banana', 2)
print banana.items
add_to_cart = Cart('tina')
print add_to_cart.addItem(banana.items, banana.price)
print "print cart", add_to_cart.items_in_cart

cucumber = Vegetables('cucumber', 3)
print add_to_cart.addItem(cucumber.items, cucumber.price)
print "print cart", add_to_cart.items_in_cart

add_to_cart.grandTotal()
	









