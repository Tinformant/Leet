Great source: https://leetcode.com/explore/learn/card/binary-search/
# First time
* 53 Maximum Subarray
* 15 3Sum
* 121 Best Time to Buy and Sell Stock
* 238 Product of Array Except Self
* 561 Array Partition I 
* 169 Majority Element
* 66 plus one
* 283 Move Zeroes
* 88 Merge Sorted Array
* 122 Best Time to Buy and Sell Stock II
* 16 3Sum Closest
* 48 Rotate Image
* 56 Merge Intervals
* 31 Next Permutation
* 289 Game of Life
* 73 Set Matrix Zeroes


# TODO



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
