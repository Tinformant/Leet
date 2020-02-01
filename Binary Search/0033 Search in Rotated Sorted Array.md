## 0033 Search in Rotated Sorted Arra
```java
public int search(int[] nums, int target) {
	int l = 0;
	int h = nums.length - 1;

	while (l <= h) {
		int m = l + (h - l) / 2;
		int cur = nums[m];
		
		if ((cur < nums[0]) != (target < nums[0])) 
			cur = target < nums[0] ? Integer.MIN_VALUE : Integer.MAX_VALUE;

		// Can we compare with nums.length - 1?
		// if ((cur < nums[nums.length - 1]) != (target < nums[nums.length - 1]))  
		//     cur = target < nums[0] ? Integer.MAX_VALUE : Integer.MIN_VALUE;

		if (cur < target) 
			// Can we have l = mid?
			l = m + 1;
		else if (cur > target)
			h = m - 1;
		else 
			return m;
	}
	return -1;
}
```
