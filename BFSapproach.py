from TreeDataStruct import Tree, Node
from Block import Block 
from PossibleMove import PossibleMove 
from SmartApproach import SmartApproach

import copy

class BFSapproach(SmartApproach):
	def __init__(self, numSpaces, numBlocks):
		super().__init__(numSpaces, numBlocks)
		self.exploredStates = []    # codes of explored states that should be avoided
		self.possibleStates = []	# the queue that is used to coordinate the next movement of the BFS search
		self.gameEndFound = False   # flag that indicates the game being over, begins backtracking
		self.victoryPath = []		# the shortest path 
		#self.moveTree = Tree()		# moveTree follows which moves were taken, allows us to backtrack to find shortest path


	def BFS(self, intialState):
		initCode = self.getCodeFromState(intialState)
		self.possibleStates.append(initCode)

		self.BFS_Recurse()

		victoryPath.reverse()

		print(victoryPath)


	def BFS_Recurse(self):
		# check to see if won, if true return
		if(len(self.possibleStates) <= 0):
			return

		currStateCode = self.possibleStates.pop(0)
		currState = self.getStateFromCode(currStateCode)

		if(pollWinState(currState) == True):
			self.gameEndFound = True
			return 

		# 1) find all possible moves
		possibleMoves = buildPossibleMoves(currState)
		for possibleMove in possibleMoves:
			# check possible states for being valid 
			newState = generateBoardState(currState, possibleMove)

			newStateCode = getCodeFromState(newState)

			# validate code 
			if not (self.exploredStates.contains(newStateCode)):
				self.exploredStates.append(newStateCode)
				self.possibleStates.append(newStateCode)

		self.BFS_Recurse()

		if(gameEndFound == True):
			victoryPath.append(possibleStates)




