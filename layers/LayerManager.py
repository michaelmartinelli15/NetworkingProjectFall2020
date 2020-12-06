from layers.Layer import Layer
from layers.ApplicationLayer import ApplicationLayer
from layers.LinkLayer import LinkLayer
from layers.NetworkLayer import NetworkLayer
from layers.TransportLayer import TransportLayer
from Node import Node
from Node import NodeController

class LayerManager():
    def __init__(self, controller):
        self.description = "layerManager"
        self.application = ApplicationLayer(None)
        self.link = LinkLayer(None)
        self.network = NetworkLayer(None)
        self.transport = TransportLayer(None)
        self.controller = controller

    def sendPacket(self, packet):
        self.application.send(packet.source, packet.destination)
        #print(packet)
        #print(self.controller.nodes[packet.destination])