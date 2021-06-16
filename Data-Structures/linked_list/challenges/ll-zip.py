# from linked_list.linked_list import LinkedList,Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.nodesList=[]

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        
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
        Inserts a new node before a given node value
        """

        current = self.head
        node = Node(newVal)

        if current.value == value:
            node.next = current
            self.head = node
            return node

        while current.next:
            if current.next.value == value:
                node.next = current.next
                current.next = node
                return node
            else:
                return ('Node not exist')
        current = current.next
        


    def insertAfter(self ,value, newVal) :

        """
        Add a new node with the given newValue immediately after the first value node
        """
        current = self.head
        node = Node(newVal)
                
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                return node
            if current.next == None:
                return ('Node not exist')
            current = current.next





    def includes(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        x=False
        if value in self.nodesList:
            x=True
            return x
        else:
            x = False
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
        output+='NULL'
            
        return output


    def kthFromEnd(self, k):
        """
        Returns the nth value of the Linkedlist starting from the end
        """
        current = self.head
        cnt = 0
        while current:
            cnt += 1
            current = current.next
        
        reverse_idx = cnt - k -1
        
        cnt = 0
        current = self.head
        if reverse_idx < 0:
            return 'Exception'
        else:
            while current:
                if cnt == reverse_idx:
                    return current.value
                cnt += 1
                current = current.next

def zipLists(ll1, ll2):

        current1 = ll1.head
        current2 = ll2.head
        while current1:
            if current2:
                save1 = current1.next
                current1.next = current2
                
                if save1:
                    save2 = current2.next
                    current2.next = save1
                     
                if not save2:
                    break
                
                current1 = save1
                current2 = save2
        return ll1


if __name__=="__main__":
    ll1= LinkedList()
    ll1.append('T')
    ll1.append('A')
    ll1.append('0')
    ll1.append('A')
    ll1.append('T')
    
    print(ll1)
    
    ll2= LinkedList()
    ll2.append(7)
    ll2.append(-8)

    ll2.insertAfter(7, 8)
    print(ll2)

    zip_ll = zipLists(ll2,ll1)
    print(zip_ll)    

