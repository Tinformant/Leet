0096 Unique Binary Search Trees
```java
public int numTrees(int n) {
    // # of unique trees at length n
    int[] dp = new int[n + 1];
    
    // n = 0 is somehow 1 tree
    dp[0] = 1;
    
    // n = 1;
    dp[1] = 1;
    
    for (int curN = 2; curN <= n; curN++) {
        for (int root = 1; root <= curN; root++) {
            int left = dp[root - 1];
            int right = dp[curN - root];
            dp[curN] += left * right;
        }
    }
    return dp[n];
}
```
dp is the number of unique BST at different length. Say, when filling up dp[2], the inner loop decides which number (from 1 to curN) will be the root of a tree. Variables right and left mean the right and left brances of a BST. Thus, the total number of BST given a cerntain number is the root is __num of right branches x num of left branches__

When curN = 3, there are 3 cases:
1. when 1 is the root, total num of BST = __num of right branches x num of left branches__
2. when 2 is the root, total num of BST = __num of right branches x num of left branches__
3. when 3 is the root, total num of BST = __num of right branches x num of left branches__
Total number of BST for n = 3 is the sum of the above three.
