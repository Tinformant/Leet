## 0101 Symmetric Tree
### Recursive Solution
**Java**
```java
boolean isMirror (TreeNode left, TreeNode right) {
        if (left == null && right == null)
            return true;
        if (left == null || right == null)
            return false;
        if (left.val != right.val)
            return false;
        return isMirror(left.left, right.right) && isMirror(left.right, right.left);
    }

public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}
```
**Python**
```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left, right):
            if left == right:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        if root is None:
            return True
        return isMirror(root.left, root.right)
```

## Iterative Solution
**Java**

**Python**
