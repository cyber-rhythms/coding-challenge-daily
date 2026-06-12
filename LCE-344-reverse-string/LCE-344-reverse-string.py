# Submission.
# O(n) time complexity, O(1) space complexity.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Set left and right pointers at beginning and end of list.
        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

"""
Code Review.

Strengths:
* Good reproduction of two-pointers.
* Good that you are doing simultaneous assignment for index swapping rather than assigning to an intermediate temp variable.

Deficiencies:
* Strictly, only require `while left < right`.
* Because for odd cardinality arrays, then yours carries out a redundant computation. 

Remarks:
* Declarative version, optimised version of this is `s.reverse()`.
* In your notebook, you wrote that "the only safe way to mutate an iterable whilst looping over is two pointers."
* Not necessarily. Modifying an iterable whilst expanding or shrinking i.e. structural mutation, can cause index bugs.
* But if iterable is fixed, and you are only mutating element by index - standard loops are safe.
* Two-pointers is one way -- could also do until the mid-point.

Solution:
"""
