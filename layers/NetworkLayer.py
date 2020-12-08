from layers.Layer import Layer
from layers.LinkLayer import LinkLayer
from queue import Queue


class NetworkLayer(Layer):
    """docstring for NetworkLayer."""

    def __init__(self, arg):
        super(NetworkLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Network Layer"

        self.upperLayer = "Transport"
        self.lowerLayer = "Link"

    def send(self, packet, nextNode):
        packet.payload = packet.header + ": " + packet.payload
        packet.header = "N"
        self.lower.send(packet, nextNode)

    def receive(self, packet):
        print("Network Layer Header: ", packet.header)

        index = packet.payload.find(" ")

        packet.header = packet.payload[0]
        #packet.payload = packet.payload[index+1:]
        packet.payload = packet.payload[3:]

        self.upper.receive(packet)
