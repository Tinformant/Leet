# Binary Search
Binary search **only works in a sorted array**. If the input array is not sorted, make it sorted.

## Binary Search Algorithm
```java
// Given input of int[] nums, int target
int l = 0;
int r = nums.length - 1;
while (l <= r) {
    int m = l + (r - l) / 2;
    if (nums[m] < target)
        l = m + 1;
    else if (nums[m] > target)
        r = m - 1;
    else
        return m;
```

## Find the middle index
```java
// This may overflow
int mid = (left + right) / 2;
// Use this instead
int mid = left + (right - left) / 2;
```
