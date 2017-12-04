'''
import networkx as nx

import random

from itertools import permutations

class MaxFlow():
    def __init__(self):
        self.resGraph = None

    def BFS(self,graph, source, goal):
        nodes = graph.nodes(data=True)
        queue = []
        
        queue.append(source)
        capacity = nx.get_edge_attributes(graph,'capacity')

        while not queue.empty():
            neighbors = currentNode.neighbors()
            for neighbor in neighbors:
                if capacity[graph.predecessors(neighbor),neighbor] != 0 and neighbor not in queue:
                    queue.append(neighbor)
            queue.remove(currentNode)
            currentNode = queue.pop([0])



    def fordFulkerson(self, graph, source, goal):
        max_flow = 0
        while self.path = nx.bfs_tree(graph,source):
            min_capacity = float('-inf')
            pathNodes = self.path.nodes(data=True)
            graphNodes = graph.nodes(data=True)
            
            # Get min capacity in current path
            for node in pathNodes:
                if  node[1]['capacity'] < min_capacity:
                    min_capacity = node[1]['capacity']
                    
            max_flow += min_capacity

            for node in graphNodes:
                if node in pathNodes
                    nx.set_node_attributes(graph, {node: node[1]['capacity'] - min_capacity},'capacity')
        return max_flow
'''