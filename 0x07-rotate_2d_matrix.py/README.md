# 0x07. Rotate 2D Matrix
`#Algorithm` `#Python`

## Overview

This project involves implementing an **in-place algorithm** to rotate an `n x n` 2D matrix by **90 degrees clockwise**. It is designed to enhance your understanding of **matrix manipulation** and **in-place operations** in Python, challenging you to minimize space complexity while achieving the desired transformation.

## Learning Objectives

By completing this project, you will gain insights into:

- **Matrix Representation:** Understand how 2D matrices are represented using lists of lists in Python and learn how to access and modify their elements.
- **In-Place Operations:** Perform operations directly on the matrix without creating copies, optimizing space complexity.
- **Matrix Transposition:** Learn the process of swapping rows with columns.
- **Reversing Rows:** Manipulate the rows of the matrix as part of the rotation process.
- **Nested Loops:** Master nested loops to iterate and modify matrix elements effectively.

## Task

### Rotate 2D Matrix

Write a function `rotate_2d_matrix(matrix)` to rotate a given `n x n` 2D matrix 90 degrees clockwise in-place.

Constraints:
- The matrix is guaranteed to have two dimensions and will not be empty.
- The function should not return anything but modify the `matrix` directly.

### Example

Input:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Output:
```python
matrix = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Implementation Steps
1. Transpose the Matrix:
- Swap elements across the diagonal.
- Example: `[matrix[i][j] = matrix[j][i]]` for `i < j`.

2. Reverse Each Row:
- Reverse the order of elements in each row using slicing or a loop.

### Testing

Run the test file:
```bash
./main_0.py
```
