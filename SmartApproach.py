from Block import Block 
from PossibleMove import PossibleMove 

import copy


class SmartApproach:
	def __init__(self, numSpaces, numBlocks):
		self.numSpaces = numSpaces
		self.numBlocks = numBlocks


	def generateBoardState(self, currState, move):
		newState = copy.deepcopy(currState)
		blockToBeMoved = move.getBlock
		whereTo = move.getMoveIndex
		
		# because we know the block being moved is at the end of the list 
		# find list size and pop end
		indexSizeAtBlock = len(newState[blockToBeMoved.getCurrIndex()])
		newState[blockToBeMoved.getCurrIndex()].pop()

		# append moved block to its new index
		newState[selectedMove.getMoveIndex()].append(blockGettingMoved)
		# set the block's index 
		blockGettingMoved.setCurrIndex(selectedMove.getMoveIndex())



	def buildPossibleMoves(self, gameStatus):
		possibleMoves = [] 

		# search each space for a "top" block to add to the movable block list
		for i in range(len(gameStatus)):
			if(len(gameStatus[i]) > 0):
				currBlock = gameStatus[i][len(gameStatus[i]) - 1]
				if(i == 0):
					possibleMoves.append(PossibleMove(currBlock, i+1))
				elif(i == self.numSpaces-1):
					possibleMoves.append(PossibleMove(currBlock, i-1))
				else:
					possibleMoves.append(PossibleMove(currBlock, i+1))
					possibleMoves.append(PossibleMove(currBlock, i-1))

		return possibleMoves



	def pollWinState(self, currState):
		"""
		params: None
		returns: None
		what it does: polls the status of the game to see if it has been won
		"""
		for i in range(0, self.numSpaces):
			inOrderCount = 0

			for block in currState[i]:
				if(block.getBlockNum() == inOrderCount):
					inOrderCount += 1

			if(inOrderCount == self.numBlocks):
				return True

		return False


	def getCodeFromState(self, boardStatus):
		statusString = ""
		# _ for next space
		# , for next 
		#O(N) operation to condense the memory impact of the program
		for i in range(self.numSpaces):
			statusString += "_"
			for j in range(len(boardStatus[i])):
				statusString += str(boardStatus[i][j]) + ","

		return statusString


	def getStateFromCode(self, statusCode):
		decodedStatus = [] 		# where the new status will be stored
		nextNum = ""			# used to read in numbers of varying size
		# _ for next space
		# , for next 
		#O(N) operation to condense the memory impact of the program
		for i in range(0, len(statusCode)):
			# either a '_', ',' or an integer
			if(statusCode[i] == '_'):
				decodedStatus.append(list())
			elif(statusCode[i] == ','):
				# add the currently compiled number and flush it out of nextNum
				decodedStatus[len(decodedStatus) - 1].append(int(nextNum))
				nextNum.clear()
			else:
				nextNum += statusCode[i]

		return decodedStatus