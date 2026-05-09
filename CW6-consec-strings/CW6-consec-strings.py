# Submission.

def longest_consec(str_arr, k):

    n = len(str_arr)
    if n == 0 or k > n or k <= 0:
        return ""

    len_arr = list(map(len, str_arr))
    
    # The sums of any partial slices after the final complete length k slice will get smaller, and won't be detected by max. 
    sum_arr = [sum(len_arr[i:i+k]) for i in range(n)]
    max_len = max(sum_arr)

    for i in range(num_strings):
        if sum_arr[i] == max_len:
            return "".join(str_arr[i:i+k])

###------------------------------ Code review.-----------------------------------###
         
def longest_consec(str_arr, k):

    n = len(str_arr)
    if n == 0 or k > n or k <= 0:
        return ""

    lens = [len(s) for s in str_arr]

    # Sum of the first window.
    current_len = sum(lens[:k])
    max_len = current_len
    best_index = 0

    # Slide window of length k across array, using array indexing to enforce fixed length.
    # An array of length n can pass (n - (k - 1)) sliding windows of length k.
    for i in range(n-k):
        current_len = current_len - lens[i] + lens[i + k]
        if current_len > max_len:
            max_len = current_len
            best_index = i + 1

    return "".join(str_arr[best_index : best_index + k])