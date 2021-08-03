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
    
    
    def get_neighbors(self, node):
        output = []
        
        if node in self.adjacency_list:
            # print(self.adjacency_list[node][1].node.value)
            for neighbour in self.adjacency_list[node]:
                output.append([neighbour.node.value, neighbour.weight])
                
        return output
    



def business_trip(gragh, cities):
    cost = 0
    flag = True

    for i in range(len(cities)-1):
        if not flag:
            return False, '$0'
        neighbors = gragh.get_neighbors(cities[i])
        for neighbor in neighbors:
            if cities[i+1] == neighbor[0]:
                cost += neighbor[1]
                flag = True
                break
            else:
                flag = False
    if not flag :
        cost = 0
    return flag, '$'+str(cost)


if __name__ == "__main__":
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstropolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2, 150)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node3, 99)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    print(business_trip(g,['Metroville','Pandora']))
    print(business_trip(g,['Narnia','Arendelle','Naboo']))