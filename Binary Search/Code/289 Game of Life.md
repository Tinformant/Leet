# 289 Game of Life
## Keep a Copy Board
```java
public void gameOfLife(int[][] board) {
    int[][] neighbors = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    int rows = board.length;
    int cols = board[0].length;

    int[][] copy = new int[rows][cols];

    for (int i = 0; i < rows; i++) 
        for (int j = 0; j < cols; j++)
            copy[i][j] = board[i][j];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int liveNeighbors = 0;
            for (int[] n : neighbors) {
                int newRow = i + n[0];
                int newCol = j + n[1];

                if (newRow < 0 || newCol < 0 || newRow > rows - 1 || newCol > cols - 1)
                    continue;

                if (copy[newRow][newCol] == 1)
                    liveNeighbors++;
            }
            if (copy[i][j] == 1 && (liveNeighbors < 2 || liveNeighbors > 3))
                board[i][j] = 0;
            else if (copy[i][j] == 0 && liveNeighbors == 3)
                board[i][j] = 1;
        }
    }
}
```
* Time Complexity: O(M x N) 
* Space Complexity: O(M x N)
## Change in Place
```java
public void gameOfLife(int[][] board) {
    int[][] neighbors = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    int rows = board.length;
    int cols = board[0].length;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int liveNeighbors = 0;
            for (int[] n : neighbors) {
                int newRow = i + n[0];
                int newCol = j + n[1];

                if (newRow < 0 || newCol < 0 || newRow > rows - 1 || newCol > cols - 1)
                    continue;

                if (board[newRow][newCol] == 1 || board[newRow][newCol] == -1)
                    liveNeighbors++;
            }
            if (board[i][j] == 1 && (liveNeighbors < 2 || liveNeighbors > 3))
                board[i][j] = -1;
            else if (board[i][j] == 0 && liveNeighbors == 3)
                board[i][j] = 2;
        }
    }
    for (int i = 0; i < rows; i++) 
        for (int j = 0; j < cols; j++) {
            if (board[i][j] == -1)
                board[i][j] = 0;
            else if (board[i][j] == 2)
                board[i][j] = 1;
        }
}
```
* Time Complexity: O(M x N) 
* Space Complexity: O(1)
