# 0x09. Island Perimeter
`#Algorithm` `#Python`

## Overview
This project focuses on developing an algorithm to calculate the perimeter of an island represented in a 2D grid. The grid is a matrix of integers where:
- `0` represents water.
- `1` represents land.

Your task is to write a Python function that computes the perimeter of the island, following specific constraints and conditions.

## Learning Objectives

Through this project, you will:
- Understand and navigate 2D arrays (lists of lists in Python).
- Apply conditional logic to solve a geometric problem.
- Develop an algorithm to count and calculate the perimeter of a shape in a grid context.
- Reinforce concepts like iterative loops and data structure manipulation.

## Implementation

### Function

Write a function def `island_perimeter(grid):` that:
1. Input: A 2D grid of integers.
- `0` represents water.
- `1` represents land.
- Each cell is square with side length = 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is completely surrounded by water.
- The island is a single connected component without internal "lakes."

2. Output: The perimeter of the island.

### Steps to Solve

1. Analyze the Grid
- Iterate through each cell in the grid.
- For every `1` (land cell), check its adjacent cells:
    - If the adjacent cell is `0` (water) or out of bounds, it contributes to the perimeter.
2. Count the Perimeter
- Each land cell has four potential edges.
- Subtract edges that are shared with neighboring land cells.

### Constraints

- Grid dimensions do not exceed `100 x 100`.
- Ensure your function handles edge cases efficiently:
    - Completely water grids.
    - Rectangular grids with varying dimensions.

### Testing

To test your function:
1. Save the function in `0-island_perimeter.py`.
2. Use the provided `0-main.py` script to test the function with sample grids.
