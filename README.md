# Chapter 6: Design with Functions

Author: darwish

Python exercises based on Kenneth A. Lambert, *Fundamentals of Python: First Programs*, 2nd Edition, Chapter 6. Uses only the Python standard library.

## Run

Open this folder in VS Code, select a Python 3 interpreter, and run `main.py`, or use:

```shell
python main.py
python -m unittest -v
```

If `python` is not available in your terminal, use the full path to your selected Python interpreter. In PowerShell: `& 'path/to/python.exe' main.py`.

## Exercises

1. **Recursive summation:** `summation(1, 10)` returns `55`. Exercises 1 and 6 share the final extended function, preserving the original two-argument call.
2. **Recursive displayRange:** Prints each integer from the lower bound through the upper bound. Each call increases `lower` by 1; recursion stops when `lower > upper`.
3. **Mapping:** `list(map(abs, numbers))` creates a list of absolute values.
4. **Filtering:** `list(filter(lambda x: x > 0, numbers))` keeps positive numbers. Zero is excluded, and the original list is unchanged.
5. **Reducing:** `reduce(lambda left, right: left + right, words, "")` concatenates strings in order. It preserves the supplied spaces and returns an empty string for an empty list.
6. **Default arguments:** `summation(lower, upper, step=1, function=lambda x: x)` applies a function to each visited value before adding the results. The identity lambda returns its argument unchanged.

The recursive call passes both `step` and `function` onward so that later calls keep the caller's choices.

```python
summation(1, 10)                   # 55
summation(1, 10, 2)                # 25
summation(1, 100, 2, math.sqrt)     # approximately 333.415276
```

The last example adds `sqrt(1) + sqrt(3) + ... + sqrt(99)`. The value 100 is not visited because the sequence starts at 1 and advances by 2. Pass `math.sqrt` without parentheses to supply the function itself.

The exercises name `numbers` and `words` without specifying their contents. The demonstration uses negative numbers, zero, and positive numbers, plus strings with explicit spaces. These sample inputs can be changed.

This exercise expects integer bounds and a positive integer step. Invalid steps are rejected to prevent recursion that never reaches the base case. An empty ascending range returns 0. Use small ranges because Python limits recursion depth.

The `if __name__ == "__main__":` guard runs the demonstration only when the file is executed directly; importing the module does not print it.

## Expected results

| Operation | Result |
| --- | --- |
| `summation(1, 10)` | `55` |
| `displayRange(1, 10)` | `1` through `10`, one per line |
| Absolute values | `[10, 3, 0, 2, 5, 7, 8]` |
| Positive numbers | `[2, 5, 8]` |
| Combined string | `Python functions are useful.` |
| `summation(1, 10, 2)` | `25` |
| `summation(1, 100, 2, math.sqrt)` | Approximately `333.415276` |

## Tests

`test_main.py` contains 12 tests covering the original sum, empty and single-value ranges, step behavior, invalid steps, custom functions, the square-root example, recursive argument propagation, printed ranges, list operations, and quiet imports.

## Textbook references

Page numbers refer to the uploaded textbook; PDF page positions are listed in parentheses.

- Pages 176-177 (PDF 198-199): recursive `displayRange` and `summation`.
- Pages 193-194 (PDF 215-216): default and optional arguments.
- Pages 195-198 (PDF 217-220): higher-order functions, mapping, filtering, reducing, and lambda.
- Pages 199-200 (PDF 221-222): exercises corresponding to assignment items 3-6.

The textbook PDF is not included in this repository.

## Repository

https://github.com/sandwich-006/chapter6-functions

To save and publish future changes after testing:

```shell
git add main.py test_main.py README.md .gitignore
git commit -m "Update Chapter 6 exercises"
git push
```
