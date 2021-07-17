## Hash Table
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

### Code Challenge #30
Implement a Hashtable with the following methods:

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: takes in the key and returns the value from the table.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
hash: takes in an arbitrary key and returns an index in the collection.


### Approach & Efficiency
The approach used is to convert the key of the input into index and put the key value object in the hashtable, that contains a linked list for the collisions.
Big O Notation
Time: O(1)
Space: O(N)
