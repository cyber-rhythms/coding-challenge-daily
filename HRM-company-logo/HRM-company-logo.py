# Submission.

# HINT: Issue if you use `counter.most_common(n)` is that if you have ties on letter counts involving more than three letters, using the `counter.most_common(3)` method will mean that you will select an arbitrary slice in the orders they were added, and not alphabetically.

# When you cover sorting algorithms in DSA, and multi-pass sorting, make sure you have a look at sorting algorithm "stability".


from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    
    # Sort alphabetically first, then by frequency.
    alphabetic_order = sorted(counts.items())
    freq_order = sorted(alphabetic_order, key=lambda x: x[1], reverse=True)
    
    for letter, count in freq_order[:3]:
        print(f"{letter} {count}")

"""
Code Review.

Strengths:
- Good to use `collections.Counter`, and to sort it to preserve key-value association using `sorted(Counter.items())`.
- Time complexity is O(U log U), where U is number of unique string characters.

Deficiencies:
- Allocation of two intermediate lists in memory.

Remarks: 

- What this problem looks at is how to coordinate a situation where you have to multi-pass sort the data by multiple, prioritised criteria -  frequency and alphabetically.
- You didn't have a declarative solution available, so coded imperatively - fine.
- Sorting by dominant freq. criterion first, then by secondary alphabetic criterion requires complex code that needs to detect ties, isolate tied sub-arrays, and then implementing a secondary sort(s) on these localised
areas.
- Counter-intuitively: Sort by least important criterion first, then the most important last.
- If the latter is a stable sorting algorithm, then it preserves first pass.

Solution:

- A cleaner declarative approach does what you effectively wrote imperatively, except using the `key` parameter of `sorted()` to handle a multi-pass sort.
- Passing the key function (-x[1], x[0]) is because `sorted()` is by default ascending, and `reverse=True` is a global modifier, and we want descending order only on the frequency.
- Python loops through comparing each tuple lexicographically (left -> right), so that if there are ties in comparing first element of the tuples, then defer to the second element of the tuple to compare.
"""

from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    sorted_counts = sorted(counts.items(), keys=lambda x: (-x[1], x[0]))

    for letter, count in sorted_counts[:3]:
         print(f"{letter} {count}")

