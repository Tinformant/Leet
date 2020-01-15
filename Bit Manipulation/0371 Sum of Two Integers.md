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
