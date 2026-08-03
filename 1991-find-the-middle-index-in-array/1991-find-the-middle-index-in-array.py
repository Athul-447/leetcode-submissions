class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=0
        total = sum(nums)
        for i in range(len(nums)):
            rsum = total-lsum-nums[i]
            if lsum==rsum:
                return i
            lsum += nums[i]
        return -1