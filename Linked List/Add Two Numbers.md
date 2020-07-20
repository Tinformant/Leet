## 2 Add Two Numbers
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = l1;
    int carry = 0;

    ListNode prev = new ListNode(-1);
    prev.next = l1;
    while (l1 != null || l2 != null) {

        int x = (l1 != null) ? l1.val : 0;
        int y = (l2 != null) ? l2.val : 0;

        int sum = x + y + carry;
        carry = sum / 10;
        sum = sum % 10;

        if (l1 != null)
            l1.val = sum;
        else {
            prev.next = l2;
            l2.val = sum;
        }

        if (l1 != null) 
            l1 = l1.next;
        if (l2 != null)
            l2 = l2.next;
        prev = prev.next;
    }

    // For input [5] [5]
    if (carry != 0)
        prev.next = new ListNode(1);

    return dummy;
}
```
## 445 Add Two Numbers II
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();

    while (l1 != null) {
        s1.add(l1.val);
        l1 = l1.next;
    }

    while (l2 != null) {
        s2.add(l2.val);
        l2 = l2.next;
    }

    // 4 -> 3
    // 6 -> 4
    // dummy is a pointer that points to the previous calculated node
    ListNode dummy = null;
    int carry = 0;
    // carry != 0 is for test case [5][5]
    while (!s1.empty() || !s2.empty() || carry != 0) {
        int sum = carry;
        if (!s1.empty()) 
            sum += s1.pop();
        if (!s2.empty()) 
            sum += s2.pop();

        // next is the next significant digit than cur
        ListNode next = new ListNode(sum % 10);
        next.next = dummy;
        dummy = next;
        carry = sum / 10;
    }
    return dummy;
}
```
