##Week 7 Task 2

#Implement BFS and DFS traversals for the above graph. Save the nodes traversed in sequence to a text file

import copy

class Node(object):
  
  def __str__(self):
    return self.name + ':' + str(self.neighbours)
    
  def __repr__(self):
    return self.name
  
  def __init__(self, name):
    self.name = name
    self.neighbours = list()

  def add_neighbour(self, neighbour):
      self.neighbours.append(neighbour)
      self.neighbours.sort()
      
class Graph(object):
  
  def __init__(self): #Create Dictionary
    self.nodes = {}
  
  def add_node(self, node):
      self.nodes[node.name] = node
      
  def add_edge(self, edge_left, edge_right):
    if edge_left not in self.nodes:
      self.add_node(Node(edge_left))
    if edge_right not in self.nodes:
      self.add_node(Node(edge_right))
    self.nodes[edge_left].add_neighbour(edge_right)
    self.nodes[edge_right].add_neighbour(edge_left)

  def print_graph(self):
    for key in sorted(list(self.nodes.keys())):
      print(key + " " + str(self.nodes[key].neighbours))
    
  def bfs(self, node):
    Q = []
    visited = []
    Q.append(node)
    while len(Q):
      u = Q.pop(0)
      if u not in visited:
        visited.append(u)
        for e in u.neighbours:
          Q.append(self.nodes[e])
    print(visited)

  def dfs(self, node):
    visited = []
    stack = [node]
    while len(stack):
      u = stack.pop(0)
      temp = copy.copy(u.neighbours)
      temp.reverse()
      if u not in visited:
        visited.append(u)
        for e2 in temp:
          stack = [self.nodes[e2]] + stack
    print(visited)
 
g = Graph() 
  
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for j in edges:
  g.add_edge(j[:1], j[1:])

g.print_graph()
g.bfs(g.nodes['A'])
g.dfs(g.nodes['A'])



