## 0226 Invert Binary Tree
### Recursion
**Java**
```Java
public TreeNode invertTree(TreeNode root) {
    if (root == null) 
        return null;

    TreeNode temp;
    temp = root.left;
    root.left = root.right;
    root.right = temp;

    invertTree(root.left);
    invertTree(root.right);

    return root;

}
```
**Python**



### Iteration
**Java**
```
public TreeNode invertTree(TreeNode root) {
    if (root == null)
        return null;

    Deque<TreeNode> queue = new ArrayDeque<>();
    queue.add(root);

    while(!queue.isEmpty()) {
        TreeNode cur = queue.removeFirst();
        TreeNode temp = cur.left;
        cur.left = cur.right;
        cur.right = temp;

        if (cur.left != null)
            queue.add(cur.left);
        if (cur.right != null)
            queue.add(cur.right);
    }
    return root;

}
```
**Python**
