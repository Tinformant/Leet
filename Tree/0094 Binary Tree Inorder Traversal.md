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
```java
public List<Integer> inorderTraversal(TreeNode root) {
    Stack<TreeNode> stack = new Stack<>();
    List<Integer> out = new ArrayList<Integer>();

    while(root != null || !stack.isEmpty()) {
        while (root != null) {
            stack.push(root);
            root = root.left;
        }

        root = stack.pop();
        out.add(root.val);
        root = root.right;
    }

    return out;
}
```
**Python**
```Python
public List<Integer> inorderTraversal(TreeNode root) {
    if (root == null) return null;

    Stack<TreeNode> stack = new Stack<>();
    List<Integer> out = new ArrayList<Integer>();

    stack.push(root);
    root = root.left;
    while( !stack.isEmpty()) {
        while (root != null) {
            stack.push(root);
            root = root.left;
        }

        root = stack.pop();
        out.add(root.val);
        root = root.right;
        if (root != null)
            stack.push(root);
    }

    return out;
}
```

