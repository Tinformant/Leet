## 104 Maximum Depth of Binary Tree
TODO: iterative solution

### Recursive Solution:
**java**
```java
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
```
### Iterative Solution
**java**

