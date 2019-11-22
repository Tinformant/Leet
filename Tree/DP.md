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
For the double for loop:
```
The outer loop fills up the dp array. For example, when length = 2, it is calculating the number of unique trees when n = 2.
When length = 2, the inner loop decides which number (from 1 to length) will be the root of a tree. Variable right and left mean the right and left brances of a BST. Thus, the total number of BST when 1 is the root is 
    # of right branches x # of left branches
```
