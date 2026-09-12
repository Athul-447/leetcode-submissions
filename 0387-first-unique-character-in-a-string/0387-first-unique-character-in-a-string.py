class Solution:
    def firstUniqChar(self, s: str) -> int:
        HashMap = {}
        for i in range(len(s)):
            HashMap[s[i]] = 1 + HashMap.get(s[i],0)
        for i in range(len(s)):
            if HashMap[s[i]] == 1:
                return i
        return -1
