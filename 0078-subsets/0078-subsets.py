class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        cur = []
        res = []
        def backtracking(i):
            if i == n:
                res.append(cur.copy())
                return
            
            backtracking(i+1)

            cur.append(nums[i])
            backtracking(i+1)
            cur.pop()
        backtracking(0)
        return res
