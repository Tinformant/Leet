322 Coin Change

Bottom-Up
```java
public int coinChange(int[] coins, int amount) {
    
    int max = amount + 1;
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, max);
    dp[0] = 0;
    
    for (int i = 1; i < amount + 1; ++i) {
        for (int coin : coins) {
            if (coin <= i ) {
                // Watch out for overflow/underflow
                // We are doing plus one even if there is no solution to subprolem
                dp[i] = Math.min(dp[i] , dp[i -  coin] + 1);
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
```
