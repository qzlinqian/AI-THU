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
                value -= 41
            ghostDis = manhattanDistance(newPos, ghostPos)
            if (ghostDis > ghostState.scaredTimer):
                value -= 40/ghostDis
        foodList = currentFood.asList()
        foodDis = [manhattanDistance(newPos, food) for food in foodList]
        nearestFood = min(foodDis)
        if (nearestFood == 0):
            value += 41
        else:
            value += 40/nearestFood
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
        agentNum = gameState.getNumAgents()

        gameTree = [[-1, 0, gameState, 0, -1],]
        start = 0
        end = 1
        boudaries = [-1,0,]
        # Build the tree by layers. Every gameState.getNumAgents layers form a group
        # Expand the former layer to build the tree
        for currentDepth in range(0, self.depth):
            for j in range(0, agentNum):
                for nodeOrder in range(start, end):
                    actions = gameTree[nodeOrder][2].getLegalActions(j)
                    for action in actions:
                        nextState = gameTree[nodeOrder][2].generateSuccessor(j, action)
                        gameTree.append([nodeOrder, len(gameTree), nextState, action, j])
                start = end
                end = len(gameTree)
                boudaries.append(start)

        # The final (start, end) is the last layer
        valueDict = {}
        while start == end:
            start = boudaries.pop()
        while start > -1:
            for nodeOrder in range(start, end):
                fatherOrder = gameTree[nodeOrder][0]
                agent = gameTree[nodeOrder][4]
                if nodeOrder in valueDict:
                    value = valueDict[nodeOrder][0]
                else:
                    value = self.evaluationFunction(gameTree[nodeOrder][2])
                    valueDict[nodeOrder] = [value, -1]
                if agent == 0:
                    #Pacman
                    if (fatherOrder not in valueDict) or (valueDict[fatherOrder][0] < value):
                        valueDict[fatherOrder] = [value, nodeOrder]
                else:
                    #Ghost
                    if (fatherOrder not in valueDict) or (valueDict[fatherOrder][0] > value):
                        valueDict[fatherOrder] = [value, nodeOrder]
                # if newStart > fatherOrder:
                    # newStart = fatherOrder   #Or some leaf nodes at the begining of a non-buttom layer would be left out
            end = start
            start = boudaries.pop()

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

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        result = self.miniMaxProne(gameState, 0, 0, float("-inf"), float("inf"))
        # print(result[0])  # Why the value is not the same as the doc?
        return result[1]
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def expectimaxSearch(self, gameState, agent, depth):
        depthNum = self.depth
        agentNum = gameState.getNumAgents()
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
            bestVal = float("-inf")
            for action in actions:
                value = self.expectimaxSearch(gameState.generateSuccessor(agent, action), newAgent, newDepth)[0]
                if bestVal < value:
                    bestVal = value
                    bestAction = action
            return [bestVal, bestAction]
        else:
            valueSum = 0
            for action in actions:
                valueSum += self.expectimaxSearch(gameState.generateSuccessor(agent, action), newAgent, newDepth)[0]
            return [valueSum/len(actions), 0]


    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        result = self.expectimaxSearch(gameState, 0, 0)
        return result[1]
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    position = currentGameState.getPacmanPosition()
    foodGrid = currentGameState.getFood()
    ghostStates = currentGameState.getGhostStates()
    foodDis = [manhattanDistance(position, food) for food in foodGrid]
    if len(foodGrid.asList()) == 0:
        return len(ghostStates)+5
    xList, yList = zip(*foodGrid.asList())
    left = min(xList)
    right = max(xList)
    top = max(yList)
    bottom = min(yList)
    cost = top - bottom + right - left
    top = abs(top - position[1])
    bottom = abs(bottom - position[1])
    left = abs(left - position[0])
    right = abs(right - position[0])
    if top > bottom:
        cost += bottom
    else:
        cost += top
    if left > right:
        cost += right
    else:
        cost += left
    value = len(ghostStates)/cost - len(xList)
    # value = 4/(sum(foodDis))

    ghostDis = [manhattanDistance(position, ghostState.getPosition()) for ghostState in ghostStates]
    for index in range(0, len(ghostStates)):
        dis = manhattanDistance(position, ghostStates[index].getPosition())
        if dis == 0:
            value -= 6
        else:
            if dis < 6 and ghostStates[index].scaredTimer < dis:
                value -= 4/dis

    return value
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
