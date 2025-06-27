import sys
import os
import unittest

from conditionals import (
    check_adult,
    check_age_group,
    check_driving_eligibility,
    greet_name,
    check_name_conditions,
    check_name_any_conditions,
    compare_xyz,
    check_game,
    get_month_name,
)

class TestConditionals(unittest.TestCase):

    def test_check_adult(self):
        self.assertEqual(check_adult(21), "You are an adult.")
        self.assertEqual(check_adult(18), "You are an adult.")
        self.assertEqual(check_adult(17), "You are a minor.")
        self.assertEqual(check_adult(0), "You are a minor.")

    def test_check_age_group(self):
        self.assertEqual(check_age_group(21), "You are an adult.")
        self.assertEqual(check_age_group(18), "You are an adult.")
        self.assertEqual(check_age_group(15), "You are a teenager.")
        self.assertEqual(check_age_group(13), "You are a teenager.")
        self.assertEqual(check_age_group(12), "You are a minor.")
        self.assertEqual(check_age_group(0), "You are a minor.")

    def test_check_driving_eligibility(self):
        self.assertEqual(check_driving_eligibility(21, True), "You can drive.")
        self.assertEqual(
            check_driving_eligibility(21, False), "You can take driving test."
        )
        self.assertEqual(check_driving_eligibility(17, True), "You cannot drive.")
        self.assertEqual(check_driving_eligibility(17, False), "You cannot drive.")

    def test_greet_name(self):
        self.assertEqual(greet_name("Ahmet"), "Hello Ahmet!")
        self.assertEqual(greet_name("John"), "Hello Stranger!")

    def test_check_name_conditions(self):
        self.assertEqual(check_name_conditions("Ahmet"), "success")
        self.assertEqual(check_name_conditions("John"), "fail")
        self.assertEqual(check_name_conditions("Ahmetoglu"), "fail")

    def test_check_name_any_conditions(self):
        self.assertEqual(check_name_any_conditions("Ahmet"), "success")
        self.assertEqual(check_name_any_conditions("JOHN"), "success")
        self.assertEqual(check_name_any_conditions("john"), "success")

    def test_compare_xyz(self):
        self.assertEqual(compare_xyz(5, 10, 15), "z is greater than x and y")
        self.assertEqual(compare_xyz(15, 10, 5), "x is greater than y")
        self.assertEqual(compare_xyz(5, 15, 10), "y is greater than z")

    def test_check_game(self):
        self.assertEqual(check_game("football"), "You are playing football.")
        self.assertEqual(check_game("basketball"), "You are playing basketball.")
        self.assertEqual(check_game("tennis"), "You are playing tennis.")
        self.assertEqual(check_game("cricket"), "You are playing something else.")

    def test_get_month_name(self):
        self.assertEqual(get_month_name(1), "January")
        self.assertEqual(get_month_name(2), "February")
        self.assertEqual(get_month_name(3), "March")
        self.assertEqual(get_month_name(4), "April")
        self.assertEqual(get_month_name(5), "May")
        self.assertEqual(get_month_name(6), "June")
        self.assertEqual(get_month_name(7), "July")
        self.assertEqual(get_month_name(8), "August")
        self.assertEqual(get_month_name(9), "September")
        self.assertEqual(get_month_name(10), "October")
        self.assertEqual(get_month_name(11), "November")
        self.assertEqual(get_month_name(12), "December")
        self.assertEqual(get_month_name(0), "Invalid month")
        self.assertEqual(get_month_name(13), "Invalid month")


if __name__ == "__main__":
    unittest.main()
