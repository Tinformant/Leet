## 0515 Find Largest Value in Each Tree Row
### BFS
```java
public List<Integer> largestValues(TreeNode root) {
    List<Integer> out = new LinkedList();
    Queue<TreeNode> q = new LinkedList();

    if (root != null)
        q.add(root);
    while (!q.isEmpty()) {
        int size = q.size();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < size; i++) {
            TreeNode cur = q.poll();
            if (cur.left != null)
                q.add(cur.left);
            if (cur.right != null)
                q.add(cur.right);
            if (cur.val > max)
                max = cur.val;
        }
        out.add(max);
    }
    return out;
}
```
