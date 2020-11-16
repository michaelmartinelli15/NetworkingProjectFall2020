from layers.Layer import Layer

class TransportLayer(Layer):
    """docstring for TransportLayer."""

    def __init__(self, arg):
        super(TransportLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Transport Layer"

        self.upperLayer = "Application"
        self.lowerLayer = "Network"
