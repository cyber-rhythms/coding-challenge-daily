# Submission.

import string

def char_id(prev_char_id, current_ciph_id):
    diff = prev_char_id - current_ciph_id
    return diff if (0 <= diff and diff <= 76) else 77 + diff

def encrypt(text):
    # Empty or null string exit.
    if not text:
        return text

    # Get characters allowable by the rubric.
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    digits = string.digits
    misc_chars = ".,:;-?! \'()$%&\""
    all_chars = "".join([uppers, lowers, digits, misc_chars])

    # Disallowable character exit.
    if not set(text) <= set(all_chars):
        raise Exception("Input string has disallowable characters")

    # Build dictionaries - second dictionary for quick lookup.
    indices = {char: i for i, char in enumerate(all_chars)}
    chars = {i: char for i, char in enumerate(all_chars)}

    # Stage 1: Case switching.
    swapped_case = [char if i % 2 == 0 else char.swapcase() for i, char in enumerate(text)]

    result = []
    for prev, current in zip(swapped_case[:-1], swapped_case[1:]):

        # Stage 2: Apply the (bizarre) index-diff transformation as specified in rubric.
        index_diff = indices[prev] - indices[current]
        new_index = index_diff + 77 if index_diff < 0 else index_diff
        result.append(chars[new_index])

    # Stage 3: "Mirror" the first character.
    index = indices[swapped_case[0]]
    max_index = len(indices) - 1
    new_index = max_index - index
    result.insert(0, chars[new_index])

    return "".join(result)

def decrypt(ciph_text):

    if not ciph_text:
        return ciph_text

    # Get characters allowable by the rubric.
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    digits = string.digits
    misc_chars = ".,:;-?! \'()$%&\""
    all_chars = "".join([uppers, lowers, digits, misc_chars])

    # Disallowable character exit.
    if not set(ciph_text) <= set(all_chars):
        raise Exception("Input string has disallowable characters")

    # Build dictionaries - second dictionary for quick lookup.
    indices = {char: i for i, char in enumerate(all_chars)}
    chars = {i: char for i, char in enumerate(all_chars)}

    # Stage 3 inverse: Undo mirroring of the first character.
    result = []
    ciph_index_0 = indices[ciph_text[0]]
    max_index = len(indices) - 1
    index_0 = max_index - ciph_index_0
    result.append(chars[index_0])
    
    # Stage 2 inverse: Undo the index difference.
    prev_index = index_0
    for i in range(1, len(ciph_text)):
        current_ciph_index = indices[ciph_text[i]]
        current_index = char_id(prev_index, current_ciph_index)
        result.append(chars[current_index])
        prev_index = current_index

    # Stage 1 inverse: Undo case-swapping.
    return "".join([char if i % 2 == 0 else char.swapcase() for i, char in enumerate(result)])

"""
Code Review.

Strengths:
- 
Deficiencies:
Remarks:
Solution:
"""
