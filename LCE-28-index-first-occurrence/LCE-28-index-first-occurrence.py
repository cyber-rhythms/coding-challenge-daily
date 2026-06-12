# Submission.
# O((n-k+1)k) time, O(k) space.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        k = len(needle)
        for i in range(n-k+1):
            current_window = haystack[i:i+k]
            if needle == current_window:
                return i
        return -1

"""
Code Review.

Strengths:
Deficiencies:
Remarks:
* Given that you already know that the declarative solution is `haystack.find(needle)`, your choice to write imperative code to check is fine.
* But your is a half-way house -- in that slicing is somewhat inefficient memory-wise.

* Below is template for last index of sliding window and number of sliding windows.
for length `n` array, with length `k` sliding window.
* Partitioning integers `1, 2, ..., n-k | n-k+1, ... , n` gives n-k and k integers.
* The last k integers form the last length `k` sliding window, so n-k+1 sliding windows in total.
* We want to run n - k + 1 iterations, corresponding to each sliding window.
* So range(n - k + 1), and because this is half-open, final index is n - k.

* Before getting bogged down in CPython internals - for now, a length-k slice is O(k) time and O(k) space.

Solution:
* Solution to assume a `match` and then override if there is a mismatch avoids having to track matched characters (unlike your notebook solution) using a counter.
* Avoidance of length-k slicing means O(1) space instead of O(k).
"""
# Fully imperative solution.
# O((n-k+1)k) time and O(1) space.

def strStr(haystack, needle):
    n = len(haystack)
    k = len(needle)

    for i in range(n-k+1):
        # Instead of comparing a slice, and instead of counting matched characters, use a match Boolean default to True, then override inside inner loop.
        match = True
        for j in range(k):
            if haystack[i + j] != needle[j]:
                match = False
                break
    else:
        return i
    return -1
