class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if len(t)>len(s):
            return ""
        need = Counter(t)
        window = {}
        have = 0
        needcount = len(need)
        left =0
        reslen = float('inf')
        res= [-1,-1]
        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1+window.get(ch,0)
            if ch in need and window[ch] == need[ch]:
                have+=1
            while have == needcount:
                if right-left+1 <reslen:
                    reslen = right-left+1
                    res = [left,right]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        l,r = res
        return s[l:r+1] if reslen != float('inf') else ""            
            