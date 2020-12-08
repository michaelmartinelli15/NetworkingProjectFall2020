import numpy as np
from random import choice
from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import layers
from layers.Layer import Layer
from layers.LayerManager import LayerManager
from Packet import Packet

class Node():
    def __init__(self, id):
        self.battery = 100
        self.energySpent = 0
        self.id = id
        self.connectedNodes = []
        self.layerManager = LayerManager(self.id)

    def __str__(self):
        return f'Node: {self.id}\n\tBattery: {self.battery}\n\tActive Connections: {len(self.connectedNodes)}'

    def getNextNode(self, parents, j):
        nextIndex = parents[j]
        if parents[nextIndex] == -1:
            for node in self.connectedNodes:
                if node.id == j:
                    return node

        return self.getNextNode(parents, nextIndex)

    def send(self, packet):
        nextNode = self.getNextNode(self.layerManager.routes, packet.destination)

        self.battery -= 1
        self.energySpent += 1

        print("Node ", self.id, ": Sending Packet")
        #print(self)

        self.layerManager.sendPacket(packet, nextNode)

    def forward(self, packet):
        nextNode = self.getNextNode(self.layerManager.routes, packet.destination)

        self.battery -= 1
        self.energySpent += 1

        print("Node ", self.id, ": Forwarding Packet")

        self.layerManager.forwardPacket(packet, nextNode)

    def receive(self, packet):
        print("Node ", self.id, ": Receiving Packet")
        #print(self)
        if packet.destination == self.id:
            print("Node ", self.id, ": Unpacking...")
            self.layerManager.receivePacket(packet)
        else:
            self.forward(packet)

class NodeController():
    def __init__(self, numNodes, maxConnections):
        self.numNodes = numNodes
        self.maxConnections = maxConnections
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

    def resetBattery(self):
        for node in self.nodes:
            node.battery = 100
            node.energySpent = 0

    def findMaxRemainingBattery(self, batteryMatrix, currentPath):
        minCost = 100000000

        for nodeIndex in range(self.numNodes):
            if batteryMatrix[nodeIndex] < minCost and currentPath[nodeIndex] == False:
                minCost = batteryMatrix[nodeIndex]
                minIndex = nodeIndex

        return minIndex

    def findShortestDistance(self, distanceMatrix, currentPath):
        minCost = 10000000

        for nodeIndex in range(self.numNodes):
            if distanceMatrix[nodeIndex] < minCost and currentPath[nodeIndex] == False:
                minCost = distanceMatrix[nodeIndex]
                minIndex = nodeIndex

        return minIndex

    def printPath(self, parents, j):
        if parents[j] == -1 :
            print(j)
            return
            self.printPath(parents , parents[j])
            print(j)

    def printSolution(self, dist, parents):
        src = 6
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
            self.printPath(parents,i)

    def dijsktra(self, node):
        costs = [1000000] * self.numNodes
        costs[node.id] = 0

        shortestPath = [False] * self.numNodes

        parents = [-1] * self.numNodes

        for iter in range(0, self.numNodes):
            nodeIndex = self.findShortestDistance(costs, shortestPath)

            shortestPath[nodeIndex] = True

            for neighbor in self.nodes[nodeIndex].connectedNodes:
                if shortestPath[neighbor.id] == False and costs[neighbor.id] > costs[nodeIndex] + 1:
                    # cost to the current node + 1 for the cost to the next node (all nodes are 1 away) + the amount of energySpent to avoid nodes with low battery
                    costs[neighbor.id] = costs[nodeIndex] + 1
                    parents[neighbor.id] = nodeIndex

        node.layerManager.routes = parents

    def dijsktraWithEnergySpent(self, node):
        costs = [1000000] * self.numNodes
        costs[node.id] = 0

        shortestPath = [False] * self.numNodes

        parents = [-1] * self.numNodes

        for iter in range(0, self.numNodes):
            nodeIndex = self.findMaxRemainingBattery(costs, shortestPath)

            shortestPath[nodeIndex] = True

            for neighbor in self.nodes[nodeIndex].connectedNodes:
                if shortestPath[neighbor.id] == False and costs[neighbor.id] > costs[nodeIndex] + 1 + neighbor.energySpent:
                    # cost to the current node + 1 for the cost to the next node (all nodes are 1 away) + the amount of energySpent to avoid nodes with low battery
                    costs[neighbor.id] = costs[nodeIndex] + 1 + neighbor.energySpent
                    parents[neighbor.id] = nodeIndex

        #self.printSolution(costs, parents)
        node.layerManager.routes = parents

    def updateLayerManagers(self):
        for node in self.nodes:
            self.dijsktra(node)

    def updateLayerManagersWithEnergySpent(self):
        for node in self.nodes:
            self.dijsktraWithEnergySpent(node)

    def printPaths(self):
        for node in self.nodes:
            node.layerManager.printSolution()

    def allNodesStillActive(self):
        for node in self.nodes:
            if node.battery == 0:
                return False

        return True

    def generateSourceAndDestination(self):
        source = randint(0,9)
        destination = randint(0,9)

        if source == destination:
            return self.generateSourceAndDestination()

        return source, destination

    def simulate(self):
        baselineCount = 0
        augmentedCount = 0

        while self.allNodesStillActive():
            source, destination = self.generateSourceAndDestination()

            self.updateLayerManagers()

            packet = Packet(source, destination)

            print("Preparing to sim with packet")
            print(packet)

            self.nodes[source].send(packet)
            baselineCount += 1

        self.resetBattery()

        while self.allNodesStillActive():
            source, destination = self.generateSourceAndDestination()

            self.updateLayerManagersWithEnergySpent()

            packet = Packet(source, destination)

            print("Preparing to sim with packet")
            print(packet)

            self.nodes[source].send(packet)
            augmentedCount += 1

        print("Simulation Complete")
        print("Packets sent using default Dijsktra: ", baselineCount)
        print("Packets sent using augmented Dijsktra focusing on energy conservation: ", augmentedCount)
