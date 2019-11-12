### 0139 Word Break
Subproblem is if subarray(0, i) can be segmented into words from the dictionary. So dp[0] means whether subarray(0, 0) (which is an empty string) can be segmented, and of course the answer is yes.

```java
public boolean wordBreak(String s, List<String> wordDict) {
    boolean[] dp = new boolean[s.length() + 1];
    dp[0] = true;
    
    for (int i = 1; i < s.length() + 1; ++i) {
        for (int j = 0; j < i; ++j) {
            if (dp[j] && wordDict.contains(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length()];
}
```
