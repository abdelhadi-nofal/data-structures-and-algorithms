from graph import __version__
from graph.graph import Edge,Graph,Vertix


def test_version():
    assert __version__ == '0.1.0'


def test_Graph_exits():
    assert Graph


def test_Vertex_exits():
    assert Vertix


def test_Edge_exits():
    assert Edge


def test_create_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('hadi')
    assert vertex.value == 'hadi'


def test_add_edge():
    graph = Graph()
    vertex1 = graph.add_vertex('ahmad')
    vertex2 = graph.add_vertex('moe')
    graph.add_edge(vertex1, vertex2, 11)
    assert graph.adjacency_list[vertex1][0].vertex == vertex2



def test_size():
    graph = Graph()
    vertex1 = graph.add_vertex('ahmad')
    vertex2 = graph.add_vertex('moe')
    graph.add_edge(vertex1, vertex2, 11)
    assert len(graph.adjacency_list) == 2 
    


def test_get_vertices():
    graph = Graph()
    vertex1 = graph.add_vertex('meat')
    vertex2 = graph.add_vertex('cheese')
    graph.add_edge(vertex1, vertex2, 11)
    output = graph.get_vertices()
    assert output == ['meat', 'cheese']


