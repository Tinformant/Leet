# Binary Search
Binary search **only works in a sorted array**. If the input array is not sorted, make it sorted.

## Find the middle index
```java
// This may overflow
int mid = (left + right) / 2;
// Use this instead
int mid = right + (left - right) / 2;
```
