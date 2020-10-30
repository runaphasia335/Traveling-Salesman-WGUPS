# Carlos Perez
# Student ID: 000819792

import heapq

# Algorithm to determine the shortest path.

# function takes the graph and the starting node. Sets the starting node to 0 distance, and predecessor to none. Since each node
# has a minimum distance of MAX. 0 distance for the starting will determine each edge weight to its adjacent nodes.

# 0(N^2)
class Algorithm(object):

    def __init__(self,graph, start_node):

        start_node.min_distance = 0
        start_node.predecessor = None
        unvisited = [i for i in graph.adjacency_list]
        # uses heapify to set the lowest as priority
        heapq.heapify(unvisited)
        # Function will continue to run until empty
        while len(unvisited):

            # Pops the smallest node and makes it the current node
            current = heapq.heappop(unvisited)
            current.visited = True

            # Searches through the current nodes adjacency list, making 'target' the adjacent node
            for target in graph.adjacency_list[current]:
                # while the adjacent node is has not been visited
                if target.visited == True:
                    continue
                weight = graph.get_weight(current, target)
                # create edge weight with an adjacent node
                new_distance = current.min_distance + float(weight)

                # if new_distance is less than the adjacent node minimum distance, it assigns new_distance weight
                # to the adjance node's minimum_distance. Then sets the current node as predecessor.
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = current

            # Pops each node fro, unvisited_list
            while len(unvisited):
                heapq.heappop(unvisited)
            # recreates unvisited_list while leaving out nodes marked as visited.
            unvisited = [i for i in graph.adjacency_list if i.visited == False]
            heapq.heapify(unvisited)




    # function to find the shortest path to a node. Returns the target node with an assigned distance.

    def shortest_path(self, target_node):
        node = target_node
        while node is not None:
            node = node.predecessor
        return target_node





