
class Node(object):
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_next):
		self.next = new_next

class UnorderedList(object):
	def __init__(self):
		self.head = None
		self.first = None

	def is_empty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		if self.first == None:
			self.first = temp
		
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()

		return count

	def search(self, item):
		current = self.head
		found = False

		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()

		return found


	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def append(self, item):
		current = self.head

		while current.get_next() != None:
			current = current.get_next()

		current.set_next(Node(item))
	