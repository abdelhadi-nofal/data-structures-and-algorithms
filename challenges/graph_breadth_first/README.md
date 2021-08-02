## Code Challenge #36

Implement a breadth-first traversal on a graph.

Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## White Board :

![image](https://user-images.githubusercontent.com/79086986/127907977-301c7ec9-dcb4-4ead-af75-91c9b5447eb0.png)


## Code :

```
    def breadth_first(self, vertex):
        nodes = []
        holder = set()
        breadth = Queue()
        holder.add(vertex.value)
        breadth.enqueue(vertex)
        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self._adjacency_list[front]:
                if child.vertex.value not in holder:
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes

```

## Complexity :

time : O(n)
space : O(1)
