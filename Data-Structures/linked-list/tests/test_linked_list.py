from linked_list import __version__
from linked_list.linked_list import (
    Node,
    LinkedList,   
)


def test_version():
    assert __version__ == '0.1.0'


def test_insert_4():
    ll = LinkedList()
    ll.insert(4)
    ll.append(-1)
    assert ll.head.value == 4
    assert ll.head.next.value == -1


def test_append_1_s():
    ll = LinkedList()
    ll.insert(4)
    ll.append(-1)
    ll.append('s')
    assert ll.head.value == 4
    assert ll.head.next.value == -1
    assert ll.head.next.next.value == 's'


def test_includes():
    ll = LinkedList()
    ll.insert(4)
    ll.append(-1)
    assert ll.includes(4) == True
    assert ll.includes(-1) == True
    # assert ll.includes(5) == False


def test_print():
    ll = LinkedList()
    ll.insert(4)
    ll.append(-1)
    ll.append(3)
    
    assert str(ll) == '{4} ->{-1} ->{3} ->'

def test_linked_list_insert_before():
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.insertBefore(4, 2)
    actual = str(ll)
    expected = "{2} ->{4} ->{3} ->"
    assert actual == expected

def test_linked_list_insert_after():
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.insertAfter(3, 7)
    actual = str(ll)
    expected = "{4} -> {3} ->{7} ->"
    assert actual == expected    
    


    

