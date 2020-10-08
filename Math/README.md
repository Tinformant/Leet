## 829 Consecutive Numbers Sum
```java
public int consecutiveNumbersSum(int N) {
    int count = 0;
    for (int i = 1; i * (i - 1) / 2 < N; i++)
        if ((N - i * (i - 1) / 2 ) % i == 0)
            count++;
    return count;

}
```
