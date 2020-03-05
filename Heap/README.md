# HEAP
## Java.util.PriorityQueue Class
The default Java PriorityQueue is a min heap (head is min).
```java
PriorityQueue<Integer> q = new PriorityQueue<Integer>(); 
```

Min heap: head is min
```java
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
    // compare method must be public
    @Override
    public int compare(Object o1, Object o2)  {
        if (o1 < o2)
            return -1;
        if (o1 == o2)
            return 0;
        else // (o1 > o2)
            return 1;
    }
});
```
Max heap: head is max

```java
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
     // compare method must be public
    @Override
    public int compare(Object o1, Object o2)  {
        if (o1 < o2)
            return 1;
        if (o1 == o2)
            return 0;
        else // (o1 > o2)
            return -1;
    }
});
```
