## 0598 Range Addition II
### Brute Force
**Java**
```java
public int maxCount(int m, int n, int[][] ops) {
    int[][] arr = new int[m][n];

    for (int[] op : ops) {
        for (int i = 0; i < op[0]; i++)
            for (int j = 0; j< op[1]; j++)
                arr[i][j]++;
    }
    int count = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (arr[i][j] == arr[0][0])
                count++;
    return count;
}
```
### One Pass
**Java**
```java
public int maxCount(int m, int n, int[][] ops) {
    for (int[] op : ops) {
        m = Math.min(m, op[0]);
        n = Math.min(n, op[1]);
    }
    return m * n;
}
```
**Python**
```python
def maxCount(self, m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    if not ops:
        return m*n
    return min(op[0] for op in ops)*min(op[1] for op in ops)
```    
