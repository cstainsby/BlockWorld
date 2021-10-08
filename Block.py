
# this class holds all relevant info for each block
class Block:
	# constructor
	def __init__(self, blockNum, currIndex):
		self.blockNum = blockNum
		self.currIndex = currIndex

	# toString method
	def __str__(self):
		return str(self.blockNum)

	# get the block's number
	def getBlockNum(self):
		return self.blockNum

	# get the block's current index
	def getCurrIndex(self):
		return self.currIndex

	# setter for current index
	def setCurrIndex(self, currIndex):
		self.currIndex = currIndex