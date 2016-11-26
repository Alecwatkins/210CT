##Week 7 Task 1

## Write the pseudocode for an unweighted graph data structure. You either use an adjacency matrix or
## an adjacency list approach. Also, write a function to add a new node and a function to add an edge.
## Following that, implement the graph you have designed in the language of your choice. You may use
## your own linked list from previous labs, the STL LL, or use a simple fixed size array (10 elements
## would be fine)

##PSEUDOCODE

#Class Node:
# __init__:
#   name
#   neighbours

# FUNCTION add_neighbour:
#   append value to neighbours
#   sort neighbours

#Class Graph:
# __init__
#   create empty dictionary of nodes

# FUNCTION add_node:
#   append node to dictionary

# FUNCTION add_edge:
#   call add_neighbour for that node and the reverse
#   i.e. Add A to B and add B to A if edge = AB

# FUNCTION print_graph:
#   print dictionary in order
#   sort by key and print corresponding value

class Node(object):
  
  def __init__(self, name):
    self.name = name
    self.neighbours = list()

  def add_neighbour(self, neighbour):
      self.neighbours.append(neighbour)
      self.neighbours.sort()
      
class Graph(object):
  def __init__(self):
      self.nodes = {}  #Create dictionary
     
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

g = Graph()      
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for j in edges:
  g.add_edge(j[:1], j[1:])
  
g.print_graph()
