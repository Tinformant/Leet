## 0160 Intersection of Two Linked Lists
## Hash Set
**Java**
```java
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    Set<ListNode> set = new HashSet<>();

    while (headA != null) {
        set.add(headA);
        headA = headA.next;
    }

    while (headB != null) {
        if (set.contains(headB))
            return headB;
        headB = headB.next; 
    }

    return null;
}
```
**Python**
```python
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    node_set = set()
    while headA != None:
        node_set.add(headA)
        headA = headA.next
    while headB != None:
        if headB in node_set:
            return headB
        headB = headB.next

    return None
```
### Two Pointers
**Java**
```java
```

**Python**
```python
```


