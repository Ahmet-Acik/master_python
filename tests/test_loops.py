import unittest
from loops import (
    range_sequence,
    iterate_list,
    iterate_string,
    iterate_dict,
    while_loop_example,
    while_loop_with_break,
    while_loop_with_continue,
    while_loop_with_else,
    nested_loops,
    enumerate_example,
    zip_example,
    reversed_example,
    sorted_example,
    do_while_example,
    while_loop_with_else_example,
)


class TestLoops(unittest.TestCase):

    def test_range_sequence(self):
        self.assertEqual(range_sequence(1, 6), [1, 2, 3, 4, 5])
        self.assertEqual(range_sequence(1, 10, 2), [1, 3, 5, 7, 9])
        self.assertEqual(range_sequence(5, 0, -1), [5, 4, 3, 2, 1])
        self.assertEqual(range_sequence(5, 0, -2), [5, 3, 1])

    def test_iterate_list(self):
        self.assertEqual(
            iterate_list(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"]
        )

    def test_iterate_string(self):
        self.assertEqual(iterate_string("Ahmet"), ["A", "h", "m", "e", "t"])

    def test_iterate_dict(self):
        self.assertEqual(
            iterate_dict({"name": "Ahmet", "age": 21, "city": "Istanbul"}),
            [("name", "Ahmet"), ("age", 21), ("city", "Istanbul")],
        )

    def test_while_loop_example(self):
        self.assertEqual(while_loop_example(8), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(while_loop_example(3), [1, 2])

    def test_while_loop_with_break(self):
        self.assertEqual(while_loop_with_break(10), [1, 2, 3])

    def test_while_loop_with_continue(self):
        self.assertEqual(while_loop_with_continue(5), [1, 2, 4, 5])

    def test_while_loop_with_else(self):
        self.assertEqual(
            while_loop_with_else(5), [1, 2, 3, 4, "i is no longer less than 5"]
        )

    def test_nested_loops(self):
        self.assertEqual(
            nested_loops(3, 2), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        )

    def test_enumerate_example(self):
        self.assertEqual(
            enumerate_example(["apple", "banana", "cherry", "mango", "orange"]),
            [(0, "apple"), (1, "banana"), (2, "cherry"), (3, "mango"), (4, "orange")],
        )

    def test_zip_example(self):
        self.assertEqual(
            zip_example(["apple", "banana", "cherry"], ["red", "yellow", "pink"]),
            [("apple", "red"), ("banana", "yellow"), ("cherry", "pink")],
        )

    def test_reversed_example(self):
        self.assertEqual(
            reversed_example(["apple", "banana", "cherry"]),
            ["cherry", "banana", "apple"],
        )

    def test_sorted_example(self):
        self.assertEqual(
            sorted_example(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"]
        )
        self.assertEqual(
            sorted_example(["apple", "banana", "cherry"], reverse=True),
            ["cherry", "banana", "apple"],
        )
        self.assertEqual(
            sorted_example(["apple", "strawberry", "banana", "cherry"], key=len),
            ["apple", "banana", "cherry", "strawberry"],
        )

    def test_do_while_example(self):
        self.assertEqual(do_while_example(5), [0, 1, 2, 3, 4])

    def test_while_loop_with_else_example(self):
        self.assertEqual(
            while_loop_with_else_example(10),
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "Count is no longer greater than 0."],
        )


if __name__ == "__main__":
    unittest.main()
