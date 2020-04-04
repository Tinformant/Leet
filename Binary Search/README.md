# TODO
* 66 Plus One

# Two Pointers
* 1 Two Sum
* 88 Merge Sorted Array
* 160 Intersection of Two Linked List
* 167 Two Sum II
* 283 Moving Zeroes
* 209 Minimum Size Subarray Sum


# Binary Search
Binary search **only works in a sorted array**. Thus if an input array is not sorted, make it sorted.

**Time Complexity: O(log(n))**

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

## Find the Middle Index
```java
// This may overflow
int mid = (left + right) / 2;
// Use this instead
int mid = left + (right - left) / 2;
```

## Recommended Order for Review
1. 0035 Search Insert Position
2. 0278 First Bad Version
3. 0074	Search a 2D Matrix
4. 0033	Search in Rotated Sorted Array
5. 0081	Search in Rotated Sorted Array II
6. 0034 Find First and Last Position of Element in Sorted Array
