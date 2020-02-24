## 0222 Count Complete Tree Nodes
**Java**
```java
public int countNodes(TreeNode root) {

    if (root == null) 
        return 0;
    return 1 + countNodes(root.right) + countNodes(root.left);
}
```
