# Submission.

from fractions import Fraction

def integer_sum(n):
    return n * (n + 1) // 2

def square_sum(n):
    return (n * (n + 1) * (2*n + 1)) // 6

def expected_value(r, c):
    denom = ((r + 1)*(c + 1))
    num = (((c + 1) * square_sum(r)) 
            + (2 * integer_sum(r) * integer_sum(c))
            + ((r + 1) * square_sum(c)))
    return Fraction(num, denom)