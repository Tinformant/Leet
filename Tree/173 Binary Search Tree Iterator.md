## 173 Binary Search Tree Iterator

* next() and hasNext() -> stack
* In the stack, the largest nodes are in the bottom -> reverse inorder traversal

Iterate tree from
```java
public class BSTIterator {
    Stack<TreeNode> stack;
    
    public BSTIterator(TreeNode root) {
        stack = new Stack<>();
        putReverseInOrder(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        return stack.pop().val;
    }
    
    public void putReverseInOrder(TreeNode node) {
        if (node == null) return;
        
        putReverseInOrder(node.right);
        stack.push(node);
        putReverseInOrder(node.left);
    } 
}
```
