from linked_list import __version__
from linked_list.linked_list import (
    Node,
    LinkedList,zipLists
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
    assert ll.includes(5) == False


def test_print():
    ll = LinkedList()
    ll.insert(4)
    ll.append(-1)
    ll.append(3)
    
    assert str(ll) == '{4} ->{-1} ->{3} ->NULL'

def test_linked_list_insert_before():
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.insertBefore(4, 2)
    actual = str(ll)
    expected = "{2} ->{4} ->{3} ->NULL"
    assert actual == expected

def test_linked_list_insert_after():
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.insertAfter(3, 7)
    actual = str(ll)
    expected = "{4} ->{3} ->{7} ->NULL"
    assert actual == expected  


def test_linked_list_kthFromEnd():
    ll = LinkedList()
    ll.append(4)
    ll.append(-1)
    ll.append('s')
    ll.insertBefore(4, 5)
    ll.insertBefore(-1, 9)
    ll.insertAfter(4, 8)
    ll.insertAfter(-1, 98) 
    actual = (ll.kthFromEnd(0))  
    expected= "s"
    assert actual == expected
    

def test_linked_list_kthFromEnd():
    ll = LinkedList()
    ll.append(4)
    ll.append(-1)
    ll.append('s')
    ll.insertBefore(4, 5)
    ll.insertBefore(-1, 9)
    ll.insertAfter(4, 8)
    ll.insertAfter(-1, 98)  
    actual = (ll.kthFromEnd(1))
    expected= 98
    assert actual == expected
    

def test_linked_list_zipped_list():
    ll1= LinkedList()
    ll1.append(4)
    ll1.append(-1)
    ll1.append('s')
    ll1.insertBefore(4, 5)
    ll1.insertAfter(-1, 98)
    ll2= LinkedList()
    ll2.append(7)
    ll2.append(-8)
    ll2.insertAfter(7, 8)
    actual = str(zipLists(ll1,ll2))
    expected = "{5} ->{7} ->{4} ->{8} ->{-1} ->{-8} ->{98} ->{'s'} ->NULL"
    assert actual == expected  

    

