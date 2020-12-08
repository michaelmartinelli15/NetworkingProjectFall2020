#from layers.LayerManager import LayerManager
from Node import NodeController, Node
from Packet import Packet
import sys

allLayers = []

for l in allLayers:
    print(l.name)
    print("\t" + "Upper Layer: " + l.upperLayer)
    print("\t" + "Lower Layer: " + l.lowerLayer)

if len(sys.argv) == 3:
    numNodes = int(sys.argv[1])
    maxConnections = int(sys.argv[2])
    
else:
    numNodes = 10
    maxConnections = 3


# takes numNodes, maxConnections
controller = NodeController(numNodes, maxConnections)

# creates nodes and connects them up to maxConnections time
controller.createNetwork()

# conduct simulation - runs two times - once with default shortest path Dijsktra and once with the augmented Energy Conserving Dijsktra
controller.simulate()

# show graph that was used in the sim
controller.visualizeAsGraph()
