class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}
        for n in nums:
            if n%2 == 1:
                prefix+=1
            needed = prefix - k
            if needed in freq:
                count+= freq[needed]
            freq[prefix] = 1 + freq.get(prefix,0)
        return count