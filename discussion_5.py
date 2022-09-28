import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max = 0
		for i in range(len(self.items)):
			if self.items[i].stock > max:
				max = self.items[i].stock
				max_item = self.items[i]
		return max_item
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max = 0
		for i in range(len(self.items)):
			if self.items[i].price > max:
				max = self.items[i].price
				max_item = self.items[i]
		return max_item	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(0, count_a(self.item1.name), "Testing Beer")
		self.assertEqual(0, count_a(self.item2.name), "Testing Cider")
		self.assertEqual(1, count_a(self.item3.name), "Testing Water")
		self.assertEqual(2, count_a(self.item4.name), "Testing Fanta")
		self.assertEqual(2, count_a(self.item5.name), "Testing CocaCola")

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse = Warehouse()

		self.warehouse.add_item(self.item1)
		self.assertEqual([self.item1], self.warehouse.items, "Testing  one-item list")

		self.warehouse.add_item(self.item2)
		self.assertEqual([self.item1, self.item2], self.warehouse.items, "Testing two-item list")

		self.warehouse.add_item(self.item3)
		self.warehouse.add_item(self.item4)
		self.warehouse.add_item(self.item5)
		self.assertEqual(5, len(self.warehouse.items), "Testing length of five-item list")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouse1 = Warehouse()
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item3)
		self.warehouse1.add_item(self.item4)
		self.warehouse1.add_item(self.item5)
		self.assertTrue(self.warehouse1.get_max_stock() == self.item3)

		self.warehouse2 = Warehouse()
		self.warehouse2.add_item(self.item1)
		self.assertTrue(self.warehouse2.get_max_stock() == self.item1)

		self.warehouse3 = Warehouse()
		self.warehouse3.add_item(self.item1)
		self.warehouse3.add_item(self.item4)
		self.assertTrue(self.warehouse3.get_max_stock().stock == self.item4.stock)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.warehouse1 = Warehouse()
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item3)
		self.warehouse1.add_item(self.item4)
		self.warehouse1.add_item(self.item5)
		self.assertTrue(self.warehouse1.get_max_price() == self.item1)

		self.warehouse2 = Warehouse()
		self.warehouse2.add_item(self.item5)
		self.assertTrue(self.warehouse2.get_max_price() == self.item5)

		self.warehouse3 = Warehouse()
		self.warehouse3.add_item(self.item3)
		self.warehouse3.add_item(self.item4)
		self.assertTrue(self.warehouse3.get_max_price().price == self.item4.price)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()
