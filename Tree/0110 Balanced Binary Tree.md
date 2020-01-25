## 0110 Balanced Binary Tree
### Top-down recursion
**Java**
```java
class Solution {
    int getHeight(TreeNode node) {
        if (node == null)
            return 0;
        int left = getHeight(node.left);
        int right = getHeight(node.right);
        if (left == -1 || right == -1 || Math.abs(left - right) > 1)
            return -1;
        return Math.max(left, right) + 1;
    }
    
    public boolean isBalanced(TreeNode root) {
        return getHeight(root) != -1;
    }
}
```


### Bottom-up recursion
**Java**
```java
class Solution {
    int getHeight(TreeNode node) {
        if (node == null)
            return 0;
        return Math.max(getHeight(node.left), getHeight(node.right)) + 1;
    }
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        return Math.abs(getHeight(root.left) - getHeight(root.right)) < 2 
                && isBalanced(root.left) 
                 && isBalanced(root.right);
    }
}
```
