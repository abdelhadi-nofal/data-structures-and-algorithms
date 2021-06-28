# Trees

<!-- Short summary or background information -->

## Common Terminology

> Node - A Tree node is a component which may contain it’s own values, and references to other nodes

    Root - The root is the node at the beginning of the tree
    K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.
    Left - A reference to one child node, in a binary tree
    Right - A reference to the other child node, in a binary tree
    Edge - The edge in a tree is the link between a parent and child node
    Leaf - A leaf is a node that does not have any children
    Height - The height of a tree is the number of edges from the root to the furthest leaf

### How to traverse "Trees"?

- > traversing a tree allows us to search for a node, print out the contents of a tree, and much more!
- Recursion is the most common way to traverse trees

## Challenge

<!-- Description of the challenge -->

Features

Node

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

time O(n) space O(n)

## API

<!-- Description of each method publicly available in each of your trees -->

Binary Tree:
pre_order returns an array of the values, ordered appropriately = root >> left >> right

post_order returns an array of the values, ordered appropriately = left >> right >> root

in_order returns an array of the values, ordered appropriately = left >> root >> right

Binary Search Tree:
add add a new node with that value in the correct location in the binary search tree.

contains Returns boolean indicating whether or not the value is in the tree at least once.

## White Board 17

![](/trees/tree.jpg)
![image](https://user-images.githubusercontent.com/79086986/123711934-f94abf80-d879-11eb-8e44-ea1072490579.png)

