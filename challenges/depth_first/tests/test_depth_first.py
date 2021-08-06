from depth_first import __version__
from depth_first.depth_first import Edge, Graph, Vertix
from depth_first.depth_first import depth_first_graph


def test_version():
    assert __version__ == '0.1.0'





def test_graph_exist():
    assert Graph


def test_depth_first():
    assert depth_first_graph




def test_deph_first():
    graph = {
        'A' : ['B'],
        'B' : ['D', 'C', 'E'],
        'C' : [],
        'D' : ['A'],
        'E' : [],
        }
    visited = []
    assert depth_first_graph(visited, graph, 'A') == ['A','B','D','C','E']