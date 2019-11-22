0096 Unique Binary Search Trees
```java
public int numTrees(int n) {
    // # of unique trees at length n
    int[] dp = new int[n + 1];
    
    // n = 0 is somehow 1 tree
    dp[0] = 1;
    
    // n = 1;
    dp[1] = 1;
    
    for (int length = 2; length <= n; length++) {
        for (int root = 1; root <= length; root++) {
            int left = dp[root - 1];
            int right = dp[length - root];
            dp[length] += left * right;
        }
    }
    return dp[n];
}
```
