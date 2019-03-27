# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from enum import Enum
class Status(Enum):
    UNDISCOVERED = 0
    DISCOVERED = 1
    VISITED = 2

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    waiting_list = util.Stack()
    visited = util.Counter()  # Use dictionary
    # [father's state(x,y position), action needed from father to it, cost to get it, status]
    start = problem.getStartState()  # For future use
    state = start
    visited[state] = [state, 0, 0, Status.VISITED]  # Add it into the visited list
    successors = problem.getSuccessors(state)
    for successor in successors:
        visited[successor[0]] = [state, successor[1], successor[2], Status.DISCOVERED]
        waiting_list.push(successor)
    state = waiting_list.pop()[0]

    while (not problem.isGoalState(state)):
        visited[state][3] = Status.VISITED
        successors = problem.getSuccessors(state)
        for successor in successors:
            if successor[0] not in visited or visited[successor[0]][3] != Status.VISITED:
                visited[successor[0]] = [state, successor[1], successor[2], Status.DISCOVERED]
                waiting_list.push(successor)
        if waiting_list.isEmpty():
            break
        state = waiting_list.pop()[0]
    actions = util.Queue()
    while not state == start:
        father = visited[state]
        motion = father[1]
        # for i in range(0, father[2]): one step once, so no need of cost
        actions.push(motion)
        state = father[0]

    return actions.list
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    waiting_list = util.Queue()
    start = problem.getStartState()
    state = start
    # print("start:", start)
    visited = util.Counter()
    visited[state] = [state, 0, 0, Status.VISITED]
    successors = problem.getSuccessors(state)
    for successor in successors:
        visited[successor[0]] = [state, successor[1], successor[2], Status.DISCOVERED]
        waiting_list.push(successor)
        # print("sons:", successor)
    state = waiting_list.pop()[0]
    while (not problem.isGoalState(state)):
        # print("state:", state)
        visited[state][3] = Status.VISITED
        successors = problem.getSuccessors(state)
        for successor in successors:
            if successor[0] not in visited: # or visited[successor[0]][3] != Status.VISITED:
                visited[successor[0]] = [state, successor[1], successor[2], Status.DISCOVERED]
                waiting_list.push(successor)
                # print("sons:", successor)
        if waiting_list.isEmpty():
            break
        state = waiting_list.pop()[0]
    actions = util.Queue()
    while not state == start:
        # print("decide:", state)
        father = visited[state]
        # motion = father[1]
        # for i in range(0, father[2]):
        actions.push(father[1])
        state = father[0]

    return actions.list
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    waiting_list = util.PriorityQueue()
    start = problem.getStartState()
    state = start
    visited = util.Counter()
    # [father's state, action from father to get there, cost from start to get there]
    visited[state] = [state, 0, 0]
    successors = problem.getSuccessors(state)
    for successor in successors:
        visited[successor[0]] = [state, successor[1], successor[2]]
        waiting_list.update(successor, successor[2])
    state = waiting_list.pop()[0]
    while (not problem.isGoalState(state)):
        cost_present = visited[state][2]
        successors = problem.getSuccessors(state)
        for successor in successors:
            cost_new = cost_present + successor[2]
            if successor[0] not in visited or (visited[successor[0]][2] > cost_new):
                visited[successor[0]] = [state, successor[1], cost_new]
                waiting_list.update(successor, cost_new)
        if waiting_list.isEmpty():
            return []
        state = waiting_list.pop()[0]
    actions = util.Queue()
    while not state == start:
        father = visited[state]
        # motion = father[1]
        # for i in range(0, father[2]):
        actions.push(father[1])
        state = father[0]

    return actions.list
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    waiting_list = util.PriorityQueue()
    start = problem.getStartState()
    state = start
    visited = util.Counter()
    # [father's state, action from father to get there, cost from start to get there]
    visited[state] = [state, 0, 0]
    successors = problem.getSuccessors(state)
    for successor in successors:
        visited[successor[0]] = [state, successor[1], successor[2]]
        waiting_list.update(successor, successor[2] + heuristic(successor[0], problem))
    state = waiting_list.pop()[0]
    while (not problem.isGoalState(state)):
        cost_present = visited[state][2]
        successors = problem.getSuccessors(state)
        for successor in successors:
            cost_new = cost_present + successor[2]
            if successor[0] not in visited or (visited[successor[0]][2] > cost_new):
                visited[successor[0]] = [state, successor[1], cost_new]
                waiting_list.update(successor, cost_new + heuristic(successor[0], problem))
        if waiting_list.isEmpty():
            return []
        state = waiting_list.pop()[0]
    actions = util.Queue()
    while not state == start:
        father = visited[state]
        # motion = father[1]
        # for i in range(0, father[2]):
        actions.push(father[1])
        state = father[0]

    return actions.list
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
