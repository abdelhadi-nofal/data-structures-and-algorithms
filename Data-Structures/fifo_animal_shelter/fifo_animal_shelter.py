class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None 



    def enqueue(self, value):
        """
        Add to the front og the Queue
        """
        if value == 'cat' or value == 'dog':
            node = Node(value)
            if self.front:
                self.rear.next = node
                self.rear = node
            else:
                self.front = node
                self.rear = node
        else:
            raise ValueError('Can Not Input Other Animals' )




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

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("cat")
    # shelter.enqueue("bird")
    print(shelter.front.value)
    print(shelter.front.next.value)
    print(shelter.front.next.next.value)
    print(shelter.dequeue())
    print(shelter.dequeue())
    print(shelter.dequeue())
    print(shelter.front.value)

