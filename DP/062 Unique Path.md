062 Unique Paths
```java
public int uniquePaths(int m, int n) {
    int[][] dp = new int[m][n];
    
    for (int i = 0; i < m; ++i) 
        dp[i][0] = 1;
    
    for (int i = 0; i < n; ++i) 
        dp[0][i] = 1;
    
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}
```
063 Unique Paths II
```java
public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    
    if (obstacleGrid[0][0] == 1)
        return 0;
    
    int row = obstacleGrid.length;
    int col = obstacleGrid[0].length;
   
    int[][] dp = new int[row][col];
    for (int i = 0; i < row; ++i)
        Arrays.fill(dp[i], 0);
    
    for (int i = 0; i < row; ++i) {
        if (obstacleGrid[i][0] != 1) {
            dp[i][0] = 1;
        } else {
            break;
        }
    }
    
    for (int i = 0; i < col; ++i) {
        if (obstacleGrid[0][i] != 1) {
            dp[0][i] = 1;
        } else {
            break;
        }
    }
    
    
    for (int i = 1; i < row; ++i) {
        for (int j = 1; j < col; ++j) {
            if (obstacleGrid[i][j] == 1) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
    }
    return dp[row - 1][col - 1];
}
```
