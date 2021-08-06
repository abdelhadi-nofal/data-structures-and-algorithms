class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight=0):
        self.vertix = vertix
        self.weight = weight

class Graph:
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v
    
    def add_edge(self, start_node, end_node, weight=0):
        # TODO: Check if both are in the graph
        if start_node not in self.adjacency_list or end_node not in self.adjacency_list:
            raise KeyError('Start or End Vertix not in the graph')
        
        
        edge = Edge(end_node, weight)
        adjacencies = self.adjacency_list[start_node]
        adjacencies.append(edge)
    
    def get_nodes(self):
        output = []
        
        for node in self.adjacency_list:
            output.append(node.value)

        return output
    
    def get_neighbors(self, node):
        output = []
        
        if node in self.adjacency_list:
            # print(self.adjacency_list[node][1].node.value)
            for neighbour in self.adjacency_list[node]:
                output.append([neighbour.node.value, neighbour.weight])
                
        return output
    
    def size(self):
        return len(self.adjacency_list)

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            # Concatenate the value of vertix
            output += vertix.value
            # Iterate over all edges of this vertix
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value 
            # Add a new line
            output += '\n'
        return output


visited = []

def depth_first_graph(visited, graph, Vertix):
    

    if Vertix not in visited:
        visited.append(Vertix)

        for neighbour in graph[Vertix]:
            depth_first_graph(visited, graph, neighbour)
    
    return visited