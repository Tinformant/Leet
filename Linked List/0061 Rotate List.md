## 61 Rotate List
```java
public ListNode rotateRight(ListNode head, int k) {
    if (head == null)
        return null;

    if (head.next == null)
        return head;

    // Count the total number of noes
    int count = 1;
    ListNode cur = head;
    while ((cur = cur.next) != null) 
        count++;

    k = k % count;
    if (k == 0)
        return head;
    k = count - k;


    cur = head;
    System.out.println(k);
    for (int i = 1; i < k; i++) 
        cur = cur.next;
    ListNode out = cur.next;
    cur.next = null;

    cur = out;
    while (cur.next != null)
        cur = cur.next;

    cur.next = head;

    return out;
}
```
