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

Improved Iterative
**Java**
```Java
  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

      ListNode head = new ListNode(-1);        
      ListNode cur = head;

      while (l1 != null && l2 != null) {
          if (l1.val < l2.val) {
              cur.next = l1;
              l1 = l1.next;
          } else {
              cur.next = new ListNode(l2.val);
              cur.next = l1;
              l2 = l2.next;
          }
          cur = cur.next;
      }

      if (l1 != null)  
          cur.next = l1;
      else 
          cur.next = l2;

      return head.next;
  }
```
* Time complexity: O(n)
* Space complexity: O(1)

### Iterative Solution
```java
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(-1);
    ListNode ptr = dummy;

    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            ptr.next = l1;
            l1 = l1.next;

        } else {
            ptr.next = l2;
            l2 = l2.next;
        }
        ptr = ptr.next;
    }

    /* Instead of
    if (l1 != null)
        ptr.next = l1;
    if (l2 != null)
        ptr.next = l2;
    Do the below:
    */
    ptr.next = (l1 != null) ? l1 : l2;

    return dummy.next;
}
```
* Time complexity: O(n)
* Space complexity: O(1)

### Recursive solution
```java
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null)
            return (l1 != null) ? l1 : l2;
        
        ListNode ptr1 = l1;
        ListNode ptr2 = l2;
        
        if (l1.val <= l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
```
* Time complexity: O(n)
* Space complexity: O(1)

