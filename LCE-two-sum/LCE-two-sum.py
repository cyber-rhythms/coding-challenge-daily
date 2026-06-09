# Submission.
# Can only see an $O(n^2 / 2) = O(n^2)$ time, $O(1)$ space brute-force solution for this. - write it out first then review.

class Solution:
    def brute_twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        # Iterate through each element in the array.
        for i in range(n):
            # Iterate through subsequent elements in the array, excluding same element pairs.
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
Code Review - see notebook.

Strengths:
Deficiencies:
Remarks:
Solution:
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = dict()
        for index, num in enumerate(nums):
            complement = target - num

            # O(1) lookup of complement in hash-map rather than an O(n) backwards linear search. 
            if complement in hash_map:
                index_2 = hash_map[complement]
                return [index, index_2]
            
            # Add current element-index pair to hash-map if complement not found.
            hash_map[num] = index
        return []
