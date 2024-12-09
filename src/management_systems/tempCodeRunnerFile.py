import re

def LongestWord(sentence):
    """
    Find the longest word in a given sentence.
    """
    words = re.findall(r'\b\w+\b', sentence)
    longest_word = max(words, key=len)
    return longest_word

# keep this function call here 
try:
    user_input = input()
except EOFError:
    user_input = "I love dogs"  # Default input for testing
print(LongestWord(user_input))