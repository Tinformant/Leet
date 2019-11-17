#### 100 Same Tree
Recursive Solution
```java
public boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null)
        return true;
    
    if (p == null || q == null)
        return false;
    
    if (p.val != q.val)
        return false;
    
    return isSameTree(p.right, q.right) && isSameTree(q.left, p.left);
}
```
TODO iterative solution

#### 101 Symmetric Tree
```java
boolean isMirror (TreeNode left, TreeNode right) {
        if (left == null && right == null)
            return true;
        if (left == null || right == null)
            return false;
        if (left.val != right.val)
            return false;
        return isMirror(left.left, right.right) && isMirror(left.right, right.left);
    }

public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
    return isMirror(root.left, root.right);
}
```
