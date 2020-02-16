## 0209 Minimum Size Subarray Sum
### One Pass
**Java**
```java
public int minSubArrayLen(int s, int[] nums) {
    int ans = Integer.MAX_VALUE;
    int left = 0;
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        sum += nums[i];
        while (sum >= s) {
            // i - left + 1 is the length of the subarray
            ans = Math.min(ans, i - left + 1);
            sum -= nums[left++];
        }
    }
    return (ans != Integer.MAX_VALUE) ? ans : 0;
}
```
**Python**
