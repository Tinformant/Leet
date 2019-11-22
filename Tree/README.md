TODO: iterative DFS

Good source: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
### DFS
```java
void DFS (Node root) {
  if (root == null) return;
  visit(root);
  root.visited = true;
  for each (Node n in root.adjacent) {
    if (n.visited == false) {
    search(n);
}
```
### BFS
1. First move horizontally and visit all the nodes of the current layer
2. Move to the next layer

The key is using a queue.
```java
void BFS (Node root) {
  Queue queue = new Queue();
  root.marked = true;
  queue.enqueue(root);
  
  while (!queue.isEmpty()) {
    node r = queue.dequeue();
    visit(r);
    foreach (Node n in r.adjacent) {
      if (n.marked == false) {
        n.marked = true;
        queue.enqueue(n);
      }
    }
  }
}
```
