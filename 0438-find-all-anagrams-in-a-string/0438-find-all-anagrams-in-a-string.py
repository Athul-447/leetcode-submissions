class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        from collections import Counter
        need = Counter(p)
        window = Counter(s[0:len(p)])
        if need == window:
            ans.append(0)
        for i in range(len(p),len(s)):
            left = s[i-len(p)]
            right = s[i]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            window[right] += 1
            if need == window:
                ans.append(i-len(p)+1)
        return ans