## 0278 First Bad Version
### Binary Search
**Java**
```java
public int firstBadVersion(int n) {
    int slow = 1;
    int fast = n;
    while (slow < fast) {
        int mid = slow + (fast - slow) / 2;
        if (isBadVersion(mid)) {
            fast = mid;
        } else 
            slow = mid + 1;
    }
    return slow;
}
```
**Python**
``python
```
### Hare and Tortoise
