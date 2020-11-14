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
2. Deletion
    * Normal Deletion
        * Removes unreferenced objects leaving referenced objects and pointers to free space.
        * Memory allocator holds a list of references to free spaces and searches for free space whenever an allocation is required.
    * Deletion with Compacting
        * In addition to deleting unreferenced objects, move referenced object together, making new memory allocation faster.
        
**Generational GC**
1. The heap parts are: Young Generation, Old or Tenured Generation, and Permanent Generation
   * Young Generation: where all new objects are allocated and aged. When the young generation fills up, this causes a **minor garbage collection**. Minor collections can be optimized assuming a high object mortality rate. A young generation full of dead objects is collected very quickly. Some surviving objects are aged and eventually move to the old generation.
   * Old Generation: used to store long surviving objects. Typically, a threshold is set for young generation object and when that age is met, the object gets moved to the old generation. Eventually the old generation needs to be collected. This event is called a **major garbage collection**.


### Resources
* https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html
