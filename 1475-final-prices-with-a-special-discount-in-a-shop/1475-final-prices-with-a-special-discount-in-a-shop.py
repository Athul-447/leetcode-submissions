class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)-1,-1,-1):
            current = prices[i]
            while stack and stack[-1] > current:
                stack.pop()
            if stack:
                prices[i] = current - stack[-1]
            stack.append(current)
        return prices