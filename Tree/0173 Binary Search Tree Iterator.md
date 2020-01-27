## 0173 Binary Search Tree Iterator
### Flattening BST
**Java**
```java
class BSTIterator {
    
    List<Integer> list;
    void helper(TreeNode node) {
        if (node.left != null)
            helper(node.left);
        list.add(node.val);
        if (node.right != null)
            helper(node.right);
    } 


    public BSTIterator(TreeNode root) {            
        list = new LinkedList<>();
        if (root != null)
             helper(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        // Assume call to next() always valid
        return list.remove(0);
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !list.isEmpty();
    }
}
```
**Python**
### Controlled Recursion
**Java**

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
