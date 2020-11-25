import numpy as np
from random import choice
import networkx as nx
import matplotlib.pyplot as plt

class Node():
    def __init__(self, id):
        self.battery = 100
        self.id = id
        self.connectedNodes = []

    def __str__(self):
        return f'Node: {self.id}\n\tBattery: {self.battery}\n\tActive Connections: {len(self.connectedNodes)}'

class NodeController():
    def __init__(self):
        self.numNodes = 10
        self.maxConnections = 3
        self.nodes = []
        self.resetNetwork()

    def visualize(self):
        print(np.matrix(self.adjacencyMatrix))

    def visualizeAsGraph(self):
        networkGraph = nx.from_numpy_matrix(np.array(self.adjacencyMatrix))
        nx.draw(networkGraph, with_labels=True)
        plt.show()

    def connectNodes(self, sourceNode, destNode):
        self.adjacencyMatrix[sourceNode.id][destNode.id] = 1
        self.adjacencyMatrix[destNode.id][sourceNode.id] = 1

        sourceNode.connectedNodes.append(destNode)
        destNode.connectedNodes.append(sourceNode)


    def establishConnection(self, sourceNode):
        try:
            if (len(sourceNode.connectedNodes) < self.maxConnections):
                destNode = choice([i for i in self.nodes if len(i.connectedNodes) < self.maxConnections and i not in sourceNode.connectedNodes and i != sourceNode])

                self.connectNodes(sourceNode, destNode)

                print("Connected: ", sourceNode, "and ", destNode)

                return True

        except IndexError as e:
            print("Node", sourceNode.id, ": ", e)
            return False

    def createNetwork(self):
        for i in range(self.numNodes):
            self.nodes.append(Node(i))

        for n in self.nodes:
            shouldContinue = True
            while (len(n.connectedNodes) < self.maxConnections and shouldContinue):
                shouldContinue = self.establishConnection(n)


    def resetNetwork(self):
        self.adjacencyMatrix = []
        row = []
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                row.append(0)
            self.adjacencyMatrix.append(row)
            row = []
