# Submission.

import string

def find_missing_letter(chars):

    # Check whether array contains upper or lower, construct alphabet.
    if chars[0].isupper():
        alphabet = string.ascii_uppercase
    elif chars[0].islower():
        alphabet = string.ascii_lowercase

    letters = "".join(chars)
    for i in range(len(letters)):

        substring = letters[i:i+2]

        if alphabet.find(substring) == -1:
            index = alphabet.find(substring[0]) + 1
            return alphabet[index]
        
# Code review.
# Better way. Input is ordered, and is subset of reference alphabet. 
# First character of input gives us starting point to check against reference alphabet.
# Compare each character of the input string and the reference alphabet -- if there is a discrepancy, then the alphabet letter is the missing one.

import string

def find_missing_letter2(chars):
    ref = string.ascii_lowercase if chars[0].islower() else string.ascii_uppercase
    start = ref.find(chars[0])

    for i, char in enumerate(chars):
        print(char, ref[start + i])
        if char != ref[start + i]:
            return ref[start + i]