```java
    public int maxProduct(int[] nums) {
        
        if (nums == null || nums.length == 0)
            return 0;
        
        int max = nums[0]; // max product till the last position
        int min = nums[0]; // min product till the last position
        int out = nums[0]; // global max
        
        for (int i = 1; i < nums.length; i++) {
            int temp = max;
            max = Math.max(nums[i], Math.max(nums[i] * max, nums[i] * min));
            min = Math.min(nums[i], Math.min(nums[i] * temp, nums[i] * min));
            out = Math.max(out, max);
        }
        return out;   
    }
```
