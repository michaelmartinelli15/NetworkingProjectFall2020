from layers.Layer import Layer
from layers.NetworkLayer import NetworkLayer
from queue import Queue


class TransportLayer(Layer):
    """docstring for TransportLayer."""

    def __init__(self, arg):
        super(TransportLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Transport Layer"

        self.lower = NetworkLayer(None)

        self.sendBuffer = Queue()
        self.receiveBuffer = Queue()

        self.upperLayer = "Application"
        self.lowerLayer = "Network"

    def send(self):
        if not self.sendBuffer.empty():
            message = self.sendBuffer.get()
            self.sendProcess()

    def receive(self):
        if not self.receiveBuffer.empty():
            message = self.receiveBuffer.get()
            self.receiveProcess()

    def sendProcess(self, message):
        if self.lowerLayer is not None:
            print(message + " ")
            print("TL Message sent")
            self.lower.receiveProcess(message)
        else:
            pass

    def receiveProcess(self, message):
        print(message + " ")
        print("TL process received")
        self.sendBuffer.put(message)
        self.sendProcess(message)