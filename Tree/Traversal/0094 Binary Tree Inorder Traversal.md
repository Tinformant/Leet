## 94 Binary Tree Inorder Traversal
### Iterative Inorder Traversal
```java
public List<Integer> inorderTraversal(TreeNode root) {
    Stack<TreeNode> stack = new Stack<>();
    List<Integer> out = new LinkedList<>();
    // One of the condition has to be root != null
    // Or won't pass [1, null, 2, 3]
    while (!stack.isEmpty() || root != null) {
        while (root != null) {
            stack.add(root);
            root = root.left;
        }
        root = stack.pop();
        out.add(root.val);
        root = root.right;
    }
    return out;
}
```
