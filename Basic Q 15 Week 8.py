# Week 8 Task 1
# #Implement Dijkstra's algorithm for a weighted graph data structure

from random import shuffle
import unittest

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
 
 
    def dijkstras(self, start, end, visited="", path=''):
        nodes = []
        visited += start.name
        for n, w in start.neighbours:
           nodes.append(n)
        if start.name == end.name:
            return end.name
        else:
            shuffle(nodes)  # give us some better chances are discovering other nodes on successive runs
            for i in nodes:
                if visited.count(i) <= len(nodes) and i not in path:
                    rt = self.dijkstras(self.nodes[i], end, visited, path)
                    path = start.name + rt
                    return path
            return ''
 

g = Graph()
edges = ['AB3', 'AE4', 'BF7', 'CG8', 'DE11', 'DH2', 'EH6', 'FG12', 'FI10', 'FJ5', 'GJ9', 'HI1']
#edges = ['AB2', 'AC4', 'CD3', 'BD7']
for j in edges:
  g.add_edge(j[:1], j[1:2], j[2:])
 
g.print_graph()
start = g.nodes['A']
end = g.nodes['D']
 
visited = []
while True:  # we can not get all the paths in one trip, so call it repeatedly hoping it will find new routes
    res = g.dijkstras(start, end, visited)
    if res.endswith(end.name):  # only paths found that end in the end name are successful, ignore others
        print(res)
    if not res:  # we haven’t found other paths before exhausting visited; so now we give up looking
        break
