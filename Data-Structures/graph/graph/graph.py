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
            raise KeyError('Start or End Vertex not in the graph')
        
        
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


# add_node(n1,n2)

# n1 --->  n2


# A
# Edge(C, 0)
# A -> C

if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)

    # print(graph)
    # print(graph.adjacency_list)