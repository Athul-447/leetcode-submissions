class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        nums.sort()
        for i in range(len(nums)):
            l = i +1
            r = len(nums) - 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        return ans
