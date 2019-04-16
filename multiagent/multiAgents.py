# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        # print(bestIndices)
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        # print(legalMoves[chosenIndex])

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        currentFood = currentGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        value = 0
        for ghostState in newGhostStates:
            ghostPos = ghostState.getPosition()
            if (ghostPos == newPos):
                # print("0")
                value -= 41
            ghostDis = manhattanDistance(newPos, ghostPos)
            if (ghostDis > ghostState.scaredTimer):
                value -= 40/ghostDis
        foodList = currentFood.asList()
        # print(foodList)
        foodDis = [manhattanDistance(newPos, food) for food in foodList]
        nearestFood = min(foodDis)
        # print("nearestFood",nearestFood)
        if (nearestFood == 0):
            # print("yes")
            value += 41
        else:
            value += 40/nearestFood
        # print(value)
        return value
        # return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # if gameState.isLose():
            # return []
        # if gameState.isWin():
            # return []
        # print("New search.")
        agentNum = gameState.getNumAgents()

        gameTree = [[-1, 0, gameState, 0, -1],]
        start = 0
        end = 1
        boudaries = [-1,0,]
        #Build the tree by layers. Every gameState.getNumAgents layers form a group
        #Expand the former layer to build the tree
        for currentDepth in range(0, self.depth):
            # newStack = []
            # end = len(gameTree)
            for j in range(0, agentNum):
                for nodeOrder in range(start, end):
                    actions = gameTree[nodeOrder][2].getLegalActions(j)
                    for action in actions:
                        nextState = gameTree[nodeOrder][2].generateSuccessor(j, action)
                        gameTree.append([nodeOrder, len(gameTree), nextState, action, j])
                # if end < len(gameTree):
                start = end
                end = len(gameTree)
                boudaries.append(start)

        #The final (start, end) is the last layer
        valueDict = {}
        # print("start:", start, "end:", end)
        # for i in range(start, end):
            # value = self.evaluationFunction(gameTree[i][2])
            # valueDict[i] = [value, -1]

        # for currentDepth in range(self.depth-1, -1, -1):
            # for i in range(agentNum-1, -1, -1):
        # start = boudaries.pop()
        while start == end:
            start = boudaries.pop()
        while start > -1:
            # newStart = start
            for nodeOrder in range(start, end):
                fatherOrder = gameTree[nodeOrder][0]
                agent = gameTree[nodeOrder][4]
                # print("depth:", currentDepth, ", agent:", i, ", current node:", nodeOrder, ", father:", fatherOrder)
                # print(nodeOrder, "in dict ", nodeOrder in valueDict)
                # value = valueDict[nodeOrder][0]
                if nodeOrder in valueDict:
                    value = valueDict[nodeOrder][0]
                else:
                    value = self.evaluationFunction(gameTree[nodeOrder][2])
                    valueDict[nodeOrder] = [value, -1]
                    # continue
                if agent == 0:
                    #Pacman
                    if (fatherOrder not in valueDict) or (valueDict[fatherOrder][0] < value):
                        valueDict[fatherOrder] = [value, nodeOrder]
                        # print(fatherOrder, ":", valueDict[fatherOrder])
                else:
                    #Ghost
                    if (fatherOrder not in valueDict) or (valueDict[fatherOrder][0] > value):
                        valueDict[fatherOrder] = [value, nodeOrder]
                        # print(fatherOrder, ":", valueDict[fatherOrder])
                # if newStart > fatherOrder:
                    # newStart = fatherOrder   #Or some leaf nodes at the begining of a non-buttom layer would be left out
            end = start
            start = boudaries.pop()

        # actionList = []
        # nodeOrder = valueDict[0][1]
        # for depth in range(0, self.depth):
            # for i in range(0, agentNum):
        #     if nodeOrder == -1:
        #         if i == 0:
        #             return gameState.isWin()
        #         else:
        #             return gameState.isLose()
                # actionList.append(gameTree[nodeOrder][3])
                # print(i, gameTree[nodeOrder][3])
                # if i == 0:
                    # print(depth, valueDict[nodeOrder])
                # nodeOrder = valueDict[nodeOrder][1]
        # print(gameTree)
        # print(valueDict)
        # if len(valueDict) == 0:
            # return []
        node = valueDict[0][1]
        return gameTree[node][3]
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def miniMaxProne(self, gameState, agent, depth, alpha, beta):
        agentNum = gameState.getNumAgents()
        depthNum = self.depth
        # if (agent == (agentNum-1)) and (depth == (depthNum-1)):
        if (depth == depthNum):
            # Leaf
            return [self.evaluationFunction(gameState), 0]

        newAgent = agent+1
        newDepth = depth
        if newAgent == agentNum:
            newAgent -= agentNum
            newDepth += 1

        actions = gameState.getLegalActions(agent)
        if len(actions) == 0:
            return [self.evaluationFunction(gameState), 0]

        if agent == 0:
            # Max
            bestVal = float("-inf")
            for action in actions:
                value = self.miniMaxProne(gameState.generateSuccessor(agent, action), newAgent, newDepth, alpha, beta)[0]
                if value > bestVal:
                    bestVal = value
                    bestAction = action
                if alpha < bestVal:
                    alpha = bestVal
                if beta < alpha:
                    break
            return [bestVal, bestAction]
        else:
            # Min
            bestVal = float("inf")
            for action in actions:
                value = self.miniMaxProne(gameState.generateSuccessor(agent, action), newAgent, newDepth, alpha, beta)[0]
                if value < bestVal:
                    bestVal = value
                    bestAction = action
                if beta > bestVal:
                    beta = bestVal
                if beta < alpha:
                    break
            return [bestVal, bestAction]
        # else:
            # Others
            # bestVal = float("inf")
            # actions = gameState.getLegalActions(newAgent)
            # values = [miniMaxProne(gameState.generateSuccessor(newAgent, action), newAgent, newDepth, alpha, beta) for action in actions]
            # return min(values)

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # agentNum = gameState.getNumAgents
        # depth = self.depth
        # actions = gameState.getLegalActions(0)
        # for action in actions:
        # values = [self.miniMaxProne(gameState.generateSuccessor(0, action), 0, 0, float("-inf"), float("inf")) for action in actions]
        # alpha = float("-inf")
        # beta = float("inf")
        # bestVal = float("-inf")
        # for action in actions:
            # value = self.miniMaxProne(gameState.generateSuccessor(0, action), 0, 0, alpha, beta)
            # if value > bestVal:
                # bestVal = value
                # bestAction = action
        # print(values)
        # bestIndices = [index for index in range(len(values)) if values[index] == bestVal]
        # chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        # return actions[chosenIndex]
        # return bestAction
        result = self.miniMaxProne(gameState, 0, 0, float("-inf"), float("inf"))
        # print(result[0])  # Why the value is not the same as the doc?
        return result[1]

        # waitingList = []
        # valueDict = {}
        # gameTree = []

        # gameTree.append([gameState, -1, -1, -1, float("inf")])  # [state, father, agent, depth, value]
        # actions = gameState.getLegalActions()
        # waitingList.append([0, len(actions)])  # [node in tree, unexpanded nodes]
        # # for action in actions:
        #     # waitingList.append([gameState.generateSuccessor(0, action), 0, 0, 0])   # [state, father, agent, depth, unexpanded nodes]

        # while len(waitingList) > 0:
        #     newNode = waitingList[-1]
        #     # nodeNum = len(gameTree)
        #     if newNode[2] == agentNum-1 and newNode[3] == depth-1:
        #         # Leaf
        #         value = self.evaluationFunction(newNode[0])
        #         gameTree[newNode[0]][4] = value
        #         waitingList.pop()
        #         father = gameTree[newNode[0]][1]
        #     else:
        #         # gameTree.append([newNode, float("-inf")])
        #         currentAgent = newNode[2]+1
        #         currentDepth = newNode[3]
        #         if currentAgent == agentNum:
        #             currentAgent -= agentNum
        #             currentDepth += 1
        #         actions = newNode[0].getLegalActions(currentAgent)
        #         for action in actions:
        #             waitingList.append([newNode[0].generateSuccessor(currentAgent, action), nodeNum, currentAgent, currentDepth])

        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
