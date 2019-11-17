### 0094 Binary Tree Inorder Traversal
```java
List<Integer> out = new ArrayList<>();
void inOrder (TreeNode node) {
    if (node == null) return;
        inOrder(node.left);
        out.add(node.val);
        inOrder(node.right);
}

public List<Integer> inorderTraversal(TreeNode root) {
    inOrder(root);
    return out;
}
```
