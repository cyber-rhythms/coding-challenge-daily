# Submission.

def longest_repetition(chars):
    if not chars:
        return ("", 0)

    max = [chars[0], 1]
    current = [chars[0], 1]

    for i in range(len(chars) - 1):

        # Update running character-repetition state list.
        if chars[i] == chars[i + 1]:
            current[1] += 1

            # Compare with maximum character-repetition state, if there is an update.
            if current[1] > max[1]:
                max[0], max[1] = chars[i], current[1]

        # Reset the running character-repetition state if next char is distinct.
        else:
            current[0], current[1] = chars[i + 1], 1

    return max[0], max[1]

"""
Code Review.

Strengths:
Deficiencies:
Remarks:
Solution:
"""
