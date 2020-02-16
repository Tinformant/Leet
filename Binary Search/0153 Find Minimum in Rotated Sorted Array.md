## 0153 Find Minimum in Rotated Sorted Array
### Binary Search
**Java**
```java
public int findMin(int[] num) {
    if (num == null || num.length == 0)
        return 0;

    if (num[num.length - 1] > num[0])
        return num[0];

    // If input is rotated
    int l = 0;
    int h = num.length - 1;
    while (l < h) {
        int m = (h - l) / 2 + l;

        // Case 1: [4, 5, 1, 2, 3]
        // m > 0 for test case [2, 1]
        if (m > 0 && num[m - 1] > num[m])
            return num[m];

        // Case 2: [2, 3, 4, 5, 1]
        // Min in on the right side of m
        else if (num[l] <= num[m] && num[m] > num[h])
            l = m + 1;

        // Case 3: [5, 1, 2 ,3 ,4]
        // Min is on the left side of m
        else
            h = m - 1;
    }
    return num[l];
}
```
