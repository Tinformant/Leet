## 203 Remove Linked List Elements
### Iteration
* Time Complexity: O(n)
* Space Complelxity :O(1)

**Java**
```java
public ListNode removeElements(ListNode head, int val) {
    ListNode dummy = new ListNode(-1);
    dummy.next = head;

    ListNode prev = dummy;
    while (head != null) {
        if (head.val == val)
            prev.next = head.next;
        else
            prev = head;
        head = head.next;
    }
    return dummy.next;
}
```
**Python**
```python
def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    while head:
        if head.val == val:
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return dummy.next;
```
### Recursion
