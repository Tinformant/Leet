# HEAP
int compare(Object o1, Object o2) 返回一个基本类型的整型

如果要按照升序排序，
```
if (o1 < o2)
    return -1;
if (o1 == o2)
    return 9;
if (o1 > o2)
    return 1;
```
如果要按照降序排序
if o1 < o2，return 1 ，相等返回0，01大于02返回-1（负数）

```java
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
    @Override
    public int compare(ListNode o1,ListNode o2){
        if (o1.val < o2.val)
            return -1;
        else if (o1.val == o2.val)
            return 0;
        else 
            return 1;
    }
});
```
