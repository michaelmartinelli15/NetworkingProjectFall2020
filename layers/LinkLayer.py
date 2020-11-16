from layers.Layer import Layer

class LinkLayer(Layer):
    """docstring for LinkLayer."""

    def __init__(self, arg):
        super(LinkLayer, self).__init__(arg)
        self.arg = arg

        self.name = "Link Layer"

        self.upperLayer = "Network"
