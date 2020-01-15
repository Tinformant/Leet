## 0371 Sum of Two Integers
Idea: 
1. Use a bit mask of 1 to gauge each bit. 
2. The mask starts as 1.
3. For loop starts with comparing the last bit n. If the last bit of n is 1, then n & mask != 0.
4. Signed Left shift mask, mask becomes 10, 100, 1000...
```java
public int hammingWeight(int n) {
    int count = 0;
    int mask = 1;
    for (int i = 0; i < 32; i++) {
        if ((n & mask) != 0) 
            count++;
        mask <<= 1;
    }
    
    return count;
}
```
## 0268 Missing Number
1. A number XOR with itself is 0.
2. nums has length n, so xor every element with its index will result in n ^ missing;
3. (n ^ missing) ^ n will result in missing.
```java
public int missingNumber(int[] nums) {
    int missing = nums.length;
    for (int i = 0; i < nums.length; ++i) 
        missing ^= i ^ nums[i];
    return missing;
}
```
