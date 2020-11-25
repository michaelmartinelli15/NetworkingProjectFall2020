from layers.ApplicationLayer import ApplicationLayer
from layers.TransportLayer import TransportLayer
from layers.NetworkLayer import NetworkLayer
from layers.LinkLayer import LinkLayer
from Node import NodeController, Node

allLayers = []

allLayers.append(ApplicationLayer(None))
allLayers.append(TransportLayer(None))
allLayers.append(NetworkLayer(None))
allLayers.append(LinkLayer(None))

for l in allLayers:
    print(l.name)
    print("\t" + "Upper Layer: " + l.upperLayer)
    print("\t" + "Lower Layer: " + l.lowerLayer)

controller = NodeController()
controller.visualize()
controller.createNetwork()
controller.visualize()
controller.visualizeAsGraph()
#controller.test()
