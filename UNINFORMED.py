from filereader import File
import random
from node import *

class UnInf:
    edgesSpace = []
    edgesEarth = {}
    edgesToSend = {}
    lauchesMade =[]
    nodesFringe = []
    nodesExplored = []

    #iniciar root node
    node = Node(State(method.vertices_list,[]),0, 0, len(method.launchs),[],[])

    # Used for storing recursive search structure
    temp_edges = None


    def __init__(self):
        pass

    def sendToSpace(self, edge):
        self.edgesSpace.append(edge)

    def selectLaunch(self):
        pass


    def calculateCost(self, launch):
        return launch["data"]["fix_cost"]+launch["data"]["var_cost"]*(launch["edges"][0]["weight"]+launch["edges"][1]["weight"])

    def launchData(self):
        temp_data = method.launchs.pop()
        launch_data={}
        launch_data["date"]= temp_data[0]
        launch_data["max_payload"]= temp_data[2]
        launch_data["fix_cost"] = temp_data[3]
        launch_data["var_cost"] = temp_data[4]
        return launch_data

    def chooseFirstEdges(self):
        """Not used anymore"""
        # escolhe um edge
        temp1 = {}
        temp1["id"] = random.choice(list(self.edgesEarth.keys()))
        temp1["weight"] = self.vertices[temp1["id"]]
        self.sendToSpace(temp1)  # insere nos edges do espaco
        # escolhe o seguinte edge que esteja ligado a este
        temp2 = {}
        temp2["id"] = random.choice(self.edgesEarth[temp1["id"]])
        temp2["weight"] = self.vertices[temp2["id"]]
        self.sendToSpace(temp2)
        # insere no primeiro lancamento os dois edges
        # edges.append([temp1, temp2])
        # limpar edges dos que estao disponiveis na terra
        del self.edgesEarth[temp1["id"]]
        del self.edgesEarth[temp2["id"]]
        templaunch = {}
        templaunch["edges"] = [temp1, temp2]
        templaunch["data"] = self.launchData()
        templaunch["cost"] = self.calculateCost(templaunch)

    def deleteConnection(self, edges, edge_to_delete):

        for edge in edges:
            if edge_to_delete in edges[edge]:
                edges[edge].remove(edge_to_delete)


    def chooseFirstEdge(self, max_payload):
        possibleEdges={}
        for edge in self.edgesEarth.keys():
            if self.vertices[edge] < max_payload:
                possibleEdges[edge] = {}
        return possibleEdges

    def chooseSecondEdge(self, firstEdges, max_payload, temp_earth):
        for edge in firstEdges:
            #self.temp_edges[edge] = None
            temps = temp_earth[edge]
            if len(temps) == 0:
                return
            for temp in temps:
                if temp is None:
                    pass
                else:
                    weight = self.vertices[temp] + self.vertices[edge]
                    if weight <= max_payload: #checks if w1+w2< max_payload
                        #if firstEdges[edge] is None:
                        #    pass
                        #else:
                        firstEdges[edge][temp]={}
                        del temp_earth[edge]
                        self.deleteConnection(temp_earth, edge)

                        #self.chooseSecondEdge(firstEdges[edge], max_payload-weight, temp_earth)


    def action(self):
        #if self.temp_edges is not None:
        #    del self.temp_edges

        templaunch = {}
        templaunch["data"] = self.launchData()
        self.temp_edges = self.chooseFirstEdge(templaunch["data"]["max_payload"])
        self.tempEarth = self.edgesEarth
        self.chooseSecondEdge(self.temp_edges, templaunch["data"]["max_payload"], self.tempEarth)
        print



    def connectedEdges(self, edges):
        pass
        #Coelho

    #recebe array de edges
    #assume que os edges no espaço
    def checkIfSpace(self, edgesToLaunch, edgesSpace, size):
        edgesSpaceConnections = []
        ##parte to coelho
        i=-1
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
        edgesToLaunchOri= edgesToLaunch=[]
        edgesSpace = []
        i=0
        for combination in combinations:
            i=+1
            self.checkIfSpace(edgesToLaunch, edgesSpace, len(edgesToLaunch))
            for edge in edgesToLaunchOri:
                if edge not in edgesToLaunch:
                    notPossible=1
                    combinations.pop(i)


if __name__ == '__main__':
    file = File("mir.txt")
    method= UnInf()
    method.edgesEarth = file.edges
    method.launchs= file.launchs
    method.vertices= file.vertices

    method.launch()
    print("ola")
    method.launch()
    method.launch()
    print

    #decide-se modulos seguintes


    print
