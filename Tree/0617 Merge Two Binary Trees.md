## 0617 Merge Two Binary Trees.md
### Recursion
**Java**
```java
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    if (t1 == null)
        return t2;
    else if (t2 == null)
        return t1;
    else {
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }
}
```
**Python**
### Iteration
**Java**
```java
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    if (t1 == null)
        return t2;
    Stack < TreeNode[] > stack = new Stack <> ();
    stack.push(new TreeNode[] {t1, t2});
    while (!stack.isEmpty()) {
        TreeNode[] t = stack.pop();
        if (t[0] == null || t[1] == null) {
            continue;
        }
        t[0].val += t[1].val;
        if (t[0].left == null) {
            t[0].left = t[1].left;
        } else {
            stack.push(new TreeNode[] {t[0].left, t[1].left});
        }
        if (t[0].right == null) {
            t[0].right = t[1].right;
        } else {
            stack.push(new TreeNode[] {t[0].right, t[1].right});
        }
    }
    return t1;
}
```
