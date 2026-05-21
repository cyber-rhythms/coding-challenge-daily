# Submission.

def encrypt(text, n):
    if not text or n < 1:
        return text
    
    ciph_text = text[:len(text)]
    for _ in range(n):
        odds = [char for i, char in enumerate(ciph_text) if i % 2 == 1]
        evens = [char for i, char in enumerate(ciph_text) if i % 2 == 0]
        ciph_text = "".join(odds + evens)

    return ciph_text


def decrypt(ciph_text, n):

    if not ciph_text or n < 1:
        return ciph_text

    odd_indices = [i for i in range(len(ciph_text)) if i % 2 == 1]
    even_indices = [i for i in range(len(ciph_text)) if i % 2 == 0]
    indices = odd_indices + even_indices

    for _ in range(n):
        text = [0] * len(ciph_text)
        for index, char in zip(indices, ciph_text):
            text[index] = char
        ciph_text = text
    
    return "".join(ciph_text)

"""
Code Review.

Strengths:
- Edge case handling is fine. Variables are expressive. Intuitive zipping.

Deficiencies:
- line 7 - remember strings are immutable so don't need to worry about creating a copy using a slice. 

Remarks:
- Looking at the exploitation of the step in slicing makes my code look -- clumsy!

Solution:
- For this problem, we can make use of the slicing with customised steps `text[start:stop:step]`, meaning we save on O(n) time and space of creating index arrays.
- text[1::2]` grabs all the odd-indexed elements, and `text[::2]` the evens! 
"""

def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text

def decrypt(ciph_text, n):
    if not ciph_text or n <= 0:
        return ciph_text
    
    mid = len(text) // 2
    res = list(ciph_text)

    for _ in range(n):
        res[1::2] = text[::mid]
        res[::2] = text[mid:]
        text = "".join(res)

    return text