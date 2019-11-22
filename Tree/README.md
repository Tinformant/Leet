## Binary Search Tree
* Left child less than parent
* Right child greater than parent
* The left and right subtree each must also be a BST.
A binary tree has at most two kids.
```java
class BinaryTree {
    Node root;

    BinaryTree(int key) {
        root = new Node(key);
    }
    
    class Node {
        int key;
        Node left, right;

        Node (int item) {
            key = item;
            left = right = null;
        }
    }
}
```


### Time Complexity
* Insert, remove and search: average case O(logn), worst case O(n)



## Tree Traversal
### Depth First Traversal
1. Inorder: left -> root -> right
2. Preorder: root -> left -> right
3. Postorder: left -> right -> root

```java
void printInOrder (Node node) {
    if (node == null) return;
    
    printInOrder(node.left);
    System.out.println(node.value);
    printInOrder(node.right);
}
void printPreOrder (Node node) {
    if (node == null) return;
    
    System.out.println(node.value);
    printPreOrder(node.right);
    printPreOrder(node.left);
}
void printPostOrder (Node node) {
    if (node == null) return;

    printPreOrder(node.left);
    printPreOrder(node.right);
    System.out.println(node.value);
}
```

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