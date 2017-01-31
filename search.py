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
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):


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
    "Use The following to execute DFS"
    "python pacman.py -l tinyMaze -p SearchAgent"
    "python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs"

    stack = util.Stack()
    closed = []
    stack.push([(problem.getStartState(), "Start", 1)])

    while not stack.isEmpty():

        # In the top of the stack, we have stored the whole queue of nodes we have gone through.
        # There is nothing else in the stack.
        # In path, we find the whole way that we have gone through.
        path = stack.pop()
        print "Path Lenght: ", len(path)
        print "Path: ", path

        # In top_stack_node we store the last node stored in path
        top_stack_node = path[len(path) - 1]

        # In top_stack_state we store the state (x,y) of the last node stored in path
        top_stack_state = top_stack_node[0]
        print "top_stack_state: ", top_stack_state
        if problem.isGoalState(top_stack_state):

            return [x[1] for x in path][1:]

        if top_stack_state not in closed:
            closed.append(top_stack_state)
            print "Expanded: ", top_stack_state

            # Checks all of the successors and if they are not in the closed list, add them to the stack.
            # We are expanding the node.
            # In the Stack, we keep pushing the whole path to the solution.
            for successor in problem.getSuccessors(top_stack_state):
                print "SUCCESSOR FOUND: ", successor

                if successor[0] not in closed:

                    # It copies the content of path in successorPath, not a reference
                    successorPath = path[:]
                    print "SuccesorPath: ", successorPath
                    successorPath.append(successor)
                    print "SuccesorPAth after: ", successorPath
                    # print "successorPath: ", successorPath
                    stack.push(successorPath)
                else:
                    print successor[0], " IS ALREADY EXPLORED!!"

        test = stack.pop()
        print "Last Test", test
        test2 = stack.pop()
        print "Last Test", test2
        stack.push(test2)
        stack.push(test)

        print "***************************************"


    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "We can use basically the same alforithm because using a queue, the first node that we push is the first that will"
    "Be popped, unlike the stack, where the last pushed was the first popped. This way, we expand the nodes following "
    "the entry order. (First in first out)"

    "Note, because our code has been written generically, "
    "python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs"


    queue = util.Queue()
    closed = []
    queue.push([(problem.getStartState(), "Start", 1)])

    while not queue.isEmpty():

        # In the top of the stack, we have stored the whole queue of nodes we have gone through.
        # There is nothing else in the stack.
        # In path, we find the whole way that we have gone through.
        path = queue.pop()
        print "Path Lenght: ", len(path)
        print "Path: ", path

        # In top_stack_node we store the last node stored in path
        top_stack_node = path[len(path) - 1]

        # In top_stack_state we store the state (x,y) of the last node stored in path
        top_stack_state = top_stack_node[0]
        print "top_stack_state: ", top_stack_state
        if problem.isGoalState(top_stack_state):

            return [x[1] for x in path][1:]

        if top_stack_state not in closed:
            closed.append(top_stack_state)
            print "Expanded: ", top_stack_state

            # Checks all of the successors and if they are not in the closed list, add them to the stack.
            # We are expanding the node.
            # In the Stack, we keep pushing the whole path to the solution.
            for successor in problem.getSuccessors(top_stack_state):
                print "SUCCESSOR FOUND: ", successor

                if successor[0] not in closed:

                    # It copies the content of path in successorPath, not a reference
                    successorPath = path[:]
                    print "SuccesorPath: ", successorPath
                    successorPath.append(successor)
                    print "SuccesorPAth after: ", successorPath
                    # print "successorPath: ", successorPath
                    queue.push(successorPath)
                    # else:
                    # print successor[0], " IS ALREADY EXPLORED!!"

        print "***************************************"


    return []



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs"
    "python pacman.py -l mediumScaryMaze -p StayWestSearchAgent"

    # Cost in this case is a function
    cost = lambda aPath: problem.getCostOfActions([x[1] for x in aPath])

    priority_queue = util.PriorityQueueWithFunction(cost)
    closed = []
    priority_queue.push([(problem.getStartState(), "Stop", 1)])

    while not priority_queue.isEmpty():

        # In the top of the stack, we have stored the whole queue of nodes we have gone through.
        # There is nothing else in the stack.
        # In path, we find the whole way that we have gone through.
        path = priority_queue.pop()
        print "Path Lenght: ", len(path)
        print "Path: ", path

        # In top_stack_node we store the last node stored in path
        top_stack_node = path[len(path) - 1]

        # In top_stack_state we store the state (x,y) of the last node stored in path
        top_stack_state = top_stack_node[0]
        print "top_stack_state: ", top_stack_state
        if problem.isGoalState(top_stack_state):

            return [x[1] for x in path][1:]

        if top_stack_state not in closed:
            closed.append(top_stack_state)
            print "Expanded: ", top_stack_state

            # Checks all of the successors and if they are not in the closed list, add them to the stack.
            # We are expanding the node.
            # In the Stack, we keep pushing the whole path to the solution.
            for successor in problem.getSuccessors(top_stack_state):
                print "SUCCESSOR FOUND: ", successor

                if successor[0] not in closed:

                    # It copies the content of path in successorPath, not a reference
                    successorPath = path[:]
                    print "SuccesorPath: ", successorPath
                    successorPath.append(successor)
                    print "SuccesorPAth after: ", successorPath
                    # print "successorPath: ", successorPath
                    priority_queue.push(successorPath)
                    # else:
                    # print successor[0], " IS ALREADY EXPLORED!!"

        print "***************************************"


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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
