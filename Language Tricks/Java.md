# Java Tricks for Interview
**Returning a New Array**
```java
return new int[] {x, y};
```
## Collections Time Complexity
List                 | Add  | Remove | Get  | Contains | Next | Data Structure
---------------------|------|--------|------|----------|------|---------------
ArrayList            | O(1) |  O(n)  | O(1) |   O(n)   | O(1) | Array
LinkedList           | O(1) |  O(1)  | O(n) |   O(n)   | O(1) | 


Queue                   |  Offer   | Peak |   Poll   | Remove | Size | Data Structure
------------------------|----------|------|----------|--------|------|---------------
PriorityQueue           | O(log n) | O(1) | O(log n) |  O(n)  | O(1) | Priority Heap
LinkedList              | O(1)     | O(1) | O(1)     |  O(1)  | O(1) | 
ArrayDequeue            | O(1)     | O(1) | O(1)     |  O(n)  | O(1) |


## Garbage Collection
Automatic garbage collection looks at heap memory, identifying which objects are in use and which are not, and deleting the unused objects
**Steps**
1. Marking: garbage collector identifies which pieces of memory are in use and which are not.
  * Time-consuming if all objects have to be scanned
2a. Deletion
