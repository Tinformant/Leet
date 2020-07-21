## 637 Average of Levels in Binary Tree
```java
public List<Double> averageOfLevels(TreeNode root) {
    List<Double> out = new LinkedList();
    Queue<TreeNode> q = new LinkedList();

    q.add(root);
    while (!q.isEmpty()) {
        int size = q.size();
        // sum should be long to avoid integer overflow
        long sum = 0;
        for (int i = 0; i < size; i++) {
            TreeNode cur = q.remove();
            sum += cur.val;
            if (cur.left != null)
                q.add(cur.left);
            if (cur.right != null)
                q.add(cur.right);
        }

        // Convert sum to double
        out.add(sum * 1.0 / size);
    }
    return out;
}
```
