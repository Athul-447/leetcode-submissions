class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest =nums[1] + nums[2] + nums[0]
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total-target) < abs(closest-target):
                    closest = total

                elif total<target:
                    l+=1
                else:
                    r-=1

        return closest