class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}
        for n in nums:
            prefix += n
            remainder = prefix%k
            if remainder in freq:
                count += freq[remainder]
            freq[remainder] = 1 + freq.get(remainder,0)
        return count