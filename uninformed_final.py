from filereader import File
import random
from node import *

class UnInf:

    edgesSpace = []
    edgesEarth = {}
    edgesToSend = {}
    lauchesMade = []
    nodesFringe = []
    nodesExplored = []

    # iniciar root node
    node = Node(State(method.vertices_list, []), 0, 0, len(method.launchs), [], [])

    # Used for storing recursive search structure



    def __init__(self):
        pass

    def checkIfSpace(self, edgesToLaunch, edgesSpace, size):
        edgesSpaceConnections = []
        ##parte to coelho
        i = -1
        for edge in edgesToLaunch:
            i += 1
            if edge in edgesSpaceConnections:
                edgesToLaunch.pop(i)
                edgesSpace.append(edge)
        if len(edgesToLaunch) == size:
            return
        else:
            self.checkIfSpace(edgesToLaunch, edgesSpace, len(edgesToLaunch))

    def launch(self):

        combinations = []
        edgesToLaunchOri = edgesToLaunch = []
        edgesSpace = []
        for combination in combinations:
            self.checkIfSpace(edgesToLaunch, edgesSpace, len(edgesToLaunch))
            for edge in edgesToLaunchOri:
                if edge not in edgesToLaunch:
                    notPossible = 1
                    combinations.pop



if __name__ == '__main__':
    file = File("mir.txt")
    method= UnInf()
    method.edgesEarth = file.edges
    method.launchs= file.launchs
    method.vertices= file.vertices

    method.launch()
    print("ola")
    method.launch()