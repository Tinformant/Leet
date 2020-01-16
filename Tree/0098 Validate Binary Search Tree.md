```java
boolean validate(TreeNode node, Integer lower, Integer upper) {
    if (node == null)
        return true;

    int val = node.val;
    if (lower != null && val <= lower)
        return false;
    if (upper != null && val >= upper)
        return false;

    if (!validate(node.right, val, upper))
        return false;
    if (!validate(node.left, lower, val))
        return false;

    return true;    
}
public boolean isValidBST(TreeNode root) {
    return validate(root, null, null);
}
```
