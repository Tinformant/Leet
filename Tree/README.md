## Binary Tree
* Only constraint is that a binary tree has at most two children.

## Binary Search Tree
* Left child less than parent
* Right child greater than parent
* No duplicate node
* The left and right subtree each must also be a BST.

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
1. Inorder: left -> root -> right
```java
void printInOrder (Node node) {
    if (node == null) return;
    
    printInOrder(node.left);
    System.out.println(node.value);
    printInOrder(node.right);
}
```
* Inorder traversal of BST is an array sorted in the ascending order.
* Inorder traversal is not a unique identifier of BST.
2. Preorder: root -> left -> right
```java
void printPreOrder (Node node) {
    if (node == null) return;
    
    System.out.println(node.value);
    printPreOrder(node.right);
    printPreOrder(node.left);
}
```
* Preorder traversal is a unique identifier of BST.

3. Postorder: left -> right -> root
```java
void printPostOrder (Node node) {
    if (node == null) return;

    printPreOrder(node.left);
    printPreOrder(node.right);
    System.out.println(node.value);
}
```
* Postorder traversal is a unique identifier of BST.

**inorder = sorted(postorder) = sorted(preorder)**

**inorder + postorder** or **inorder + preorder** are both unique identifiers of whatever binary tree.

## Search
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
Sources
1. https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
