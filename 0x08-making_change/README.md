# 0x08. Making Change
`#Algorithm` `#Python`

## Overview

This project explores a classic algorithmic problem: **the coin change problem**. The goal is to determine the minimum number of coins required to meet a specific total amount, given a list of coin denominations. It emphasizes understanding and applying concepts from **greedy algorithms** and **dynamic programming** while ensuring solutions are efficient and meet runtime constraints.

## Learning Objectives

By completing this project, you will:
- Understand **greedy algorithms** and their application to optimization problems.
- Learn the principles of **dynamic programming** for solving problems with overlapping subproblems and optimal substructure.
- Analyze and optimize **algorithmic complexity** (time and space).
- Strengthen your **Python programming** skills by implementing efficient functions.

## Task

### Change Comes From Within

Implement the function `def makeChange(coins, total)`:

Requirements:
- If `total` is `0` or less, return `0`.
- If `total` cannot be met with any combination of the coins, return `-1`.
- Assume coins are integers greater than `0`.
- You have an **infinite supply** of each coin denomination.
- The solution will be evaluated for runtime efficiency.

Example Usage:
```bash
$ ./0-main.py
7
-1
```

## Concepts

1. Greedy Algorithms
- Selects the best choice at each step.
- May not always guarantee the global optimum for the coin change problem (depending on coin denominations).

2. Dynamic Programming
- Breaks the problem into smaller overlapping subproblems.
- Guarantees an optimal solution for all denominations but may be computationally expensive.

3. Algorithmic Complexity
- Time complexity: Analyze the efficiency of your approach.
- Space complexity: Optimize memory usage where possible.
