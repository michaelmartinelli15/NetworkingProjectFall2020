from layers.ApplicationLayer import ApplicationLayer
from layers.TransportLayer import TransportLayer
from layers.NetworkLayer import NetworkLayer
from layers.LinkLayer import LinkLayer

allLayers = []

allLayers.append(ApplicationLayer(None))
allLayers.append(TransportLayer(None))
allLayers.append(NetworkLayer(None))
allLayers.append(LinkLayer(None))

for l in allLayers:
    print(l.name)
    print("\t" + "Upper Layer: " + l.upperLayer)
    print("\t" + "Lower Layer: " + l.lowerLayer)
