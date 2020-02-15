# HEAP
Min heap: head is min
```java
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
    @Override
    int compare(Object o1, Object o2)  {
        if (o1 < o2)
            return -1;
        if (o1 == o2)
            return 0;
        if (o1 > o2)
            return 1;
    }
});
```
Max heap: head is max

```java
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
    @Override
    int compare(Object o1, Object o2)  {
        if (o1 < o2)
            return 1;
        if (o1 == o2)
            return 0;
        if (o1 > o2)
            return -1;
    }
});
```
