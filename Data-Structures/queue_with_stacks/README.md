# Challenge Summary

<!-- Description of the challenge -->

Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Whiteboard Process

<!-- Embedded whiteboard image -->

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

time O(1)
space O(1)

## Solution

<!-- Show how to run your code, and examples of it in action -->

```
class PseudoQueue:
    """
    standard queue class
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()


    def enqueue(self, value):


        while self.stack2.top:
            self.stack1.push(self.stack2.pop())

        self.stack2.push(value)

        while self.stack1.top:
            self.stack2.push(self.stack1.pop())


    def dequeue(self):
        return self.stack2.pop()
```
