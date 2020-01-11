```java
public int lengthOfLongestSubstring(String s) {
    
    Set<Character> set = new HashSet<>();
    int out = 0;
    int start = 0;
    int end = 0;
    while (start < s.length() && end < s.length()) {
        if (!set.contains(s.charAt(end))) {
            set.add(s.charAt(end++));
            out = Math.max(out, end - start);
        }
        else
            set.remove(s.charAt(start++));
    }
    return out;
}
```
