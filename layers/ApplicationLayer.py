from layers.Layer import Layer
from layers.TransportLayer import TransportLayer
from queue import Queue

class ApplicationLayer(Layer):
    """docstring for ApplicationLayer."""

    def __init__(self, arg):
        super(ApplicationLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Application Layer"

        self.upperLayer = None
        self.lowerLayer = "Transport"

    def send(self, packet, nextNode):
        packet.header = "A"
        self.lower.send(packet, nextNode)

    def receive(self, packet):        
        print("Application Layer Header: ", packet.header)

        print("Packet received with payload: ", packet.payload)
