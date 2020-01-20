## 0021 Merge Two Sorted Lists.md
### Iterative solution
**Java**
```java
  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

      ListNode ptr1 = l1;
      ListNode ptr2 = l2;

      ListNode head = new ListNode(-1);        
      ListNode cur = head;

      while (ptr1 != null && ptr2 != null) {
          if (ptr1.val < ptr2.val) {
              cur.next = new ListNode(ptr1.val);
              ptr1 = ptr1.next;
          } else {
              cur.next = new ListNode(ptr2.val);
              ptr2 = ptr2.next;
          }
          cur = cur.next;
      }

      if (ptr1 != null)  
          cur.next = ptr1;
      else 
          cur.next = ptr2;

      return head.next;
  }
```
* Time complexity: O(n)
* Space complexity: O(n)
