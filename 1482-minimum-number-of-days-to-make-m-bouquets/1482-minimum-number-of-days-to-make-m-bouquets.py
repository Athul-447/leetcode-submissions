class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l<=r:
            mid = (l+r) // 2
            flower = 0
            bouquet = 0
            for day in bloomDay:
                if day <= mid:
                    flower+= 1
                    if flower == k:
                        bouquet += 1
                        flower = 0
                else:
                    flower = 0
            if bouquet >= m:
                r  = mid-1
            else:
                l = mid+1
        return l