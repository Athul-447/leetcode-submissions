class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        count = {0:-1}
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in count:
                ans = max(ans,i-count[prefix])
            else:
                count[prefix] = i
        return ans
            