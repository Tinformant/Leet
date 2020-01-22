## 0098 Validate Binary Search Tree.md
### Recursive Solution
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
```
boolean helper(Integer lowerLimit, TreeNode node, Integer upperLimit) {
    if (node == null)
        return true;
    else if (upperLimit != null && node.val >= upperLimit)
        return false;
    else if (lowerLimit != null && node.val <= lowerLimit)
        return false;
    else
        // lowerLimit < node < upperLimit
        // lowerLimit < left < node
        // node < right < upperLimit
        return helper(lowerLimit, node.left, node.val) && helper(node.val, node.right, upperLimit);
}

public boolean isValidBST(TreeNode root) {
    return helper(null, root, null);        
}
```
