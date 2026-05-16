# Submission.

def prod_fib(ref):

    # Initialise a while loop.
    fib = [0, 1]
    prod = fib[-1] * fib[-2]

    while prod < ref:
        fib_num = sum(fib[-1: -3: -1])
        fib.append(fib_num)
        prod = fib[-1] * fib[-2]

    return [fib[-1], fib[-2], prod == ref]

"""
Code Review.

Strengths: 

Deficiencies:
- $O(n)$ space complexity for a single query kata.

Remarks:
- Now you've covered some DSA - the solution below compared with yours is a
classic example of space time complexity trade off.
- Your space complexity is $O(n)$, whereas solution below is space complexity O(1).
- All depends on how many queries you need - for this kata, solution below is better.

Solution:
"""

def prod_fib(ref):
    a, b = 0, 1
    while a * b < ref:
        a, b = b, a + b
    return [a, b, ref == a * b]