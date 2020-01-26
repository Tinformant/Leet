## 0160 Intersection of Two Linked Lists
## Hash Set
```java
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    Set<ListNode> set = new HashSet<>();

    while (headA != null && headB != null) {
        if (set.contains(headA))
            return headA;
        else
            set.add(headA);
        if (set.contains(headB))
            return headB;
        else
            set.add(headB);
        headA = headA.next;
        headB = headB.next;            
    }

    ListNode cur = headA == null ? headB : headA;

    while (cur != null) {
        if (set.contains(cur))
            return cur;
        else {
            set.add(cur);
            cur = cur.next; 
        }
    }
    return null;
}
```
