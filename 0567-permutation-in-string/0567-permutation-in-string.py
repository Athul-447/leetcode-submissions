class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) >len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[0:len(s1)])
        if need == window:
            return True
        for i in range(len(s1),len(s2)):
            left = s2[i - len(s1)]
            right = s2[i]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            window[right] += 1
            if need ==  window:
                return True
        return False