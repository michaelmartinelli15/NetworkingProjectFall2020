from layers.LayerManager import LayerManager
from Node import NodeController, Node
from Packet import Packet

allLayers = []

for l in allLayers:
    print(l.name)
    print("\t" + "Upper Layer: " + l.upperLayer)
    print("\t" + "Lower Layer: " + l.lowerLayer)

# takes numNodes, maxConnections
controller = NodeController(10, 3)
layerManager = LayerManager(controller)
controller.visualize()
controller.createNetwork()
controller.visualize()
controller.visualizeAsGraph()

randPacket = Packet()
layerManager.sendPacket(randPacket)


#print(layerManager.application.name)