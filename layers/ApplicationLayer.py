from layers.Layer import Layer
from layers.TransportLayer import TransportLayer
from queue import Queue

class ApplicationLayer(Layer):
    """docstring for ApplicationLayer."""

    def __init__(self, arg):
        super(ApplicationLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Application Layer"

        self.sendBuffer = Queue()
        self.receiveBuffer = Queue()

        self.sendBuffer.put("BS")

        self.lowerLayer = "Transport"
        self.lower = TransportLayer(None)

    def send(self, sendNode, receiveNode):
        if not self.sendBuffer.empty():
            message = self.sendBuffer.get()
            self.sendProcess(message)

    def receive(self):
        if not self.receiveBuffer.empty():
            message = self.receiveBuffer.get()
            self.receiveProcess()

    def sendProcess(self, message):
        if self.lowerLayer is not None:
            print(message + " ")
            #print("AL Message sent")
            self.lower.receiveProcess(message)
        else:
            pass

    def receiveProcess(self):
        print("AL process received")
