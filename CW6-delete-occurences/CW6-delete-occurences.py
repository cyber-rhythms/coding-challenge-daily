from collections import defaultdict

def delete_nth(lst, N):
    result = []
    counts = defaultdict(int)
    for x in lst:
        if counts[x] < N:
            result.append(x)
            counts[x] += 1

    return result