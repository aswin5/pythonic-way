import random
class vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, distance = 0):
        self.connectedTo[nbr] = distance
    def getConnections(self):
        return self.connectedTo.keys()
    def getKey(self):
        return self.key
    def getDistance(self,nbr):  
        return self.connecteo[nbr]

class graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex=vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertix(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertList[item]
    def addEdge(self,f,t,distance=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], distance)
    def getVertices(self):
        self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items ==[]
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self, item):
        return self.items.pop()
    def size(self):
        return len(self.items)

def throwDice(self):
    return random.randint(1,6)

def bfs(g,start):
    start.setDistance

testCases = int(raw_input())
answer = []
for x in xrange(testCases):
    g = graph()
    initialPosition = 1
    numberOfSnakes = int(raw_input())
    snakes = {}
    # snakes = [[] for x in xrange(numberOfSnakes)]
    for i in xrange(numberOfSnakes):
        tmpSnake = []
        tmpSnake=raw_input().split(" ")
        snakes[tmpSnake[0]]=tmpSnake[1]
    numberOfLadders = int(raw_input())
    ladders = {}
    for i in xrange(numberOfLadders):
        tmpLadder  = []
        tmpLadder = raw_input().split(" ")
        ladders[tmpLadder[0]]=tmpLadder[1]
    


# __author__ = 'ashwin'
#
# class vertex:
#     def __init__(self, key):
#         self.id = key
#         self.connectedTo = {}
#
#     def addNeighbor(self,nbr,weight=0):
#         self.connectedTo[nbr] = weight
#
#     def __str__(self):
#         return str(self.id) + 'ConnectedTo: ' + str([x.id for x in self.connectedTo])
#
#     def getConnections(self):
#         return self.connectedTo.keys()
#     def getId(self):
#         return self.id
#     def getWeight(self,nbr):
#         return self.connectedTo[nbr]
#
# class graph:
#     def __init__(self):
#         self.vertList={}
#         self.numVertices=0
#     def addVertex(self,key):
#         self.numVertices = self.numVertices + 1
#         newVertex = vertex(key)
#         self.vertList[key] = newVertex
#         return newVertex
#     def getVertix(self,n):
#         if n in self.vertList:
#             return self.vertList[n]
#         else:
#             return None
#     def __contains__(self, n):
#         return n in self.vertList
#     def addEdge(self, f, t, cost= 0):
#         if f not in self.vertList:
#             nv = self.addVertex(f)
#         if t not in self.vertList:
#             nv = self.addVertex(t)
#         self.vertList[f].addNeighbor(self.vertList[t], cost)
#     def getVertices(self):
#         return self.vertList.keys()
#     def __iter__(self):
#         return iter(self.vertList.values())
#
#
# g = graph()
# for i in xrange(6):
#     g.addVertex(i)
# print g.vertList
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))
