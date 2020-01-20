## 0203 Remove Linked List Elements

```java
public ListNode removeElements(ListNode head, int val) {
    
    while (head != null && head.val == val)
        head = head.next;
    
    if (head == null)
        return null;
    
    ListNode temp = new ListNode(-1);
    temp.next = head;
    while (temp != null && temp.next != null) {
        while (temp.next != null && temp.next.val == val)
            temp.next = temp.next.next;
        temp = temp.next;
    }
    return head;
}
```
