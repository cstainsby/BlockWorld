
from TreeDataStruct import Tree, Node
from Block import Block 
from PossibleMove import PossibleMove 
from BFSapproach import BFSapproach as bfs

import copy
import random 



class SmartBlockWorld():
	blockWorldList = []
	# this will act like a stack because the more recent the board state
	# the more likley the computer might try to repeat it(limits search time)
	previousBoardStatesStack = []

	def __init__(self):
		"""
		params: None
		returns: None
		what it does: sets up the tree for the smart blockworld game
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

		approach = bfs(self.numSpaces, self.numBlocks)

		approach.BFS(self.blockWorldList)