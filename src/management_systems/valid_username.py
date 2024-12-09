"""
Codeland Username Validation

Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples

Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true


"""

# def CodelandUsernameValidation(strParam):
#     if len(strParam) < 4 and len(strParam) > 25:
#         return 'false'
#     if not strParam[0].isalpha():
#         return 'false' 
#     if not strParam.isalnum:
#         return 'false'
#     if strParam[-1] == '_':
#        return 'false'
#     return 'true'

#   # # code goes here
#   # return strParam

# # keep this function call here 
# print(CodelandUsernameValidation("u__hello_world123"))


"""
Longest Word

Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. 
Words may also contain numbers, for example "Hello world123 567"
Examples

Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
Tags

"""
def LongestWord(sentence):
    """
    Find the longest word in a given sentence.
    """
    # Remove non-alphanumeric characters and split the sentence into words
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in sentence).split()
    longest_word = max(words, key=len)
    return longest_word

# Test cases
test_cases = [
    "hello world",
    "this is some sort of sentence",
    "longest word!!",
    "coderbyte",
    "a beautiful sentence^&!",
    "oxford press",
    "123456789 98765432",
    "letter after letter!!",
    "a b c dee",
    "a confusing /:sentence:/[ this is not!!!!!!!~"
]

# Run the test cases
for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {LongestWord(test)}")
    print()