from queue import Queue

class Layer():
    """Base Layer class inherited by other layers"""

    def __init__(self, arg):
        super(Layer, self).__init__()
        self.arg = arg

        self.name = None

        self.sendBuffer = Queue()
        self.receiveBuffer = Queue()

        self.upperLayer = "None"
        self.lowerLayer = "None"
