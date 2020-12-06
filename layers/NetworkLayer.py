from layers.Layer import Layer
from layers.LinkLayer import LinkLayer
from queue import Queue


class NetworkLayer(Layer):
    """docstring for NetworkLayer."""

    def __init__(self, arg):
        super(NetworkLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Network Layer"

        self.lower = LinkLayer(None)

        self.sendBuffer = Queue()
        self.receiveBuffer = Queue()

        self.upperLayer = "Transport"
        self.lowerLayer = "Link"

    def sendProcess(self, message):
        if self.lowerLayer is not None:
            print(message + " ")
            print("NL Message sent")
            self.lower.receiveProcess(message)
        else:
            pass

    def receiveProcess(self, message):
        print(message + " ")
        print("NL process received")
        self.sendBuffer.put(message)
        self.sendProcess(message)
