# Submission.
# O(n) time and O(n) space.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

"""
Code Review.

Strengths: 
* Declarative one-liner.

Deficiencies:
* Space complexity of O(n) to store a list of pointers in `s.split()`.

Remarks:
* This is a situation where the use of a built-in function, whilst declarative cleaner, is less memory efficient.
* Learning to recognise that imperative look-aheads with if-else conditoons are generally a no-no as too fragile.
* Instead, use Boolean state tracking, which is the most elemental example of tokenization.

Alternate submission:
* Imperative method using Boolean state tracking O(n) time and O(1) space.
* For real-world cases, worst-case asymptotic time O(n) masks the following.
* In practice, imperative version is O(k) time, where k is length of last word, due to early exit.
* And for many real-world applications k << n.
"""

# A faster imperative submission.
# O(n) time and O(1) space.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        # Boolean state tracking to differentiate between whitespace at end of word, and before a letter.
        word_started = False

        for char in reversed(s):
            if char != " ":
                length += 1
                if not word_started:
                    word_started = True
            elif word_started:
                return length
            
        # Successful loop completion happens when the string is a single word, return length.
        return length
