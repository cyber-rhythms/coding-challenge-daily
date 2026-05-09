# Final submission.

def is_pangram(string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    string = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
    chars = {char.lower() for char in string if char.isalpha()}
    membership = [1 if letter in chars else 0 for letter in alphabet]
    return len(membership) == 26 and all(membership)

# Code review: Could have coded an early exit, and your len(membership) == 26 is redundant. Here is a cleaner solution using set membership.

import string
def is_pangram(string):
    return set(string.ascii_lowercase) <= set(s.lower())