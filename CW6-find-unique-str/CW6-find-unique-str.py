# Submission.

def find_uniq(arr: list[str]) -> str:
    
    signature_0, signature_1 = set(arr[0].lower()), set(arr[1].lower())

    # Edge case early exit.
    # If first two elements differ, use third element to deduce unique value.
    if signature_0 != signature_1:
        signature_2 = set(arr[2].lower())
        return arr[0] if signature_0 != signature_2 else arr[1]
    
    # Otherwise, first element is common value, linear search for unique value.
    common = signature_0
    for string in arr[2:]:
        signature = set(string.lower())
        if signature != common:
            return string

"""
Code Review.

Strengths: 

- Excellent,, performant code.
- Space complexity: $O(M)$ in the length of the string - hold 3 length $M$ sets in memory.
- Time complexity: $O(n)$ in the length of the array - but short circuiting may reduce average time.

Deficiencies:
- Whilst code is performant, the somewhat finnicky three element logic could be made more readable without those nested if/else statements.

Remarks:

- Good to see you are learning from the previous kata - and this time chose not to form a dictionary of counts to find the unique element (space expensive).
- An example of eager evaluation vs early exit saving space.

Solution:
"""


