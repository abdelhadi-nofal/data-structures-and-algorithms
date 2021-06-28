from trees import __version__
from trees.trees import Node,Binary_Tree,Binary_Search_Tree
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_pre_order():
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected

def test_in_order():
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected

def test_post_order():
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected

def test_breadth_first():
    actual = tree.breadth_first()
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert actual == expected


def test_traverse_postorder_max_value():
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(8)
    bst.add(17)
    bst.add(23)
    bst.add(3)
    bst.add(-1)
    bst.add(50)
    bst.add(34)
    assert bst.contains(10) == True
    assert bst.post_order() == [-1, 3, 8, 34, 50, 23, 17, 10]
    assert bst.max_value() == 50



def test_contains():
    bin_tree = Binary_Search_Tree()
    bin_tree.add(10)
    assert bin_tree.contains(10) == True
    assert bin_tree.max_value() == 10


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

tree = Binary_Tree()
a.left = b 
a.right = c
tree.root = a 
b.left = d
b.right = e 
c.left = f 





