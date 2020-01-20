Recursion is when a method calls itself again and again until it reaches a specified stopping condition. In general, the method mentioned above is called a recursive method.

Recursive Method
1. Base Case: The base case is where the call to the method stops, meaning, it does not make any subsequent recursive calls.
2. Recursive Case: The recursive case is where the method calls itself again and again until it reaches the base case.

Check for prime number
```java
class Solution {
    int i = 2;
    public static Object isPrime(int num, int i) {
        // Write your code here
        // Modify the return statement according to "true"
        // or "false" according to your code
        if (num == 2 || i == num)
            return true;
        else if (num % i == 0)
            return false;
        else 
            return isPrime(num, ++i);
    }
}
```
