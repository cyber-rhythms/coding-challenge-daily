# Submission.

def tribonacci(sig, n):

    # A sequence of at most the signature length only requires a slice.
    if n <= 3:
        return sig[:n]
    
    # Otherwise carry out recursion.
    else:
        current_sum = sum(sig)
        sig.append(current_sum)

        for i in range(1, n-3):
            current_sum = sum(sig[i:])
            sig.append(current_sum)


"""
Code Review.

Strengths: 
- O(n) time complexity.

Deficiencies:
- Mutation of original input in-place - a big blooper. Can introduce subtle bugs.
- Slicing logic is fragile - coupling of slice index `i` to the loop iterator means
that whoever reading has to manually state-track.
- Code redundancy - An extra iteration outside the loop means extra work in counting
how many iterations for the person reading.

Remarks:
- Remember, slicing in Python generates a shallow copy (unlike Numpy views).
- Code readability also encompasses the logic e.g. indexing being sufficient clear,
so it can be clearly gleaned without using a debugger to track indices/state.
- Declarative/intentional code explicitly tells the reader what is being done, without
the need for inference/manual state tracking etc.
- And professional code wraps edge cases really cleanly into the logic.

Solution:
- The one below wraps edge cases much more cleanly, creates a copy, and is much more intentional code.

"""

def tribonacci(signature: list[int | float], n: int) -> list[int | float]:

    if n <= 0:
        return []
    
    # Create shallow copy. If n < len(signature), this handles the edge cases.
    # Otherwise, we "over-slice" and it returns the full signature.
    result = signature[:n]

    # Half-open interval for range, so we generate $n - len(result)$ Fibonacci nos.
    # If $n <= len(signature), range(0) bypasses the loop entirely.
    # Loop iterator index and slicing decoupled, and iteration count is declarative.
    for _ in range(n - len(result)):
        result.append(sum(result[-3:]))

    return result

