Great source: https://leetcode.com/explore/learn/card/binary-search/
# Two Pointer + Sliding Window + Binary Search
# First time
* 238 Product of Array Except Self
* 561 Array Partition I 
* 48 Rotate Image

# Two Pointers
* 1 Two Sum
* 11 Container with Most Water
* 15 3Sum
* 16 3Sum Closest
* 26 Remove Duplicates from Sorted Array
* 27 Remove Element
* 88 Merge Sorted Array
* 160 Intersection of Two Linked List
* 167 Two Sum II
* 283 Moving Zeroes
* 209 Minimum Size Subarray Sum

# Other
* 28 Implement strStr()
* 283 Move Zeroes
* 56 Merge Intervals
* 169 Majority Element

# Bad Questions
* 31 Next Permutation
* 66 Plus One

# Binary Search Recommended Order for Review
1. 35 Search Insert Position
2. 278 First Bad Version
3. 74	Search a 2D Matrix
4. 33	Search in Rotated Sorted Array
5. 81	Search in Rotated Sorted Array II
6. 34 Find First and Last Position of Element in Sorted Array

# Sliding Window
* 3 Longest Substring Without Repeating Characters    


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



* 375 Guess Number Higher or Lower
