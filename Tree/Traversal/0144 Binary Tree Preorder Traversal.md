## 0144 Binary Tree Preorder Traversal
### Iterative Preorder Traversal
```java    
public List<Integer> preorderTraversal(TreeNode root) {
    Deque<TreeNode> queue = new ArrayDeque<>();
    List<Integer> out = new LinkedList<>();

    if (root == null)
        return out;

    queue.add(root);
    while (!queue.isEmpty()) {
        root = queue.poll();
        out.add(root.val);
        if (root.left != null) 
            queue.add(root.left);
        if (root.right != null) 
            queue.add(root.right);            
    }
    return out;
}
```
