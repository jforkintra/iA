from filereader import File
from node import Node
from node import State
import queue
import itertools


def canConnect(plan, onOrbit, moduleIn):
    if onOrbit is None:
        return False
    else:
        for module in onOrbit:
            if moduleIn in plan[module]:
                return True
    return False



def getChildren(plan, node, file):
    state = node.state
    pathCost = node.pathCost
    launchNumber=node.launchNumber
    totalLaunches = node.totalLaunches
    launchesExecuted = node.launchesExecuted
    modulesOnLaunch = node.modulesOnLaunch

    children = []

    # MaxPayload of current Launch
    maxPayload=file.launchs[launchNumber][2]

    # number of modules in this launch
    for nModules in range(0, len(state.OnEarth)+1):
        # No modules are sent
        if nModules == 0:
            children.append(Node(state, pathCost, launchNumber + 1,totalLaunches,launchesExecuted, modulesOnLaunch ))
        elif nModules == 1 and state.OnOrbit == []:
            pass
        else:
            allCombinations = itertools.combinations(state.OnEarth, nModules)
            for combination in allCombinations:
                for module in combination:
                    pass




class Search:

    file = File
    stationPlan = file.vertices

    # Goal is none on earth and complete station on orbit
    goalState = State([], file.vertices_list)
    # Creates root node
    node = Node(State(file.vertices_list,[]),0,0,len(file.launchs),[],[])
    child = None

    allLaunches = file.launchs

    fringe = queue.PriorityQueue(0)
    fringe.put((node.pathCost, node))
    explored = []


    def __init__(self, fileIn):
        file = fileIn

    # Checks if current state is goal
    def isGoal(self, state):
        if self.goalState == state:
            return True
        else:
            return False

    # Returns the pathCost of a certain node
    def getPathCost(self, node):
        return node.pathCost

    def searchPath(self, method):
        if method == "-i":
            evalFcn = lambda node: getPathCost(node)

        while True:

            if self.fringe.empty():
                print("No solution was found")
                exit(-1)

            self.node = self.fringe.get()[0]

            if self.isGoal(self.node):
                print("Solution Was Found!! Continua código")
                exit(0)

            self.explored.append(self.node)

def connectsOnOrbit(plant, onOrbit):
    connection = []
    for module in onOrbit:
        for module1 in plant[module]:
            connection.append(modulel)
    return connection



if __name__ == '__main__':
    file = File("mir.txt")

    connectsOnOrbit(file.edges, ["VK1", "VCM"])

    print
