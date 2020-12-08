from layers.Layer import Layer
from queue import Queue

class LinkLayer(Layer):
    """docstring for LinkLayer."""

    def __init__(self, arg):
        super(LinkLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Link Layer"

        self.upperLayer = "Network"
        self.lowerLayer = None

    def send(self, packet, nextNode):
        # if the packet has a link layer header, it must need to be forwarded
        if packet.header == "L":
            nextNode.receive(packet)
        # otherwise add the link layer header 
        else:
            packet.payload = packet.header + ": " + packet.payload
            packet.header = "L"

            nextNode.receive(packet)

    def receive(self, packet):
        print("Link Layer Header: ", packet.header)

        index = packet.payload.find(" ")

        packet.header = packet.payload[0]
        #packet.payload = packet.payload[index+1:]
        packet.payload = packet.payload[3:]

        self.upper.receive(packet)
