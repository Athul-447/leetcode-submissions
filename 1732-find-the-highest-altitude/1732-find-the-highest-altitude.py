class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxaltitude = 0
        for g in gain:
            altitude += g
            maxaltitude = max(altitude,maxaltitude)
        return maxaltitude