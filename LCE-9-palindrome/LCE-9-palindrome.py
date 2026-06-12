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

Strengths: 
* Correct, readable implementation of two pointers.

Deficiencies: 
* O(n) space complexity for storing the number as a string, then a list.

Remarks:
* Whole point of two pointers is that you don't actually need to store anything in memory per se.

Solution:
* See the notebook as there is quite a long going on in the following condensed solution.
* New idea here: Use modulo division as a way of effectively indexing integers (which aren't iterable).
* To assess palindrome, compare first half of digits in x and second half of digits in x (latter in reverse order).
* Use indefinite iteration, and incrementally shift digits from x to construct a bottom half of digits (in reverse order).
* Metaphor - scale balancing/coin transfer between piles, using modulo division to shift digits.

"""
# More space-efficient imperative solution.
# O(n) time, O(1) space.

class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        # Filter out negative integers and positive multiples of 10.
        # Allow 0 through.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # "Scale balancing".
        # Shift digits from end of x to build bottom_half_x in reverse.
        bottom_half_x = 0 
        while x > bottom_half_x:
            bottom_half_x = (bottom_half_x * 10) + (x % 10)
            x //= 10
        
        # Even lengths (2n digits): Standard comparison to check if palindrome.
        # Odd lengths (2n + 1 digits): Here, x will have n digits and bottom_half_x has n + 1 digits.
        # Final digit of bottom_half_x will be the middle digit of original integer, so drop it, then compare.
        return (x == bottom_half_x or x == bottom_half_x // 10)

