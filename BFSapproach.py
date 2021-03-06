from Block import Block 
from PossibleMove import PossibleMove 
from SmartApproach import SmartApproach

import copy

class BFSapproach(SmartApproach):
	def __init__(self, numSpaces, numBlocks):
		super().__init__(numSpaces, numBlocks)
		self.exploredStates = []    # codes of explored states that should be avoided
		self.possibleStates = []	# the queue that is used to coordinate the next movement of the BFS search


	def BFS(self, initialState):
		self.possibleStates.append(initialState)
		self.exploredStates.append(self.getCodeFromState(initialState))

		self.printListState(initialState)
		turnCount = 0 

		while(len(self.possibleStates) > 0):

			currState = self.possibleStates.pop(0)

			if(self.pollWinState(currState) == True):
				self.gameEndFound = True
				print("Won")
				self.printListState(currState)
				return 

			# find all possible moves
			possibleMoves = self.buildPossibleMoves(currState)
			usableMoveCount = 0
			for possibleMove in possibleMoves:
				# check possible states for being valid 
				newState = self.generateBoardState(currState, possibleMove)

				# if board state was already explored
				if(self.exploredStates.count(self.getCodeFromState(newState)) == 0):
					usableMoveCount += 1
					self.possibleStates.append(newState)
					self.exploredStates.append(self.getCodeFromState(newState))

			print("possible moves: " + str(len(possibleMoves)))
			print("useable moves: " + str(usableMoveCount))
			print("in queue: " + str(len(self.possibleStates)))
			self.printListState(currState)

	




