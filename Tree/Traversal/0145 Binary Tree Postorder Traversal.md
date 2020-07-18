## 145 Binary Tree Postorder Traversal
### Iterative Postorder Traversal
```java
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> out = new LinkedList<>();
    Stack<TreeNode> stack = new Stack<>();

    stack.push(root);
    while (root != null && !stack.isEmpty()) {
        root = stack.pop();
        out.addFirst(root.val);
        if (root.left != null)
            stack.push(root.left);
        if (root.right != null)
            stack.push(root.right);
    }
    return out;
}
```
