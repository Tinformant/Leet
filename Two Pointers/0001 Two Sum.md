## 0001 Two Sum
### Brute Force:
**Java**
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
**Python**
```python
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None;
```
* Time Complexity: O(n2)
* space Complexity: O(1)

Two-Pass Hash Map
**java*
```java
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
**python
```python
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_dict = {}
    for i, num in enumerate(nums):
        my_dict[num] = i;

    for i, num in enumerate(nums):            
        complement = target - num
        if complement in my_dict and my_dict.get(complement) != i:
            return [i, my_dict.get(complement)]
    return None
```
* Time Complexity: O(n)
* space Complexity: O(n)

One-Pass Hash Map
**Java**
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
**Python**
```python
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in my_dict and my_dict.get(complement) != i:
            return [i, my_dict.get(complement)]
        my_dict[num] = i;
    return None
 ```
* Time Complexity: O(n)
* space Complexity: O(n)
