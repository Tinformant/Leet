Brute Force:
```java
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target)
                return new int[] {i, j};
        }
    }
    return null;
}
```
* Time Complexity: O(n2)
* space Complexity: O(1)

Two-Pass Hash Map
```
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; ++i) 
        map.put(nums[i], i);
    for (int i = 0; i < nums.length; ++i) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i)
            return new int[] {i, map.get(complement)};
    }
    return null;
}
```
* Time Complexity: O(n)
* space Complexity: O(n)

One-Pass Hash Map
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; ++i) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i)
            return new int[] {i, map.get(complement)};
        else 
            map.put(nums[i], i);
    }
    return null;
}
```
* Time Complexity: O(n)
* space Complexity: O(n)
