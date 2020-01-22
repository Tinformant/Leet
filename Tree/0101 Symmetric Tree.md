## 0101 Symmetric Tree
### Recursive Solution
**Java**
```java
boolean isMirror (TreeNode left, TreeNode right) {
        // Both are null
        if (left == right)
            return true;
        // Only one is null
        if (left == null || right == null)
            return false;
        if (left.val != right.val)
            return false;
        return isMirror(left.left, right.right) && isMirror(left.right, right.left);
    }

public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
    return isMirror(root.left, root.right);
}
```
**Python**

## Iterative Solution
**Java**

**Python**
