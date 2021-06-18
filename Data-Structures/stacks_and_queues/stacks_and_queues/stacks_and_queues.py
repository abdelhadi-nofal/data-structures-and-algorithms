class Node :
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack :
    
    def __init__(self):
        self.top =  None  

    def push(self,value):        
        """
        Adds to the top of the stack
        """
        node = Node(value)
        self.top = node
        self.top.next = None   

    def pop(self):
        """
        Removes the top node of the stack.
        Returns its value
        """       
        if self.top:
            new_top = self.top
            self.top = self.top.next
            new_top.next = None
            return new_top.value
        else:
            raise AttributeError('Stack is Empty')

    def peek(self):
        """
        Return the top node of the stack value.
        """
        if self.top:
            self.top.next = None
            return self.top.value
        else:
            raise AttributeError('Stack is Empty')    

    def isEmpty(self):
        """
        Check if the stack is empty
        """
        if self.top == None:
            return True
        else :
            return False    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Add to the front og the Queue
        """
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        """
        Remove the front node from the Queue
        Returns it`s value
        """
        if self.front == None:
            raise AttributeError('Queue is Empty')
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        """
        Return the front value of the Queue
        """
        if self.front == None:
            raise AttributeError('Queue is Empty')
        else :
            return self.front.value    


    def isEmpty(slef):
        if slef.front == None:
            return True
        else :
            return False   

    