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

    stack = util.Stack()
    w, h = 5, 5
    padres = [[0 for x in range(w)] for y in range(h)]

    visited = []


    stack.push(problem.getStartState())

    while not stack.isEmpty():

        # estado, accion
        estado = stack.pop()


        if not estado in visited:
            visited.append(estado)
            succesors = problem.getSuccessors(estado)
            print "Node Expanded Here"
            for i in range(0, len(succesors)):
                print "Objective: ", problem.isGoalState(succesors[i][0])
                print "Succesors ", succesors[i]
                print "direccion ", compassAdapter(succesors[i][1])
                print "State Pushed"

                stack.push(succesors[i][0])
                x,y = succesors[i][0]
                if not succesors[i][0] in visited: padres[x-1][y-1] = compassAdapter(succesors[i][1])

                """if padres[x-1][y-1] == "North":
                    padres[x-1][y-1] = "South"
                elif padres[x - 1][y - 1] == "South":
                    padres[x - 1][y - 1] = "North"
                elif padres[x - 1][y - 1] == "East":
                    padres[x - 1][y - 1] = "West"
                elif padres[x - 1][y - 1] == "West":
                    padres[x - 1][y - 1] = "East"
                """
                if (problem.isGoalState(succesors[i][0])):
                    result = []
                    x1, y1 = succesors[i][0]
                    state = x1, y1

                    for i in range(0, 5):
                        for j in range(0, 5):
                            if padres[i][j] == 0:
                                padres[i][j] = "nope"
                    print padres[4][0] + " " + padres[4][1] + " " + padres[4][2] + " " + padres[4][3] + " " + padres[4][
                        4]
                    print padres[3][0] + " " + padres[3][1] + " " + padres[3][2] + " " + padres[3][3] + " " + \
                          padres[3][4]
                    print padres[2][0] + " " + padres[2][1] + " " + padres[2][2] + " " + padres[2][3] + " " + \
                          padres[2][4]
                    print padres[1][0] + " " + padres[1][1] + " " + padres[1][2] + " " + padres[1][3] + " " + \
                          padres[1][4]
                    print padres[0][0] + " " + padres[0][1] + " " + padres[0][2] + " " + padres[0][3] + " " + \
                          padres[0][4]


                    #padres[0][0] = "West"
                    #padres[0][1] = "South"
                    #padres[1][1] = "South"
                    #padres[2][1] = "East"
                    #padres[2][0] = "South"
                    #padres[3][0] = "South"
                    #padres[4][0] = "West"
                    #padres[4][1] = "West"
                    #padres[4][2] = "West"
                    #padres[4][3] = "West"


                    while state != problem.getStartState():
                        for i in range(0, 5):
                            for j in range (0, 5):
                                if padres[i][j] == 0:
                                    padres[i][j] = "nope"
                        """
                        print padres[4][0] + " " + padres[4][1] + " " + padres[4][2] + " "+ padres[4][3] + " " + padres[4][4]
                        print padres[3][0] + " " + padres[3][1] + " " + padres[3][2] + " " + padres[3][3] + " " + \
                              padres[3][4]
                        print padres[2][0] + " " + padres[2][1] + " " + padres[2][2] + " " + padres[2][3] + " " + \
                              padres[2][4]
                        print padres[1][0] + " " + padres[1][1] + " " + padres[1][2] + " " + padres[1][3] + " " + \
                              padres[1][4]
                        print padres[0][0] + " " + padres[0][1] + " " + padres[0][2] + " " + padres[0][3] + " " + \
                              padres[0][4]
                        print " "
                        print "inical:"
                        print problem.getStartState()
                        """
                        state = x1, y1
                        """
                        print "state"
                        print state
                        print "situacion padres state"
                        print padres[x1 - 1][y1 - 1]
                        print "result"
                        print result
                        """
                        result.append(padres[x1-1][y1-1])
                        if padres[x1-1][y1-1] == "West":
                            y1 = y1 + 1
                        elif padres[x1-1][y1-1] == "East":
                            y1 = y1 - 1
                        elif padres[x1-1][y1-1] == "North":
                            x1 = x1 - 1
                        elif padres[x1-1][y1-1] == "South":
                            x1 = x1 + 1

                        state = x1, y1

                    print result
                    result.reverse()
                    print result
                    return result


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
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
