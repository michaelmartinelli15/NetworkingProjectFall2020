from queue import Queue


class Layer():
    """Base Layer class inherited by other layers"""

    def __init__(self, arg):
        super(Layer, self).__init__()
        self.arg = arg

        self.name = None

        self.upperLayer = "None"
        self.lowerLayer = "None"

    def send(self):
        if not self.sendBuffer.empty():
            message = self.sendBuffer.get()
            self.sendProcess()

    def receive(self):
        if not self.receiveBuffer.empty():
            message = self.receiveBuffer.get()
            self.receiveProcess()

    def sendProcess(self):
        print("process sent")

    def receiveProcess(self):
        print("process received")
