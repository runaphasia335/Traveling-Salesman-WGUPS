# Carlos Perez
# Student ID: 000819792
import sys

# Node class for each address. __cmp__ and __lt__ to help compare between each node
# 0(N)
class Node(object):

    def __init__(self, address):
        self.address = address
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority

# Graph to be used during shortest path algorithm. Adds node into the graph and creating adjacency_list for each node. Also
# created undirected edges. get_weight() used for later retrieval for edge weight.
# 0(N)

class Graph(object):
    def __init__(self):
        self.weight = {}
        self.reverse_weight = {}
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, start_node, target_node, weight):
        if weight != '':
            self.weight[start_node, target_node] = weight
            self.weight[(target_node, start_node)] = weight
            self.adjacency_list[start_node].append(target_node)


    def get_weight(self, start_node, target_node):
            if self.weight[start_node, target_node]:
                weight = self.weight[start_node, target_node]
                return weight
            elif self.weight[target_node, start_node]:
                weight = self.weight[target_node, start_node]
                return weight

