# Week 8 Task 1
# #Implement Dijkstra's algorithm for a weighted graph data structure

from random import shuffle
#import unittest

class Node(object):
 
    def __str__(self):
        return self.name + ':' + str(self.neighbours)
 
#    def __repr__(self):
#      return self.name
 
    def __init__(self, name):
        self.name = name
        self.neighbours = list()
 
    def add_neighbour(self, neighbour, weight):
        self.neighbours.append((neighbour, weight))
        self.neighbours.sort()
 
class Graph(object):
    def __init__(self):
        self.nodes = {}  # Create dictionary
 
    def add_node(self, node):
        self.nodes[node.name] = node
 
    def add_edge(self, edge_left, edge_right, weight):
        if edge_left not in self.nodes:
          self.add_node(Node(edge_left))
        if edge_right not in self.nodes:
          self.add_node(Node(edge_right))
        self.nodes[edge_left].add_neighbour(edge_right, weight)
        self.nodes[edge_right].add_neighbour(edge_left, weight)
 
    def print_graph(self):
        for key in sorted(list(self.nodes.keys())):
          print("Node  " + key + "  " + str(self.nodes[key].neighbours))
          
    def dijkstra(self,start,end):
      
      visited = {}
      weights = {}
      queue = []
      start_weight = 1000
      for i in self.nodes: #For all nodes, set the initial weight to infinity
        weights[i] = start_weight
        visited[i] = None #And set the initial visited nodes or history to 0
      weights[start.name] = 0 #Start point is unique and has an initial weight of 0, it will always be 0
      queue.insert(0, start) #Insert starting point into queue
      while (len(queue) != 0): #While queue not empty
        current = queue.pop() #Current node is the back of the queue
        for j in current.neighbours: #For all neighbours of current node
          dist = weights[current.name] + int(j[1]) #Add distance from current node to each of its neighbours
          if dist < weights[j[0]]: #If this is less than starting weight (infinity) 
            weights[j[0]] = dist #Update to the new weight
            visited[j[0]] = current.name #Add these neighbours to visited
            queue.insert(0, self.nodes[j[0]]) #Insert object node back into queue
      route = [] #End route
      target = end.name #End node
      while target:
        route.append(target)
        target = visited[target]
      route.reverse() #Starting at the end therefore need to reverse the route
      return (route, weights[end.name]) #Send back the route and the distance

g = Graph()
edges = ['AB3', 'AE4', 'BF7', 'CG8', 'DE11', 'DH2', 'EH6', 'FG12', 'FI10', 'FJ5', 'GJ9', 'HI1']
#edges = ['AB2', 'AC4', 'CD3', 'BD7']
for j in edges:
  g.add_edge(j[:1], j[1:2], j[2:])
 
g.print_graph()
start = g.nodes['A']
end = g.nodes['D']
print("Start Node = " + start.name)
print("End Node = " + end.name)
route, distance = g.dijkstra(start, end)
print("Fastest Route = ", route, "Distance = ", distance)


#Attempt 1 - Not working 
 
#    def dijkstras(self, start, end, visited="", path=''):
#        nodes = []
#        visited += start.name
#        for n, w in start.neighbours:
#           nodes.append(n)
#        if start.name == end.name:
#            return end.name
#        else:
#            shuffle(nodes)  # give us some better chances are discovering other nodes on successive runs
#            for i in nodes:
#                if visited.count(i) <= len(nodes) and i not in path:
#                    rt = self.dijkstras(self.nodes[i], end, visited, path)
#                    path = start.name + rt
#                    return path
#            return ''
 
#    def find_distance(self, res):
#        for i in range(len(res)-1):
#            node = self.nodes[res[i]]
#            i = i + 1
#            print(node.neighbours)
#             
#        return(" Distance =")

#visited = []
#while True:  # we can not get all the paths in one trip, so call it repeatedly hoping it will find new routes
#    res = g.dijkstras(start, end, visited)
#    if res.endswith(end.name):# only paths found that end in the end name are successful, ignore others
#        distance = g.find_distance(res)
#        print(res, distance)
#    if not res:  # we haven’t found other paths before exhausting visited; so now we give up looking
#        break
