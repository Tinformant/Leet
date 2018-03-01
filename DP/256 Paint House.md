## 256 Paint House
The subproblem is finding out the cost at the kth house. For the k+1 house, the cost is the min(cost at k + cost at k-1).
```java
    public int minCost(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        int[][] dp = new int[costs.length][3];
        
        // dp[m][n] is the cost minimum cost at house m and color n.
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
        
        for (int i = 1; i < costs.length; i++) {
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
        }
        return Math.min(dp[costs.length - 1][0], Math.min(dp[costs.length - 1][1], dp[costs.length - 1][2]));   
    }
```
