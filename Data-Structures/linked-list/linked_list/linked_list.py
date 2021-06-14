class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Draft:
ll: head - None
ll.append(4)
ll: head - Node(4) -> None
ll.append(-1)
ll: head - Node(4) -> Node(-1) -> None
ll.append('s')
ll: head - Node(4) -> Node(-1) -> Node('s') -> None
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.nodesList=[]

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        self.value=None
        node = Node(value)
        self.nodesList=[node.value]+self.nodesList
        if not self.head:
              self.head = node
        else:         
              current = self.head
              self.head= node
              self.head.next=current
        

    def append(self, added):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(added)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        """
        Add a new node with the given newValue immediately before the first value node
        """
        current = self.head

        if current.value is value:
            self.insert(newVal)
            return
            
        while current:
            if current.next.value is value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next
        raise Exception(f"Value {{ {value} }} not present in list")


    def insertAfter(self ,value, newVal) :

        """
        Add a new node with the given newValue immediately after the first value node

        """
        current = self.head

        while current:
            if current.value is value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next

        raise Exception(f"Value {{ {value} }} not present in list")




    def includes(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        x=False
        for value in self.nodesList:
              if value==value:
                  x=True
                  break
        return x
                  
    

    
    def __str__(self):
        """
        Loop over all nodes
        print all values in one line
        { a } -> { b } -> { c } -> NULL
        """
        current = self.head
        output = ''
        while current:
            output += f"{ {(current.value)} } ->"
            current = current.next
            
        return output

        
   

    
    

if __name__ == "__main__":
    ll = LinkedList()
    # Value of first node on head
    ll.append(4)
    # next of head (next of Node(4)) is Null
    ll.append(-1)
    ll.append('s')
    ll.insertBefore(4, 5)
    # ll.insertBefore(-1, 9)
    ll.insertBefore('s', 8)
    # I have ll: head - Node(4) -> Node(-1) -> Node('s') -> None
    print(ll.head.value)
    print(ll.head.next.value)
    print(ll.head.next.next.value)
    print(str(ll))
    
    
    