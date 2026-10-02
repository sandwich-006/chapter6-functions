"""Chapter 6: Design with Functions — exercises 1–6."""

import math
from functools import reduce


# Exercises 1 and 6: extend the original recursive summation.
def summation(lower, upper, step=1, function=lambda x: x):
    """Sum function(x) from lower through upper using a positive integer step.

    The default function returns x unchanged (the identity function).
    An empty range returns 0. Use small ranges for this recursive exercise.
    """
    if not isinstance(step, int):
        raise TypeError("step must be an integer")
    if step <= 0:
        raise ValueError("step must be greater than zero")
    if lower > upper:
        return 0
    return function(lower) + summation(lower + step, upper, step, function)


# Exercise 2: preserve the recursive displayRange from the original file.
def displayRange(lower, upper):
    """Display each integer from lower through upper, one per line."""
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)


# Example inputs: the exercises specify names, but not particular values.
numbers = [-10, -3, 0, 2, 5, -7, 8]
words = ["Python", " ", "functions", " ", "are", " ", "useful."]

# Exercise 3: map abs to every number, then collect the results in a list.
absolute_values = list(map(abs, numbers))

# Exercise 4: keep only positive numbers; zero is not positive.
positive_numbers = list(filter(lambda x: x > 0, numbers))

# Exercise 5: concatenate strings exactly as given, including their spaces.
# The initial empty string also makes an empty words list return "".
combined_words = reduce(lambda left, right: left + right, words, "")


def main():
    """Run a demonstration of all six exercises."""
    print("1. Recursive summation(1, 10):", summation(1, 10))
    print("\n2. Recursive displayRange(1, 10):")
    displayRange(1, 10)
    print("\nInput numbers:", numbers)
    print("3. Mapping - absolute values:", absolute_values)
    print("4. Filtering - positive numbers:", positive_numbers)
    print("\nInput words:", words)
    print("5. Reducing - combined string:", combined_words)
    print("\n6. Summation with default and optional arguments:")
    print("summation(1, 10) =", summation(1, 10))
    print("summation(1, 10, 2) =", summation(1, 10, 2))
    print("summation(1, 100, 2, math.sqrt) =",
          summation(1, 100, 2, math.sqrt))


if __name__ == "__main__":
    main()
