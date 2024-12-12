# 0x0A. Prime Game

## Overview
This project involves solving a competitive game scenario using principles of **prime numbers**, **game theory**, and **algorithm optimization**. The game pits two players, **Maria** and **Ben**, against each other. They take turns removing prime numbers and their multiples from a set of consecutive integers. The player unable to make a move loses the game.

This project will help solidify your understanding of:
- Prime numbers
- Efficient algorithms like the Sieve of Eratosthenes
- Game theory and strategic decision-making
- Dynamic programming/memoization for optimization

---

## Learning Objectives
By completing this project, you will:
1. Understand and implement efficient algorithms to identify prime numbers.
2. Learn to apply game theory to create winning strategies.
3. Optimize calculations using dynamic programming or memoization.
4. Develop clean and efficient Python code adhering to PEP 8 standards.

---

## Concepts and Resources

### Prime Numbers and Algorithms
- **Prime Numbers**: A number greater than 1 that has no divisors other than 1 and itself.
- **Sieve of Eratosthenes**: An efficient algorithm to find all primes up to a given limit.
  - [Prime Numbers: Introduction](https://www.khanacademy.org/)
  - [Sieve of Eratosthenes in Python](https://realpython.com/python-prime-numbers/)

### Game Theory
- **Game Theory Basics**: Understanding optimal play in turn-based games.
  - [Introduction to Game Theory](https://plato.stanford.edu/entries/game-theory/)

### Dynamic Programming
- **Dynamic Programming**: A method to optimize calculations by storing intermediate results.
  - [Dynamic Programming in Python](https://www.geeksforgeeks.org/dynamic-programming/)

### Python Programming
- **Lists**: Essential for managing the game state and tracking numbers.
  - [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)

---

## Project Requirements

### Directory Structure
```plaintext
0x0A-primegame/
├── 0-prime_game.py
├── main_0.py
└── README.md

## Task: Prime Game

### Problem Description

Maria and Ben play `x` rounds of the game. For each round:
1. The set of integers is from `1` to `n` (inclusive).
2. Players take turns picking a prime number from the set and removing that prime and its multiples.
3. The player unable to make a move loses.

### Example Usage

run the `main_0.py` file.

### Implementation Notes

- **Optimal Play**: Both players will always choose the move that maximizes their chances of winning.
- **Efficiency**: Leverage the Sieve of Eratosthenes to precompute primes up to the maximum n in nums.
- **Scalability**: Ensure the solution handles up to 10,000 rounds with n values as high as 10,000.
