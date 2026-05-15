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

# Code review.

# When submitting make sure to refactor any list comprehensions which you are using to track state, as they are O(n) memory-wise.
# And notice how much cleaner and more surgically this can be achieved with simple tuple unpacking.

def prod_fib(ref):
    a, b = 0, 1
    while a * b < ref:
        a, b = b, a + b
    return [a, b, ref == a * b]