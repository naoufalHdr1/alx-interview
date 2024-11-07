# 0x05. N Queens
`#Algorithm` `#Python`

## Project Overview

The **N Queens** problem is a classic computer science and mathematical challenge. The objective is to place `N` queens on an `N×N` chessboard in such a way that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

This project involves using a backtracking algorithm to generate all possible configurations of N queens on the board and verify that each solution adheres to the constraints of the problem.

## Prerequisites

To complete this project, you will need to understand the following:
- **Backtracking Algorithms**: Using recursive approaches to explore all possible solutions and backtrack when a solution path is invalid.
- **Recursion**: Implementing recursive functions to apply the backtracking technique.
- **Python Lists**: Creating and manipulating lists to store queen positions.
- **Command-Line Arguments in Python**: Using the `sys` module to manage command-line inputs.

## Usage

The program should be run from the command line as follows:
```bash
./0-nqueens.py N
```

- **N**: the size of the board (and the number of queens). It must be an integer greater than or equal to 4.

### Output

- Each solution will be printed on a new line as a list of `[row, column]` pairs, where each pair represents the position of a queen on the board.

Example:
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### Error Handling

- If the program is executed with the wrong number of arguments, it should output:
```plaintext
Usage: nqueens N
```

- If `N` is not a valid integer, output:
```plaintext
N must be a number
```

- If `N` is less than 4, output:
```plaintext
N must be at least 4
```

## Solution Strategy

This solution involves using a **backtracking algorithm** to recursively place queens on the board, ensuring that each placement meets the non-attacking conditions. When a placement fails to meet these conditions, the algorithm backtracks and attempts a different placement.

## Example Execution
```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```
