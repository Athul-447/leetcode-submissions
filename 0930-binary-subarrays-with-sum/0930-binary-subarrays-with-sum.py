class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix = 0
        freq = {0:1}
        for n in nums:
            prefix += n
            needed = prefix - goal
            if needed in freq:
                count += freq[needed]
            freq[prefix] = freq.get(prefix,0) + 1
        return count