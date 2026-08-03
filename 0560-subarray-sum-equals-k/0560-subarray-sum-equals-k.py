class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = {0:1}
        ans = 0
        for num in nums:
            prefix += num
            if prefix - k in count:
                ans += count[prefix-k]
            
            count[prefix] = 1 + count.get(prefix,0)
        return ans