## 206 Reverse Linked List

**Iterative Solution**
```java
/* The iterativce solution is just reversing next.
 *         1 -> 2 -> 3 -> null
 * null <- 1 <- 2 <- 3 <- null
 */
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode cur = head;

    while (cur != null) {
        ListNode temp = cur.next;
        cur.next = prev;
        prev = cur;
        cur = temp;
    }
    return prev;
}
```

* Time Complexity: O(n)
* Space Complexity: O(1)


**Recursivetive Solution**
```java
public ListNode reverseList(ListNode head) {

}
```
