## 0103 Binary Tree Zigzag Level Order Traversal
BFS's default order of traversing a tree is from left to right. To generate the desired zigzag order, key here is to store the values in a deque, where new values can be added on either end of the queue.

**Java**
```java
public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    if (root == null) 
        return new ArrayList<List<Integer>>();

    List<List<Integer>> ans = new ArrayList<>();

    LinkedList<TreeNode> q = new LinkedList<TreeNode>();
    q.add(root);
    // null is used to signal the end of a level.
    q.addLast(null);

    boolean left_to_right = true;
    LinkedList<Integer> curLevel = new LinkedList<>();

    while (!q.isEmpty()) {
        TreeNode cur = q.pollFirst();
        if (cur != null) {
            if (left_to_right)
                curLevel.addLast(cur.val);
            else
                curLevel.addFirst(cur.val);

            if (cur.left != null)
                q.addLast(cur.left);
            if (cur.right != null)
                q.addLast(cur.right);
        } else {
            ans.add(curLevel);
            curLevel = new LinkedList<>();
            if (!q.isEmpty())
                 // null is used to signal the end of a level.
                q.addLast(null);
            left_to_right = !left_to_right;
        }
    }
    return ans;
}
```
