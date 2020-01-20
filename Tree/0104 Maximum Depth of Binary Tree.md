## 104 Maximum Depth of Binary Tree
TODO: iterative solution

### Recursive Solution:
**Java**
```java
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
```
**Python**
```python
def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
### Iterative Solution
**java**

