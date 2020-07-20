## 199 Binary Tree Right Side View
### BFS
* Basic BFS that returns the last node of each row.
```java
public List<Integer> rightSideView(TreeNode root) {
    Queue<TreeNode> q = new LinkedList();
    List<Integer> out = new LinkedList();

    if (root != null)
        q.add(root);
    while (!q.isEmpty()) {
        int size = q.size();
        TreeNode node = null;
        for (int i = 0; i < size; i++) {
            node = q.poll();
            if (node.left != null)
                q.add(node.left);
            if (node.right != null)
                q.add(node.right);
        }
        out.add(node.val);
    }
    return out;
}
```
### DFS
