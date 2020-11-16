from layers.Layer import Layer

class NetworkLayer(Layer):
    """docstring for NetworkLayer."""

    def __init__(self, arg):
        super(NetworkLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Network Layer"

        self.upperLayer = "Transport"
        self.lowerLayer = "Link"
