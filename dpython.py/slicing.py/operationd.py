'''Slicing in Python is a way to extract specific parts of a sequence (like lists, strings, or tuples) using a special `start:stop:step` syntax. Here's a breakdown of how slicing works:

### Syntax:
```python
sequence[start:stop:step]
```

- **`start`**: The index where the slicing begins (inclusive). Defaults to `0` if not specified.
- **`stop`**: The index where the slicing ends (exclusive). It goes up to but does not include this index.
- **`step`**: The interval between elements. Defaults to `1`.

---

### Examples:
#### 1. Basic Slicing
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]
```
- Extracts elements from index `1` to `3`.

#### 2. Omitting `start` or `stop`
```python
print(numbers[:3])   # Output: [0, 1, 2]  (start defaults to 0)
print(numbers[3:])   # Output: [3, 4, 5]  (stop goes to the end)
```

#### 3. Using `step`
```python
print(numbers[::2])  # Output: [0, 2, 4]  (every second element)
print(numbers[1::2]) # Output: [1, 3, 5]  (start at index 1, every second element)
```

#### 4. Negative Indices
```python
print(numbers[-3:])  # Output: [3, 4, 5]  (last 3 elements)
print(numbers[:-2])  # Output: [0, 1, 2, 3]  (exclude the last 2 elements)
```

#### 5. Negative Step
```python
print(numbers[::-1]) # Output: [5, 4, 3, 2, 1, 0]  (reverse the list)
print(numbers[4:1:-1]) # Output: [4, 3, 2] (reverse from index 4 to index 1)
```

---

### String Slicing
You can slice strings similarly since they are sequences of characters.
```python
text = "Python"
print(text[1:4])    # Output: "yth"
print(text[::-1])   # Output: "nohtyP" (reverse string)
```

---

### Tuple Slicing
Tuples are immutable but can also be sliced.
```python
tuple_data = (10, 20, 30, 40, 50)
print(tuple_data[1:3])  # Output: (20, 30)
```

---

### Summary Table:
| Operation         | Example           | Result               |
|--------------------|-------------------|----------------------|
| All elements       | `numbers[:]`      | `[0, 1, 2, 3, 4, 5]` |
| First 3 elements   | `numbers[:3]`     | `[0, 1, 2]`          |
| Last 3 elements    | `numbers[-3:]`    | `[3, 4, 5]`          |
| Skip every second  | `numbers[::2]`    | `[0, 2, 4]`          |
| Reverse list       | `numbers[::-1]`   | `[5, 4, 3, 2, 1, 0]` |

Let me know if you'd like additional examples! 😊'''