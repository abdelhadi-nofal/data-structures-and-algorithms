# Stacks and Queues

<!-- Short summary or background information -->

What is a Stack
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Common terminology for a stack is

Push - Nodes or items that are put into the stack are pushed
Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
Top - This is the top of the stack.
Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
IsEmpty - returns true when stack is empty otherwise returns false.
Stacks follow these concepts:

FILO
First In Last Out

This means that the first item added in the stack will be the last item popped out of the stack.

LIFO
Last In First Out

This means that the last item added to the stack will be the first item popped out of the stack.

What is a Queue
Common terminology for a queue is

Enqueue - Nodes or items that are added to the queue.
Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
Front - This is the front/first Node of the queue.
Rear - This is the rear/last Node of the queue.
Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
IsEmpty - returns true when queue is empty otherwise returns false.
Queues follow these concepts:

FIFO
First In First Out

This means that the first item in the queue will be the first item out of the queue.

LILO
Last In Last Out

This means that the last item in the queue will be the last item out of the queue.

## Challenge

<!-- Description of the challenge -->

Create a Stack and Queue class with basic methods. Both classes should use a Node class with a next pointer for their implementations.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Using Node class for Both:

## Stack

Push O(1)
Pop O(1)
Peek O(1)
IsEmpty O(1)

## Queue

Enqueue O(1)
Dequeue O(1)
Peek O(1)
IsEmpty O(1)

## API

<!-- Description of each method publicly available to your Stack and Queue-->

### Stack

- `.push(value)` - Add a new value to the top of the stack
- `.pop()` - Removes the value on the top of the stack
- `.peek()` - Return the value at the top of the stack
- `.isEmpty()` - Returns True if the stack is empty, False otherwise

### Queue

- `.enqueue(value)` - Add a new value to the end of the queue
- `.dequeue()` - Removes value from the front of the queue
- `.peek()` - Return the value at the front of the queue
- `.isEmpty()` - Returns True if the queue is empty, False otherwise
