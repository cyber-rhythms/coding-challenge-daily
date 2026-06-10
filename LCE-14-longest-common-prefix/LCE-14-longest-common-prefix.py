# Submission.
# 

class Solution:
    def longestCommonPrefix(self, arr: list[str]) -> str:

        # Find the shortest word length.
        shortest_word_length = min(map(len, arr))
    
        common_prefix = []
        for i in range(shortest_word_length):
            characters = set(word[i] for word in arr)
        
            # Letters common to every word in the array will yield a singleton `characters` set.
            if len(characters) > 1:
                return "".join(common_prefix)
            else:
                common_prefix.append(*characters)
        return "".join(common_prefix)

"""
Code Review.

Strengths:
-  Finding shortest word length is intentional - remember it is O(n) time to find a minimum.
-  Using set properties to detect mismatched characters is also good.

Deficiencies:
- Big memory overhead for creating a set object with a generator expression for every single index.
- Non-idiomatic unpacking of a singleton set `common_prefix.append(*characters)`

Remarks:
- You correctly identified in your notebook that you could use `zip(*strs)` was a good way to take the $k$th element of every word in the array.
- But got stuck in thinking you needed an expanded list of iterators `for kth_char_1, kth_char_2, ..., kth_char_n in zip(*strs)`!
- Time 

Solution:
- Notice how using `zip(*strs)` simultaneously extracts the $k$th character of every word in the array.
- And also automatically terminates when shortest string is exhausted - meaning no need to find the shortest word length.
- And also notice how using enumerate means that we automatically return the longest common prefix without creating an empty list.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Group characters by column index across all strings in the array.
        # `zip(*strs)` does so, and automatically terminates when shortest string exhausted.
        for i, characters in enumerate(zip(*strs)):
            unique_chars = set(characters)
            if len(unique_chars) > 1:
                return strs[0:i]
        
        # If no mismatch is found - shortest string is the longest prefix.
        return min(strs, key=len)


