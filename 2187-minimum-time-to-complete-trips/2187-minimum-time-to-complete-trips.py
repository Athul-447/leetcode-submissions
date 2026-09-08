class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = min(time) * totalTrips
        while l <= r:
            mid = ( l+r ) // 2
            trip = 0
            for t in time:
                trip += mid // t
            if trip >= totalTrips:
                r = mid-1
            else:
                l = mid +1
        return l
