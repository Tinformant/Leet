# Binary Tree Traversal
* 94 Binary Tree Inorder Traversal
* 144 Binary Tree Preorder Traversal
* 145 Binary Tree Postorder Traversal
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal
Basic BFS/DFS
* 515 Find Largest Value in Each Tree Row
* 637 Average of Levels in Binary Tree
## Preorder, Inorder and Postorder
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

## BFS/DFS
### DFS
```java
void DFS (Node root) {
  if (root == null) 
    return;
  visit(root);
  root.visited = true;
  for each (Node n in root.adjacent) {
    if (n.visited == false) {
    search(n);
}
```
### BFS
1. First move horizontally and visit all the nodes of the current layer
2. Then, move to the next layer
3. Key is using a queue.
## Morris Traversal
