## 0215 Kth Largest Element in an Array
### Sort
**Java**
```java
public int findKthLargest(int[] nums, int k) {
    Arrays.sort(nums);
    return nums[nums.length - k];
}
```
**Python**
```python
```

### Heap
