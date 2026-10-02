"""Run with: python -m unittest -v"""

import contextlib
import importlib.util
import io
import math
from pathlib import Path
import unittest

import main


class Chapter6Tests(unittest.TestCase):
    def test_original_summation(self):
        self.assertEqual(main.summation(1, 10), 55)

    def test_empty_range(self):
        self.assertEqual(main.summation(5, 4), 0)

    def test_single_value_and_inclusive_bound(self):
        self.assertEqual(main.summation(3, 3), 3)
        self.assertEqual(main.summation(1, 5, 2), 9)

    def test_step_larger_than_range(self):
        self.assertEqual(main.summation(2, 5, 10), 2)

    def test_nonpositive_step_is_rejected(self):
        for step in (0, -1):
            with self.subTest(step=step), self.assertRaises(ValueError):
                main.summation(1, 10, step)

    def test_fractional_step_is_rejected(self):
        with self.assertRaises(TypeError):
            main.summation(1, 10, 0.5)

    def test_keyword_function(self):
        self.assertEqual(main.summation(-2, 2, function=abs), 6)

    def test_textbook_sqrt_example(self):
        expected = math.fsum(math.sqrt(n) for n in range(1, 101, 2))
        self.assertAlmostEqual(main.summation(1, 100, 2, math.sqrt),
                               expected, places=10)

    def test_recursive_calls_preserve_function_and_step(self):
        visited = []

        def record(n):
            visited.append(n)
            return n * n

        self.assertEqual(main.summation(1, 6, 2, record), 35)
        self.assertEqual(visited, [1, 3, 5])

    def test_display_range(self):
        for lower, upper, expected in ((1, 3, "1\n2\n3\n"),
                                       (4, 4, "4\n"), (5, 4, "")):
            with self.subTest(lower=lower, upper=upper):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    main.displayRange(lower, upper)
                self.assertEqual(output.getvalue(), expected)

    def test_mapping_filtering_and_reducing(self):
        self.assertEqual(main.absolute_values, [10, 3, 0, 2, 5, 7, 8])
        self.assertEqual(main.positive_numbers, [2, 5, 8])
        self.assertEqual(main.combined_words, "Python functions are useful.")
        self.assertEqual(main.numbers, [-10, -3, 0, 2, 5, -7, 8])

    def test_import_does_not_print_demo(self):
        spec = importlib.util.spec_from_file_location(
            "chapter6_import_check", Path(main.__file__))
        module = importlib.util.module_from_spec(spec)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            spec.loader.exec_module(module)
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
