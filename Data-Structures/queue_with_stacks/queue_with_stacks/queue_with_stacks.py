class Node :
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack :
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('Stack is Empty')

    def peek(self):
        if self.top:
            self.top.next = None
            return self.top.value
        else:
            raise AttributeError('Stack is Empty')  


class PseudoQueue:
    """
    standard queue class
    """
    def __init__(self):
        self.stack2 = Stack()
        self.stack1 = Stack()
    
    
    def enqueue(self, value):

        while self.stack2.top:
            self.stack1.push(self.stack2.pop())
            
        self.stack2.push(value)

        while self.stack1.top:
            self.stack2.push(self.stack1.pop())
        

        

    def dequeue(self):
        return self.stack2.pop()

    


pseudo = PseudoQueue()
pseudo.enqueue(1)
pseudo.enqueue(2)
pseudo.enqueue(3)
pseudo.enqueue(4)
print(pseudo.stack2.peek())

pseudo = PseudoQueue()
pseudo.enqueue(1)
pseudo.enqueue(2)
pseudo.enqueue(3)
pseudo.enqueue(4)
pseudo.dequeue()
pseudo.dequeue()
pseudo.dequeue()
# pseudo.dequeue()

print(pseudo.stack2.peek())