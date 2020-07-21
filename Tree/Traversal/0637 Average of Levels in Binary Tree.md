## 637 Average of Levels in Binary Tree
### BFS
* Just a basic application of BFS.
* Only thing to watch is to use a long for sum to avoid integer overflow.
* Time Complexity: O(n) - n is the total # of nodes
* Space Complexity: O(m) - m is the maximum # of nodes in any level

**Java**
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
