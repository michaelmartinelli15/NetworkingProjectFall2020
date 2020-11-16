from layers.Layer import Layer

class ApplicationLayer(Layer):
    """docstring for ApplicationLayer."""

    def __init__(self, arg):
        super(ApplicationLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Application Layer"

        self.lowerLayer = "Transport"
