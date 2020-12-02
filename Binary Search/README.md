Great source: https://leetcode.com/explore/learn/card/binary-search/
# One/Two Pass + Two Pointer + Sliding Window + Binary Search
## First time
* 238 Product of Array Except Self
* 561 Array Partition I 
* 48 Rotate Image

## One/Two Pass Recommended Order for Review
* 1 Two Sum

## Two Pointers Recommended Order for Review
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

## Binary Search Recommended Order for Review
1. 35 Search Insert Position
2. 278 First Bad Version
3. 74	Search a 2D Matrix
4. 33	Search in Rotated Sorted Array
5. 81	Search in Rotated Sorted Array II
6. 34 Find First and Last Position of Element in Sorted Array

# Sliding Window Recommended Order for Review
* 3 Longest Substring Without Repeating Characters   

# Other
* 283 Move Zeroes
* 56 Merge Intervals
* 169 Majority Element

# Bad Questions
Single Pass
* 31 Next Permutation

Two Pointer
* 28 Implement strStr()

Other
* 66 Plus One

# Binary Search
Binary search **only works in a sorted array**. Thus if an input array is not sorted, make it sorted.

**Time Complexity: O(log(n))**

## Find the Middle Index
```java
// This may overflow
int mid = (left + right) / 2;
// Use this instead
int mid = left + (right - left) / 2;
```

## Binary Search Template I
```
Initial Condition: left = 0, right = length - 1
Loop Condition: left <= right
Search Left: right = mid - 1
Search Right: left = mid + 1
Found Target: nums[mid] = target
```
```java
int binarySearch(int[] nums, int target){
  if(nums == null || nums.length == 0)
    return -1;

  int left = 0;
  int right = nums.length - 1;
  while(left <= right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid - 1; }
  }

  // End Condition: left > right
  return -1;
}
```
## Binary Search Template II
```
Initial Condition: left = 0, right = length
Loop Condition: left < right
Search Left: right = mid
Search Right: left = mid + 1
Found Target: nums[mid] = target
```
```java
int binarySearch(int[] nums, int target){
  if(nums == null || nums.length == 0)
    return -1;

  int left = 0, right = nums.length;
  while(left < right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid; }
  }

  // Post-processing:
  // End Condition: left == right
  if(left != nums.length && nums[left] == target) return left;
  return -1;
}
```

* 375 Guess Number Higher or Lower
