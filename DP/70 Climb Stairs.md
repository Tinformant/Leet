current is the number of ways to get to the current step. next is the number of ways to get to the next step. For each iteration of the while loop, 
1) update the new next to be the sum of the old next and old current; 2) the old next becomes the new current.
```java
    public int climbStairs(int n) {
        int current = 1;
        int next = 1;
        while (n-- > 0) {
            int temp = next;
            next = next + current;
            current = temp;
        }
        return current;
    }
```
