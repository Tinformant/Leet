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
**Python**
