from layers.Layer import Layer
from layers.ApplicationLayer import ApplicationLayer
from layers.LinkLayer import LinkLayer
from layers.NetworkLayer import NetworkLayer
from layers.TransportLayer import TransportLayer
import sys

class LayerManager():
    def __init__(self, id):
        self.description = "layerManager"
        self.application = ApplicationLayer(None)
        self.link = LinkLayer(None)
        self.network = NetworkLayer(None)
        self.transport = TransportLayer(None)
        self.id = id
        self.routes = []

        self.application.id = self.id
        self.transport.id = self.id
        self.network.id = self.id
        self.link.id = self.id

        self.application.lower = self.transport

        self.transport.upper = self.application
        self.transport.lower = self.network

        self.network.upper = self.transport
        self.network.lower = self.link

        self.link.upper = self.network

    def sendPacket(self, packet, nextNode):
        self.application.send(packet, nextNode)

    def forwardPacket(self, packet, nextNode):
        self.link.send(packet, nextNode)

    def receivePacket(self, packet):
        self.link.receive(packet)

    def printPath(self, parents, j):
        if parents[j] == -1 :
            print(j)
            return
            self.printPath(parents , parents[j])
            print(j)

    def printSolution(self):
        src = self.id
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(0, 10):
            print(src, " --> ", i)
            self.printPath(self.routes, i)
