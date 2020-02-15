# HEAP

```java
PriorityQueue<ListNode> queue= new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
    @Override
    public int compare(ListNode o1,ListNode o2){
        if (o1.val < o2.val)
            return -1;
        else if (o1.val==o2.val)
            return 0;
        else 
            return 1;
    }
});
```
