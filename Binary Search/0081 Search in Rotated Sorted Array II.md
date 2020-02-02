## 0081 Search in Rotated Sorted Array II
```java
public boolean search(int[] nums, int target) {

    if (nums.length == 0)
        return false;

    int l = 0;
    int r = nums.length - 1;

    while (l + 1 < nums.length && nums[l] == nums[l + 1])
        l++;
    // l < r instead of l <= r here for test case [1, 1] 1
    while (l < r && r - 1 >= 0 && nums[r] == nums[r - 1])
        r--;

    while (l <= r) {
        int m = l + (r - l) / 2;
        int cur = nums[m];

        if ((cur < nums[0]) != (target < nums[0])) 
            cur = target < nums[0] ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        if (cur < target) 
            l = m + 1;
        else if (cur > target)
            r = m - 1;
        else 
            return true;
    }

    return false;
}
```
