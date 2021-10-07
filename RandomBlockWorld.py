import random 

from Block import Block 
from PossibleMove import PossibleMove 

class RandomBlockWorld:
	blockWorldList = []

	def __init__(self):
		"""
		params: None
		returns: None
		what it does: builds game state
		"""
		self.numSpaces = random.randint(3, 10)
		self.numBlocks = random.randint(3, 10)

		print("Number of Spaces: " + str(self.numSpaces))
		print("Number of Blocks: " + str(self.numBlocks))

		# add possible spaces for blocks
		for i in range(0, self.numSpaces):
			self.blockWorldList.append(list())

		# add blocks 
		for i in range(1, self.numBlocks+1):
			# find a random position to put each block
			blockPlacePos = random.randint(0, self.numSpaces-1)
			self.blockWorldList[blockPlacePos].append(Block(i, blockPlacePos))


	def makeMove(self):
		"""
		params: None
		returns: None
		what it does: makes a random moveable block move
		"""
		possibleMoves = [] 

		# search each space for a "top" block to add to the movable block list
		for i in range(len(self.blockWorldList)):
			if(len(self.blockWorldList[i]) > 0):
				currBlock = self.blockWorldList[i][len(self.blockWorldList[i]) - 1]
				if(i == 0):
					possibleMoves.append(PossibleMove(currBlock, i+1))
				elif(i == self.numSpaces-1):
					possibleMoves.append(PossibleMove(currBlock, i-1))
				else:
					possibleMoves.append(PossibleMove(currBlock, i+1))
					possibleMoves.append(PossibleMove(currBlock, i-1))

		# print all possible moves
		print("Possible Moves: ")
		for move in possibleMoves:
			print(move)

		# select a random move to make and then make it
		randMove = random.randint(0, len(possibleMoves) - 1)
		selectedMove = possibleMoves[randMove]
		blockGettingMoved = selectedMove.getBlock()

		print("\nMoving: " + str(selectedMove))

		# because we know the block being moved is at the end of the list 
		# find list size and pop end
		indexSizeAtBlock = len(self.blockWorldList[blockGettingMoved.getCurrIndex()])
		self.blockWorldList[blockGettingMoved.getCurrIndex()].pop()

		# append to new index
		self.blockWorldList[selectedMove.getMoveIndex()].append(blockGettingMoved)

		blockGettingMoved.setCurrIndex(selectedMove.getMoveIndex())

	def pollWinState(self):
		"""
		params: None
		returns: None
		what it does: polls the status of the game to see if it has been won
		"""
		for i in range(0, self.numSpaces):
			inOrderCount = 0

			for block in self.blockWorldList[i]:
				if(block.getBlockNum() == inOrderCount):
					inOrderCount += 1

			if(inOrderCount == self.numBlocks):
				return True

		return False


	def printListState(self):
		"""
		params: None
		returns: None
		what it does: prints current state of blockWorldList
		"""
		for i in range(self.numSpaces):
			builtStrRow = str(i) + "| "
			for j in range(len(self.blockWorldList[i])):
				builtStrRow += "[" + str(self.blockWorldList[i][j]) + "] "
			print(builtStrRow)


	def run(self):
		"""
		params: None
		returns: None
		what it does: runs the main blockworld loop, counts total runs and returns
		"""
		totalRuns = 0

		while(self.pollWinState() == False):
			print("-----------------------------------------------------------")
			self.printListState()
			self.makeMove()
			print("\n")
			totalRuns += 1

		return totalRuns

