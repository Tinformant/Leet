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

## Simple Recursion
* 98 Validate Binary Search Tree
* 100 Same Tree
* 101 Symmetric Tree
* 110 Balanced Binary Tree
* 111 Minimum Depth of Binary Tree
* 112 Path Sum
* 113 Path Sum II
* 114 Flatten Binary Tree to Linked List
* 129 Sum Root to Leaf Numbers


## Iteration instead of Recursion
* 94 Binary Tree Inorder Traversal
* 114 Flatten Binary Tree to Linked List
* 144 Binary Tree Preorder Traversal
* 145 Binary Tree Postorder Traversal

## Construct Tree
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal
* 108 Convert Sorted Array to Binary Search Tree

## Search
* 102 Binary Tree Level Order Traversal
* 107 Binary Tree Level Order Traversal II
* 116 Populating Next Right Pointers in Each Node
* 117 Populating Next Right Pointers in Each Node II
* 199 Binary Tree Right Side View
* 637 Average of Levels in Binary Tree

* 437 Path Sum III




## TODO
* 124 Binary Tree Maximum Path Sum
* 129 Sum Root to Leaf Numbers
* 285. Inorder Successor in BST
* 230. Kth Smallest Element in a BST
* 235. Lowest Common Ancestor of a Binary Search Tree
* 236. Lowest Common Ancestor of a Binary Tree
* 450. Delete Node in a BST











