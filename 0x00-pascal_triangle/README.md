# Pascal's Triangle

## Project Overview

This project involves implementing a function that generates Pascal's Triangle, a mathematical concept where each number is the sum of the two directly above it. The project will help reinforce your understanding of fundamental Python concepts, including lists, loops, and functions.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Resources](#resources)
- [License](#license)

## Introduction

Pascal's Triangle is a triangular array of the binomial coefficients. The first few rows of Pascal's Triangle are:

1 1 1 1 2 1 1 3 3 1 1 4 6 4 1

This project aims to create a Python function that generates a specified number of rows of Pascal's Triangle.

## Requirements

To successfully complete this project, you should be familiar with the following Python concepts:

- **Lists and List Comprehensions:** Creating, accessing, modifying, and iterating over lists.
- **Functions:** Defining and calling functions, passing parameters, and returning values.
- **Loops:** Utilizing for and while loops for iteration.
- **Conditional Statements:** Applying if, elif, and else conditions to implement logic.
- **Recursion (Optional):** Understanding base and recursive cases for generating rows.
- **Arithmetic Operations:** Performing addition to calculate elements in the triangle.
- **Indexing and Slicing:** Accessing elements and slices of lists.
- **Memory Management:** Being mindful of how lists are stored and copied.
- **Error and Exception Handling (Optional):** Using try-except blocks to handle potential errors.
- **Efficiency and Optimization:** Considering time and space complexity of the solution.

## Usage

To use the `pascal_triangle` function, simply call it with an integer argument representing the number of rows you want to generate. For example:

```python
from pascal_triangle import pascal_triangle

# Generate Pascal's Triangle with 5 rows
triangle = pascal_triangle(5)
print(triangle)
```

The output will be:

```python
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

If you provide a non-positive integer (n <= 0), the function will return an empty list.

## Implementation Details

The function `pascal_triangle(n)` is implemented in the file `0-pascal_triangle.py` and is designed to return a list of lists representing the triangle. It employs a nested loop structure to build each row based on the previous one, ensuring that the edges of the triangle are always 1.

## Function Definition
```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Parameters:
    n (int): The number of rows to generate.
    
    Returns:
    triangle: A list of lists representing Pascal's Triangle.
    """
```

## Resources

[What is Pascal’s Triangle] (https://intranet.alxswe.com/rltoken/F458nFkW9StJum2zPI4khg) /
[Pascal’s Triangle - Numberphile] (https://intranet.alxswe.com/rltoken/XXMN2RVCCGcF5l5ZnUIv8Q) /
[What are Python Algorithms] (https://intranet.alxswe.com/rltoken/q5v0xbgrVxG4Nf-fV-BW2w)

## License

Feel free to modify any section to better fit your project needs or add any additional information you think is necessary!
