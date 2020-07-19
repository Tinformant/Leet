## 145 Binary Tree Postorder Traversal
### Iterative Preorder Traversal: Tweak the Order of the Output
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
### Iterative Postorder Traversal
```java
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> out = new LinkedList<>();
    Stack<TreeNode> stack = new Stack<>();

    while (root != null || !stack.isEmpty()) {
        while (root != null) {
            if (root.right != null)
                stack.push(root.right);
            stack.push(root);
            root = root.left;
        }
        root = stack.pop();
        if (!stack.isEmpty() && stack.peek() == root.right) {
            stack.pop();
            stack.push(root);
            root = root.right;
        } else {
            out.add(root.val);
            root = null;
        }
    }
    return out;
```
