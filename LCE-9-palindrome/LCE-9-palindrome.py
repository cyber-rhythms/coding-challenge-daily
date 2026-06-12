# Submission.
# https://leetcode.com/problems/palindrome-number/description/
# O(n) time, O(n) space.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = list(str(x))
        left = 0
        right = len(digits) - 1
        while left <= right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True

"""
Code Review.

Strengths: Correct, readable.
Deficiencies: O(n) space complexity for storing the number as a string, then a list.
Remarks:
* Whole point of two pointers is that you don't actually need to store anything in memory per se.
Solution:
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = list(str(x))
        left = 0
        right = len(digits) - 1
        while left <= right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True

