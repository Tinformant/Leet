## Iteration instead of Recursion
* 94 Binary Tree Inorder Traversal
* 144 Binary Tree Preorder Traversal
* 145 Binary Tree Postorder Traversal

## Construct BT
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal



#### 0094 Binary Tree Inorder Traversal
An simple inorder traversal.
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
A simple bfs.
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

#### 112 Path Sum
```java
public boolean hasPathSum(TreeNode root, int sum) {
    if (root == null) 
        return false;
    
    if (root.left == null && root.right == null)
        if (root.val == sum)
            return true;
    
    return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
}
```
TODO: bfs and dfs
