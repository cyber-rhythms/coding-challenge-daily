# Submission.

def unique_in_order(seq):
    return [seq[i:i+1][0] for i in range(0, len(seq)) if seq[i:i+1] != seq[i-1:i]]

# Code review.

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result