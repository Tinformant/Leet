## 0155 Min Stack
### Linked List
**Java**
```java
class MinStack {
    class Node {
        int val;
        int min;
        Node prev;
        
        Node(int val, int min, Node prev) {
            this.val = val;
            this.min = min;
            this.prev = prev;
        }
    }
    
    Node head;
    

    /** initialize your data structure here. */
    public MinStack() {
    }
    
    public void push(int x) {
        if (head == null)
            head = new Node(x, x, null);
        else {
            Node newNode = new Node(x, Math.min(x, head.min), head);
            head = newNode;
        }
    }
    
    public void pop() {
        if (head != null)
            head = head.prev;
    }
    
    public int top() {
        if (head != null) 
            return head.val;
        else 
            return -1;
    }
    
    public int getMin() {
        if (head != null)
            return head.min;
        else 
            return -1;
    }
}
```
**Python**

### One Stack
**Java**

**Python**
