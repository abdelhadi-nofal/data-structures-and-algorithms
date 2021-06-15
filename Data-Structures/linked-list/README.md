# Singly Linked List

<!-- Short summary or background information -->

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Challenge

<!-- Description of the challenge -->

Within the LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called toString (or **str** in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

## Approach & Efficiency

What approach did you take? Why? What is the Big O space/time for this approach?

## API

## Linked_List

In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

## Code Challenge #5

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called toString (or **str** in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Code Challenge #6

Write the following methods for the Linked List class:

1. InsertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node.
2. InsertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node.

## Code Challenge #7

Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges. k-th value from the end of a linked list.

![](/linked-list/khf.jpg)
![image](https://user-images.githubusercontent.com/79086986/121959233-3046ae80-cd6d-11eb-82f3-015fbe19d148.png)

## Code Chaallenge # 8

# Challenge Summary

Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process ,Solution

<!-- Embedded whiteboard image -->

![image](https://user-images.githubusercontent.com/79086986/122129555-f5ad4680-ce3e-11eb-9b71-741fe02b84b4.png)


## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

big_O is a Python module to estimate the time complexity of Python code from its execution time. It can be used to analyze how functions scale with inputs of increasing size. big_O executes a Python function for input of increasing size N , and measures its execution time.
