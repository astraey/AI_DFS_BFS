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

def depthFirstSearch(problem,):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    """AQUI SE HACE TODO EL PRIMER EJERCICIO, recordar que hay que usar stack"""

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** OUR CODE IS HERE ***"
    """
    procedure DFS - iterative(G, v):
    let S be a stack
    S.push(v)
    while S is not empty
        v = S.pop()
        if v is not labeled as discovered:
            label v as discovered
        for all edges from v to w in G.adjacentEdges(v) do
        S.push(w)
    """
    S = util.Stack()
    visitados = []
    S.push((problem.getStartState(), []))
    while not S.isEmpty():

        estado, padres = S.pop()
        if estado not in visitados:
            visitados.append(estado)
        sucesores = problem.getSuccessors(estado)
        for i in range(0, len(sucesores)):
            print estado
            if problem.isGoalState(sucesores[i][0]):
                print "goal reached"
                print "padres en goal"
                print padres
                print "ultima direccion"
                print sucesores[i][1]
                print padres

                return padres + [sucesores[i][1]]
            if sucesores[i][0] not in visitados:
                print "sucesor added"
                print sucesores[i][0]
                print "direccion sucesores"
                print compassAdapter(sucesores[i][1])
                S.push((sucesores[i][0], padres + [sucesores[i][1]]))
    return []


def compassAdapter(direction):

    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    if direction is "North":
        return n

    if direction is "South":
        return s

    if direction is "East":
        return e

    if direction is "West":
        return w


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    S = util.Queue()
    visitados = []
    S.push((problem.getStartState(), []))
    while not S.isEmpty():

        estado, padres = S.pop()
        if estado not in visitados:
            visitados.append(estado)
        sucesores = problem.getSuccessors(estado)
        for i in range(0, len(sucesores)):
            print estado
            if problem.isGoalState(sucesores[i][0]):
                print "goal reached"
                print "padres en goal"
                print padres
                print "ultima direccion"
                print sucesores[i][1]
                print padres

                return padres + [sucesores[i][1]]
            if sucesores[i][0] not in visitados:
                print "sucesor added"
                print sucesores[i][0]
                print "direccion sucesores"
                print compassAdapter(sucesores[i][1])
                S.push((sucesores[i][0], padres + [sucesores[i][1]]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    S = util.PriorityQueue()
    visitados = []
    S.push((problem.getStartState(), []), 0)
    while not S.isEmpty():
        print "S"
        print S
        estado, padres = S.pop()

        print "estado"
        print estado
        print "padres"
        print padres
        if estado not in visitados:
            visitados.append(estado)
        sucesores = problem.getSuccessors(estado)
        for i in range(0, len(sucesores)):
            print estado
            if problem.isGoalState(sucesores[i][0]):
                print "goal reached"
                print "padres en goal"
                print padres
                print "ultima direccion"
                print sucesores[i][1]
                print padres

                return padres + [sucesores[i][1]]
            if sucesores[i][0] not in visitados:
                print "sucesor added"
                print sucesores[i][0]
                print "direccion sucesores"
                print compassAdapter(sucesores[i][1])
                S.push((sucesores[i][0], padres + [sucesores[i][1]]), problem.getCostOfActions(padres + [sucesores[i][1]]))
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    S = util.PriorityQueue()
    visitados = []
    S.push((problem.getStartState(), []), 0)
    while not S.isEmpty():
        print "S"
        print S
        estado, padres = S.pop()

        print "estado"
        print estado
        print "padres"
        print padres
        if estado not in visitados:
            visitados.append(estado)
        sucesores = problem.getSuccessors(estado)
        for i in range(0, len(sucesores)):
            print estado
            if problem.isGoalState(sucesores[i][0]):
                print "goal reached"
                print "padres en goal"
                print padres
                print "ultima direccion"
                print sucesores[i][1]
                print padres

                return padres + [sucesores[i][1]]
            if sucesores[i][0] not in visitados:
                print "sucesor added"
                print sucesores[i][0]
                print "direccion sucesores"
                print compassAdapter(sucesores[i][1])
                S.push((sucesores[i][0], padres + [sucesores[i][1]]),
                       problem.getCostOfActions(padres + [sucesores[i][1]]) + heuristic(sucesores[i][0], problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
