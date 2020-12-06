#from layers.LayerManager import LayerManager
from Node import NodeController, Node
from Packet import Packet
import sys

allLayers = []

for l in allLayers:
    print(l.name)
    print("\t" + "Upper Layer: " + l.upperLayer)
    print("\t" + "Lower Layer: " + l.lowerLayer)

# takes numNodes, maxConnections
controller = NodeController(10, 3)
#layerManager = LayerManager(controller)
#controller.visualize()
controller.createNetwork()
#controller.visualize()

#layerManager.sendPacket(randPacket)
#controller.dijsktra(randPacket)

controller.simulate()

controller.visualizeAsGraph()

#print(layerManager.application.name)