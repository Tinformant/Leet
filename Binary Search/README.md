# Binary Search

## Find the middle index
```java
// This may overflow
int mid = (left + right) / 2;
// Use this instead
int mid = right + (left - right) / 2;
```
