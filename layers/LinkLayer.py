from layers.Layer import Layer
from queue import Queue

class LinkLayer(Layer):
    """docstring for LinkLayer."""

    def __init__(self, arg):
        super(LinkLayer, self).__init__(arg)
        self.arg = arg

        self.receiveBuffer = Queue()

        self.name = "Link Layer"

        self.upperLayer = "Network"
        self.lowerLayer = None

    def sendProcess(self, message):
        if self.lowerLayer is not None:
            print(message + " ")
            print("LL Message sent")
            #self.lower.receiveProcess(message)
        else:
            print(message + " ")
            print("No Lower Layer, Message Done")
            pass

    def receiveProcess(self, message):
        print(message + " ")
        print("LL process received")
        self.sendBuffer.put(message)
        self.sendProcess(message)
