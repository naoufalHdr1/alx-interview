# 0x04. UTF-8 Validation

## Project Overview

This project, **0x04. UTF-8 Validation**, focuses on validating UTF-8 encoded data using Python. You will employ bitwise operations, an understanding of the UTF-8 encoding scheme, and list manipulation to create a function that determines if a given data set represents valid UTF-8 encoding.

## Learning Objectives

1. **Bitwise Operations:** Understand and apply bitwise operations like AND, OR, shifts, and more.

2. **UTF-8 Encoding:** Familiarize yourself with how UTF-8 encodes characters into bytes and the patterns for encoding various character lengths.

3. **Data Representation:** Represent and manipulate data at the byte level, specifically handling the least significant 8 bits of integers.

4. **List Manipulation:** Efficiently work with lists for parsing and validating the encoding sequence.

## Resources

- [Bitwise Operations: Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)\
- [UTF-8 Encoding: UTF-8 Wikipedia, Character Sets]()\
- [Python Lists: Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)\
- [Boolean Logic: Python Boolean Operations]()

## Task

### Task 0: UTF-8 Validation

- **File:** `0-validate_utf8.py`
- **Prototype:** `def validUTF8(data):`
- **Parameters:**
    - `data`: A list of integers representing byte data.
- **Return:** `True` if `data` represents a valid UTF-8 encoding; `False` otherwise.

### Instructions

- Write a function to determine whether the given data list represents a valid UTF-8 encoding sequence.
- Each integer in the list represents a byte (8 least significant bits).
- The function should handle data containing characters from 1 to 4 bytes long.
- **Input Format:** The main file will test different data sequences by running the `validUTF8` function.

### Example
```python
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Usage

To run the main testing file:
```bash
chmod +x 0-main.py
./0-main.py
```
