### Longest Substring Without Repeating Characters
Wrong attemps
java```
public int lengthOfLongestSubstring(String s) {
    int globalMax = 0;
    int curMax = 0;
    Map<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        char curChar = s.charAt(i);
        if (!map.containsKey(curChar)) {
            map.put(curChar, i);
            curMax++;
        } else {
            curMax = curMax - (map.get(curChar) + 1);
            curMax++;
            map.put(curChar, i);
        }
        globalMax = Math.max(globalMax, curMax);
    }
    return globalMax;
}
```
