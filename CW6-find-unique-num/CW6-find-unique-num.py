# Submission.

from collections import Counter
def find_uniq(arr):
    counter = Counter(arr)

    for key in counter:
        if counter[key] == 1:
            return key

"""
Code Review.

Strengths: 
- Recognition that collections.Counter can be used here instead of manual coding of a dictionary.

Deficiencies:
- collections.Counter is worst-case O(n) time complexity, then single linear pass to search is O(k) time complexity, which ends up being O(1), and so in total O(n) time complexity.
- If you have very large array sizes then this could be an issue.

Remarks: 

Solution:
- Consider the following short-circuit evaluation - which circumvents the need to build a large dictionary.
- Three scenarios.
-  1. First element unique [A, B, B, ...]
-  2. Second element unique [B, A, B, ...]
-  3. Unique element further down the list [B, B, B,..., A,...]
- 1 and 2. wrapped into an early exit guard clause, an edge case where unique value is in the first two slots. 
- 3. covered by linear search.

"""

def find_uniq(arr):

    # Edge case early exit where unique value is in first two positions of the array.
    if arr[0] != arr[1]:
        return arr[0] if arr[0] != arr[2] else arr[2]
    
    # If we get here then arr[0] is the common number.
    common = arr[0]
    for x in arr:
        if x != common:
            return x
    

    
    

