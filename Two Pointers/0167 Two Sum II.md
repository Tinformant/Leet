## 0167 Two Sum II
### Two Pointers
**Java**
```java
public int[] twoSum(int[] numbers, int target) {
    int slow = 0;
    int fast = numbers.length - 1;

    while (slow < fast) {
        if (numbers[slow] + numbers[fast] == target)
            return new int[] {slow + 1, fast + 1};
        else if (numbers[slow] + numbers[fast] < target) 
            slow++;
        else 
            fast--;
    }
    return null;
}
```
**Python**
```python
def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    fast = len(numbers) - 1
    slow = 0
    while slow < fast:
        if numbers[slow] + numbers[fast] == target:
            return [slow + 1, fast + 1]
        elif numbers[slow] + numbers[fast] < target:
            slow += 1
        else:
            fast -= 1
    return None 
```
