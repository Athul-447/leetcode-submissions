class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indices = sorted(range(len(score)),key = lambda i:score[i], reverse =True)

        ans = [""] * len(score)

        for i in range(len(score)):
            index = indices[i]

            if i == 0:
                ans[index] = "Gold Medal"

            elif i == 1:
                ans[index] = "Silver Medal"

            elif i == 2:
                ans[index] = "Bronze Medal"

            else:
                ans[index] = str(i + 1)

        return ans
