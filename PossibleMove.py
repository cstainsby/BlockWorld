from Block import Block

class PossibleMove:
	# constructor
	def __init__(self, block, moveIndex):
		self.block = block
		self.moveIndex = moveIndex

	# toString function
	def __str__(self):
		return "Block " + str(self.block.getBlockNum()) + ": " + str(self.block.getCurrIndex()) + " -> " + str(self.moveIndex)

	# getter for index to move to
	def getMoveIndex(self):
		return self.moveIndex

	# getter for block
	def getBlock(self):
		return self.block