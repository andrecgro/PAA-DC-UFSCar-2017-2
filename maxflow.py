import networkx as nx

import random

from itertools import permutations


class MaxFlow():
    def __init__(self):
        self.graph = None
        self.pos = None
        self.paths = None
        self.disp_nodes = None
        self.next_node = None
        self.distance = float('inf')
        self.path = ()

    def createRandomGraph(self):
        # Creates a comple graph with 4 or 5 vertices
        self.graph = nx.complete_graph(random.randint(4, 5))
        self.pos = nx.spring_layout(self.graph)

        # Inicializa o atributo de cor das arestas para preto
        nx.set_edge_attributes(self.graph, 'black', 'color')

        # Gera os pesos das arestas aleatoriamente para valores entre 10 e 50
        for (u, v) in self.graph.edges():
            self.graph[u][v]['weight'] = random.randint(10, 50)

        # Gera os caminhos do grafo (combinações de todos os vértices)
        self.paths = list(permutations(self.graph.nodes()))

        # Gera a lista de nós do grafo e inicializa o nó inicial
        self.disp_nodes = list(self.graph.nodes())
        self.next_node = self.disp_nodes.pop()
    
    def ford_fulkerson(graph, source, sink, debug=None):
        flow, path = 0, True
        
        while path:
            # search for path with flow reserve
            path, reserve = MaxFlow.depth_first_search(graph, source, sink)
            flow += reserve
            # increase flow along the path
            for v, u in zip(path, path[1:]):
                if graph.has_edge(v, u):
                    graph[v][u]['flow'] += reserve
                else:
                    graph[u][v]['flow'] -= reserve
            
            # show intermediate results
            if callable(debug):
                debug(graph, path, reserve, flow)

    def depth_first_search(graph, source, sink):
        undirected = graph.to_undirected()
        explored = {source}
        stack = [(source, 0, undirected[source])]
        
        while stack:
            v, _, neighbours = stack[-1]
            if v == sink:
                break
            
            # search the next neighbour
            while neighbours:
                u, e = neighbours.popitem()
                if u not in explored:
                    break
            else:
                stack.pop()
                continue
            
            # current flow and capacity
            in_direction = graph.has_edge(v, u)
            capacity = e['capacity']
            flow = e['flow']
            # increase or redirect flow at the edge
            if in_direction and flow < capacity:
                stack.append((u, capacity - flow, undirected[u]))
                explored.add(u)
            elif not in_direction and flow:
                stack.append((u, flow, undirected[u]))
                explored.add(u)
        # (source, sink) path and its flow reserve
        reserve = min((f for _, f, _ in stack[1:]), default=0)
        path = [v for v, _, _ in stack]
        
        return path, reserve
