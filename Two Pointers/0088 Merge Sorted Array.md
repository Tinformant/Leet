## 0088 Merge Sorted Array
## Merge and Sort
**Java**

**Python**
### Two Pointers
**Java**
```java
public void merge(int[] nums1, int m, int[] nums2, int n) {
    int ptr1 = m - 1;
    int ptr2 = n - 1;
    int cur = m + n - 1;

    while (ptr1 > -1 && ptr2 > -1) {
        if (nums1[ptr1] > nums2[ptr2]) {
            nums1[cur] = nums1[ptr1];
            ptr1--;
        } else {
            nums1[cur] = nums2[ptr2];
            ptr2--;
        }
        cur--;
    }
    while (ptr1 != -1) {
        nums1[cur] = nums1[ptr1];
        cur--;
        ptr1--;
    }
    while (ptr2 != -1) {
        nums1[cur] = nums2[ptr2];
        cur--;
        ptr2--;
    }
}
```
**Python**
