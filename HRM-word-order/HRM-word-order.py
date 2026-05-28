# Submission.

from collections import OrderedDict

if __name__ == "__main__":
    word_counts = OrderedDict()

    N = int(input())
    for _ in range(N):
        word = input()
        word_counts[word] = word_counts.get(word, 0) + 1

    print(len(word_counts))
    print(" ".join(str(count) for count in word_counts.values()))

"""
Code Review.

Strengths:
Deficiencies:
Remarks:
Solution:
"""
