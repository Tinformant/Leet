# Binary Tree Traversal
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal
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

## Morris Traversal
