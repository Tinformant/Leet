## 0378 Kth Smallest Element in a Sorted Matrix
### Heap Brute Force
```java
public int kthSmallest(int[][] matrix, int k) {
    PriorityQueue<Integer> q = new PriorityQueue<Integer>(); 

    for (int i = 0; i < matrix.length; ++i) 
        for (int j = 0; j < matrix.length; ++j)
            q.add(matrix[i][j]);

    for (int i = 0; i < k - 1; i++)
        q.poll();

    return q.poll();        
}
```

### Better Heap
```java

```
