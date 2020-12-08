from layers.Layer import Layer
from layers.NetworkLayer import NetworkLayer
from queue import Queue


class TransportLayer(Layer):
    """docstring for TransportLayer."""

    def __init__(self, arg):
        super(TransportLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Transport Layer"

        self.upperLayer = "Application"
        self.lowerLayer = "Network"

    def send(self, packet, nextNode):
        packet.payload = packet.header + ": " + packet.payload
        packet.header = "T"
        self.lower.send(packet, nextNode)

    def receive(self, packet):
        print("Transport Layer Header: ", packet.header)

        index = packet.payload.find(" ")

        packet.header = packet.payload[0]
        #packet.payload = packet.payload[index+1:]
        packet.payload = packet.payload[3:]

        self.upper.receive(packet)
