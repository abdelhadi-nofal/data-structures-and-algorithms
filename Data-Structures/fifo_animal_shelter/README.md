# Challenge Summary

<!-- Description of the challenge -->

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process

<!-- Embedded whiteboard image -->

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

time O(1)
space O(1)

## Solution

<!-- Show how to run your code, and examples of it in action -->

```
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
```
