## 0100 Same Tree
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



