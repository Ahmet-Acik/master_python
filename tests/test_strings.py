import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from strings import (
    declare_and_assign,
    concatenate_strings,
    repeat_string,
    format_string,
    slice_string,
    string_methods,
    get_character_in_name,
    get_substring,
    get_quote_slices,
    get_learning_fun_slices,
    reverse_string,
    concatenate_names,
    repeat_string,
    format_string,
    string_methods,
)


class TestStrings(unittest.TestCase):

    def test_declare_and_assign(self):
        self.assertEqual(declare_and_assign(), "Hello, World!")

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")

    def test_repeat_string(self):
        self.assertEqual(repeat_string("Hello", 3), "HelloHelloHello")

    def test_format_string(self):
        self.assertEqual(
            format_string("Ahmet", 21), "My name is Ahmet and I am 21 years old."
        )

    def test_slice_string(self):
        self.assertEqual(slice_string("Hello, World!", 0, 5), "Hello")

    def test_string_methods(self):
        methods = string_methods("Hello, World!")
        self.assertEqual(methods["upper"], "HELLO, WORLD!")
        self.assertEqual(methods["lower"], "hello, world!")
        self.assertEqual(methods["capitalize"], "Hello, world!")
        self.assertEqual(methods["title"], "Hello, World!")
        self.assertEqual(methods["swapcase"], "hELLO, wORLD!")
        self.assertEqual(methods["strip"], "Hello, World!")
        self.assertEqual(methods["lstrip"], "Hello, World!")
        self.assertEqual(methods["rstrip"], "Hello, World!")
        self.assertEqual(methods["find"], 7)
        self.assertEqual(methods["replace"], "Hello, World!")
        self.assertEqual(methods["split"], ["Hello,", "World!"])
        self.assertEqual(methods["join"], "H-e-l-l-o-,- -W-o-r-l-d-!")
        self.assertTrue(methods["startswith"])
        self.assertTrue(methods["endswith"])
        self.assertFalse(methods["isalpha"])
        self.assertFalse(methods["isdigit"])
        self.assertFalse(methods["isalnum"])
        self.assertFalse(methods["isspace"])
        self.assertFalse(methods["islower"])
        self.assertFalse(methods["isupper"])
        self.assertFalse(methods["istitle"])

    def test_get_character_in_name(self):
        self.assertEqual(get_character_in_name("Ahmetoglu", 0), "A")
        self.assertEqual(get_character_in_name("Ahmetoglu", -1), "u")

    def test_get_substring(self):
        self.assertEqual(get_substring("Ahmetoglu", 0, 3), "Ahm")

    def test_get_quote_slices(self):
        quote = "The greatest glory in living lies not in never falling, but in rising every time we fall."
        slices = get_quote_slices(quote)
        self.assertEqual(slices["slice_0_10"], "The greate")
        self.assertEqual(slices["slice_10_20"], "st glory i")
        self.assertEqual(slices["slice_20_30"], "n living l")
        self.assertEqual(slices["slice_30_40"], "ies not in")
        self.assertEqual(slices["full_quote"], quote)
        self.assertEqual(slices["slice_3_16_2"], " raetgo")
        self.assertEqual(
            slices["slice_2_step"], "Tegets lr nlvn isnti ee aln,bti iigeeytm efl."
        )

    def test_get_learning_fun_slices(self):
        learning_fun = "Python is fun"
        slices = get_learning_fun_slices(learning_fun)
        self.assertEqual(slices["slice_10_end"], "fun")
        self.assertEqual(slices["slice_0_6"], "Python")
        self.assertEqual(slices["slice_7_9"], "is")
        self.assertEqual(slices["slice_neg_3_end"], "fun")
        self.assertEqual(slices["slice_0_neg_4"], "Python is")
        self.assertEqual(slices["reversed"], "nuf si nohtyP")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Ahmetoglu"), "ulgotemhA")

    def test_concatenate_names(self):
        self.assertEqual(concatenate_names("Ahmet", "Oglu"), "Ahmet Oglu")

    def test_repeat_string(self):
        self.assertEqual(
            repeat_string("Ahmet Oglu", 3), "Ahmet OgluAhmet OgluAhmet Oglu"
        )

    def test_format_string(self):
        formatted = format_string("Ahmet", 40)
        self.assertEqual(formatted["concat"], "My name is Ahmet and I am 40 years old.")
        self.assertEqual(formatted["format"], "My name is Ahmet and I am 40 years old.")
        self.assertEqual(
            formatted["f_string"], "My name is Ahmet and I am 40 years old."
        )

    def test_string_methods(self):
        methods = string_methods("Ahmet")
        self.assertEqual(methods["upper"], "AHMET")
        self.assertEqual(methods["lower"], "ahmet")
        self.assertEqual(methods["capitalize"], "Ahmet")
        self.assertEqual(methods["find_h"], 1)
        self.assertEqual(methods["count_h"], 1)
        self.assertEqual(methods["find_z"], -1)
        self.assertEqual(methods["replace_A_Z"], "Zhmet")
        self.assertTrue(methods["startswith_A"])
        self.assertTrue(methods["endswith_t"])
        self.assertTrue(methods["isalpha"])
        self.assertFalse(methods["isnumeric"])
        self.assertFalse(methods["isdigit"])
        self.assertTrue(methods["isalnum"])
        self.assertFalse(methods["isspace"])
        self.assertFalse(methods["islower"])
        self.assertFalse(methods["isupper"])
        self.assertTrue(methods["istitle"])
        self.assertEqual(methods["title"], "Ahmet")
        self.assertEqual(methods["swapcase"], "aHMET")
        self.assertEqual(methods["strip"], "Ahmet")
        self.assertEqual(methods["lstrip"], "Ahmet")
        self.assertEqual(methods["rstrip"], "Ahmet")
        self.assertEqual(methods["center_20"], "*******Ahmet********")
        self.assertEqual(methods["ljust_20"], "Ahmet***************")
        self.assertEqual(methods["rjust_20"], "***************Ahmet")
        self.assertEqual(methods["zfill_20"], "0000000000000000Ahmet")
        self.assertEqual(methods["partition_m"], ("Ah", "m", "et"))
        self.assertEqual(methods["rpartition_m"], ("Ah", "m", "et"))
        self.assertEqual(methods["split_m"], ["Ah", "et"])
        self.assertEqual(methods["rsplit_m"], ["Ah", "et"])
        self.assertEqual(methods["splitlines"], ["Ahmet"])
        self.assertEqual(methods["join_123"], "1Ahmet2Ahmet3")
        self.assertEqual(methods["join_list"], "1Ahmet2Ahmet3")
        self.assertEqual(methods["encode"], b"Ahmet")
        self.assertEqual(methods["encode_utf_8"], b"Ahmet")
        self.assertEqual(methods["encode_utf_16"], b"\xff\xfeA\x00h\x00m\x00e\x00t\x00")
        self.assertEqual(
            methods["encode_utf_32"],
            b"\xff\xfe\x00\x00A\x00\x00\x00h\x00\x00\x00m\x00\x00\x00e\x00\x00\x00t\x00\x00\x00",
        )
        self.assertEqual(methods["encode_ascii"], b"Ahmet")
        self.assertEqual(methods["encode_latin_1"], b"Ahmet")
        self.assertEqual(methods["encode_cp1254"], b"Ahmet")
        self.assertEqual(methods["encode_cp857"], b"Ahmet")
        self.assertEqual(methods["encode_cp1252"], b"Ahmet")


if __name__ == "__main__":
    unittest.main()
