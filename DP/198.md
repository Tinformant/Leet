## 198 House Robber
The optimal outcome at the kth house is either:
1. equal to the optimal outcome at the k-1 house (robbing the k-1 house will stop the robber from robbing the kth house)
2. OR equal to the optimal outcome at the k-2 house PLUS the loot at kth house
```java
    public int rob(int[] nums) {
        
        // When there are 2 houses or fewer.
        if (nums.length == 0) 
            return 0;
        if (nums.length == 1) 
            return nums[0];
        if (nums.length == 2) 
            return Math.max(nums[0], nums[1]);
        
        // dp stores the optimal solution at a certain house so far 
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
            
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        
        return Math.max(dp[nums.length - 1], dp[nums.length - 2]);
    }
```

