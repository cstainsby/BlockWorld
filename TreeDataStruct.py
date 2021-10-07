


# full implementation because why not right?
class Tree():
	def __init__(self, root):
		"""
		params: The root Node to the tree
		returns: None
		what it does: sets up root node and its connections
		"""
		self.root = root
		self.children = []
		self.numNodes = 0


	def addChild(self, item):
		self.children.append(item)


	def removeChild(self, item):
		if not isEmpty:
			try:
				self.children.remove(item)
				return True
			except ValueError:
				return False
		return False


	def isEmpty(self):
		if(self.numNodes <= 0):
			return True
		else:
			return False 


class Node():
	def __init__(self, data):
		self.data = data
		self.children = []
		self.numNodes = 0


	def addChild(self, item):
		self.children.append(item)


	def removeChild(self, item):
		if not isEmpty:
			try:
				self.children.remove(item)
				return True
			except ValueError:
				return False
		return False


	def isEmpty(self):
		if(self.numNodes <= 0):
			return True
		else:
			return False 

