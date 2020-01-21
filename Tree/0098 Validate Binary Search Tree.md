## Recursive Solution
**Java**
My initial approach is:
```java
public boolean isValidBST(TreeNode root) {

    if (root == null)
        return true;
    else if (root.left != null && root.val <= root.left.val)
        return false;
    else if (root.right != null && root.val >= root.right.val)
        return false;
    else 
        return isValidBST(root.left) && isValidBST(root.right);


}
```
The above cannot solve [10, 5, 15, null, null, 6, 20], because this approach only makes comparison within each branch. This approach can ensure that each (node, left child, right child) combo is legit but unable to ensure the correctness of entire tree.

The correct recursive solution is to use a helper function to keep track the allowed upper and lower limit for each (node, left child, right child) combo.
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
