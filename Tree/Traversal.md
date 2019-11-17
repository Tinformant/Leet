#### 0094 Binary Tree Inorder Traversal
```java
List<Integer> out = new ArrayList<>();
void inOrder (TreeNode node) {
    if (node == null) return;
        inOrder(node.left);
        out.add(node.val);
        inOrder(node.right);
}

public List<Integer> inorderTraversal(TreeNode root) {
    inOrder(root);
    return out;
}
```
#### 0102 Binary Tree Level Order Traversal
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    if (root == null)
        return ans;
    Queue<TreeNode> que = new ArrayDeque<>();
    que.add(root);
    while (!que.isEmpty()) {
        List<Integer> curLevel = new ArrayList<>();  
        int s = que.size();
        // Cannot put que.size() as the termination condition in the for loop
        // que is mutable!!
        for (int i = 0; i < s; ++i) {  
            TreeNode node = que.remove();
            curLevel.add(node.val);
            
            if (node.left != null) que.add(node.left);
            if (node.right != null) que.add(node.right);
        }
        ans.add(curLevel);
    }
    return ans;
}
```
