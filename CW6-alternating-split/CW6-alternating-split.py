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
- 

Remarks:
- A much cleverer solution that is also efficine is to slice

Solution:
"""