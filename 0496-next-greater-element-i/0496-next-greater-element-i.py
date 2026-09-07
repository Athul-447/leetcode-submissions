class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                greater[nums2[i]] = stack[-1]
            else:
                greater[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(greater[num])
        return ans