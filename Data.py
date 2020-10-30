# Carlos Perez
# Student ID: 000819792

import csv
from Graph import *

class Data(object):
    def __init__(self):
        self._graph = Graph()

    # Gather all all rows from the CSV file
    # 0(N)
    def get_csv_data(self, file):
        csv_data = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # next(csv_reader, None)
            for row in csv_reader:
                csv_data.append(row)
        return csv_data

    # Uses to DistanceTable.csv file to add edges to edges list for easier retrieval when adding edge weights
    # 0(N^2)
    def get_graph(self, graph):
        edges = []
        global node
        global node2
        data = self.get_csv_data('DistanceTable.csv')
        for row in data:
            graph.add_node(Node(row[1]))
        for row in data:
            for i in range(3, len(row)):  # Starts at 3. Only need distances
                if row[i] != '':
                    edges.append((row[1], data[i - 3][1], float(row[i-1]))) # data[i-3][1] gets each connected street vertex
        # Without creating new Node objects, edges list was used to compare nodes from the adjacency list, add the compared
        # nodes to the add_edge() and add their appropriate weight.Returns graph for later use.
        for j in edges:
            for i in graph.adjacency_list:
                if i.address == j[0]:
                    node = i
                if i.address == j[1]:
                    node2 = i
            graph.add_edge(node, node2, j[2])
            graph.add_edge(node2, node, j[2])

        self._graph = graph
        return graph

    # Help finding a node that belong to the adjacency list as to avoid creating new Node objects.
    # 0(N)
    def find_node(self, address):
        for i in self._graph.adjacency_list:
            if i.address == address:
                return i

# creates object for later use
data = Data()






