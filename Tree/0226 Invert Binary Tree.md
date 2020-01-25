## 0226 Invert Binary Tree
### Recursion
**Java**
```Java
public TreeNode invertTree(TreeNode root) {
    if (root == null) 
        return null;

    TreeNode temp;
    temp = root.left;
    root.left = root.right;
    root.right = temp;

    invertTree(root.left);
    invertTree(root.right);

    return root;

}
```
**Python**
```python
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```
### Iteration
**Java**
```java
public TreeNode invertTree(TreeNode root) {
    if (root == null)
        return null;

    Deque<TreeNode> queue = new ArrayDeque<>();
    queue.add(root);

    while(!queue.isEmpty()) {
        TreeNode cur = queue.removeFirst();
        TreeNode temp = cur.left;
        cur.left = cur.right;
        cur.right = temp;

        if (cur.left != null)
            queue.add(cur.left);
        if (cur.right != null)
            queue.add(cur.right);
    }
    return root;

}
```
**Python**
```Python
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None

    arr = [root]
    while len(arr) != 0:
        cur = arr.pop()
        temp = cur.left
        cur.left = cur.right
        cur.right = temp

        if cur.left != None:
            arr.append(cur.left)
        if cur.right != None:
            arr.append(cur.right)
    return root
```
