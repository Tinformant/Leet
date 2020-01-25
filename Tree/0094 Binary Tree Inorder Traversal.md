## 0094 Binary Tree Inorder Traversal
### Recursion
**Java**
```java
class Solution {
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
}
```
**Python** 
```python
def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    out = []
    def helper(node):
        if node is None:
            return None
        helper(node.left)
        out.append(node.val)
        helper(node.right)
    helper(root)
    return out

```
### Iteration
**Java**

