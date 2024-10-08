# 0x01. Lockboxes

## Description

This project involves solving a problem where you are presented with a set of locked boxes. Each box may contain keys to other boxes, and the goal is to determine if all the boxes can be unlocked, starting from box 0, which is always unlocked by default.

The challenge requires applying algorithmic techniques to traverse through the boxes and unlock them based on the keys contained within each box. This problem can be visualized as a graph traversal where boxes represent nodes and keys represent edges to other nodes (boxes).

## Project Overview

You are provided with `n` locked boxes. Each box is numbered from `0` to `n - 1` and contains a list of keys. A key with the number `x` opens the box with number `x`. The task is to determine whether all boxes can be opened, starting from the first box (box `0`), which is always unlocked.

## Prototype

```python
def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    pass
```
- `boxes` is a list of lists. Each list represents a box, and the contents of each list represent the keys inside that box.
- The first box, `boxes[0]`, is unlocked by default.
- A key corresponds to the number of a box that it can open. For example, if a box contains key `k`, it can open box `k`.
- Return `True` if all boxes can be unlocked, otherwise return `False`.

## Requirements

- General:
    - You must write a function called `canUnlockAll` that meets the above specifications.
    - The project must be completed using Python 3, specifically on Ubuntu 20.04 LTS.
    - Your code should follow the PEP 8 style guide (version 1.7.x).
    - All Python scripts should be executable and include a shebang (`#!/usr/bin/python3`) at the start of the file.

## Concepts and Resources

Before solving this problem, it is important to have a good understanding of the following key concepts:

1. Lists and List Manipulation

You should be familiar with how to:
- Access elements in a list.
- Iterate over lists.
- Modify lists dynamically.

**Resource:** [Python Lists (Official Documentation)](https://intranet.alxswe.com/rltoken/TtGNy9p1p1d0O5G1rdY1Aw)

2. Graph Theory Basics

The problem can be thought of as a graph traversal, where each box represents a node and keys are edges to other nodes. You can apply:

- **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to traverse the keys and boxes.

**Resource:** [Graph Theory (Khan Academy)](https://intranet.alxswe.com/rltoken/eVcYI8g-6nF0Na46xnRdhw)

3. Algorithmic Complexity

Understanding time and space complexity helps optimize the solution and avoid inefficient algorithms.

**Resource:** [Big O Notation (GeeksforGeeks)](https://intranet.alxswe.com/rltoken/01qym1qAJUkLrb47PvqnKg)

4. Recursion

Some solutions might benefit from using recursion to navigate through the boxes and keys.

**Resource:** [Recursion in Python (Real Python)](https://intranet.alxswe.com/rltoken/zpEuvv0l9EHohIx-HwiAAA)

5. Queue and Stack

Both queues and stacks are important for implementing BFS or DFS algorithms. For example:

- Queue for BFS.
- Stack for DFS.

**Resource:** [Queue and Stack in Python (GeeksforGeeks)](https://intranet.alxswe.com/rltoken/CQLm4RJrdwyo2DAcNCtwIA)

6. Set Operations

Sets are useful for tracking visited boxes and available keys efficiently.

**Resource:** [Python Sets (Official Documentation)](https://intranet.alxswe.com/rltoken/zkmtaPqAbKyxx41kRw7ulA)

## Example Usage

Below is an example of how the function can be used:
```python
#!/usr/bin/python3
from 0_lockboxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Approach

### Step-by-Step Solution

1. Initialization:

- Start with box 0 unlocked.
- Use a list or set to keep track of the boxes that have been unlocked.

2. Traversal:

- Traverse through each box, collecting the keys found.
- Mark each box that has been unlocked.
- For each key, check if it can open another box that hasn't been unlocked yet.

3. Termination:

- If all boxes are unlocked, return `True`.
- If some boxes remain locked even after using all keys, return `False`.

### Algorithm

You can solve this problem using either BFS or DFS. Both approaches involve maintaining a list of unlocked boxes and exploring the boxes as you collect keys. If you successfully unlock all boxes, the function returns `True`. Otherwise, it returns `False`.

### Time Complexity

- In the worst case, the algorithm might need to visit each box multiple times, but the set operations ensure that already unlocked boxes are not revisited unnecessarily.
- The overall complexity is `O(n + k)` where `n` is the number of boxes, and `k` is the total number of keys encountered.

### Task

0. Lockboxes: Write a function `canUnlockAll` that determines if all boxes can be opened.
